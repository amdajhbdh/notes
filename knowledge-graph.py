#!/usr/bin/env python3
"""
Knowledge Graph Builder
Maps concept relationships and dependencies
"""
import sqlite3
import json
from pathlib import Path
from typing import Dict, List, Set

VAULT = Path("/home/med/Documents/bac/resources/notes/Study-Vault")
DB = VAULT / ".vault-index.db"
GRAPH_DB = VAULT / ".knowledge-graph.db"

class KnowledgeGraph:
    def __init__(self):
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(GRAPH_DB)
        c = conn.cursor()
        
        c.execute('''CREATE TABLE IF NOT EXISTS concepts (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            note_path TEXT,
            subject TEXT,
            difficulty TEXT
        )''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS relationships (
            id INTEGER PRIMARY KEY,
            from_concept INTEGER,
            to_concept INTEGER,
            rel_type TEXT,
            strength REAL,
            FOREIGN KEY(from_concept) REFERENCES concepts(id),
            FOREIGN KEY(to_concept) REFERENCES concepts(id)
        )''')
        
        conn.commit()
        conn.close()
    
    def extract_concepts(self):
        """Extract concepts from vault"""
        conn_vault = sqlite3.connect(DB)
        c = conn_vault.cursor()
        
        c.execute('''SELECT path, title, subject, type FROM notes 
                     WHERE type='concept' ''')
        notes = c.fetchall()
        conn_vault.close()
        
        conn_graph = sqlite3.connect(GRAPH_DB)
        c = conn_graph.cursor()
        
        for path, title, subject, note_type in notes:
            c.execute('''INSERT OR IGNORE INTO concepts (name, note_path, subject)
                         VALUES (?, ?, ?)''', (title, path, subject))
        
        conn_graph.commit()
        conn_graph.close()
        
        return len(notes)
    
    def build_relationships(self):
        """Build relationships from links"""
        conn_vault = sqlite3.connect(DB)
        c_vault = conn_vault.cursor()
        
        conn_graph = sqlite3.connect(GRAPH_DB)
        c_graph = conn_graph.cursor()
        
        # Get all links
        c_vault.execute('SELECT source_path, target_path FROM links')
        links = c_vault.fetchall()
        
        relationships = 0
        for source, target in links:
            # Get concept IDs
            c_graph.execute('SELECT id FROM concepts WHERE note_path=?', (source,))
            from_id = c_graph.fetchone()
            
            c_graph.execute('SELECT id FROM concepts WHERE note_path=?', (target,))
            to_id = c_graph.fetchone()
            
            if from_id and to_id:
                c_graph.execute('''INSERT OR IGNORE INTO relationships 
                                   (from_concept, to_concept, rel_type, strength)
                                   VALUES (?, ?, 'related', 1.0)''',
                               (from_id[0], to_id[0]))
                relationships += 1
        
        conn_vault.close()
        conn_graph.commit()
        conn_graph.close()
        
        return relationships
    
    def find_prerequisites(self, concept_name: str) -> List[str]:
        """Find concepts that should be learned first"""
        conn = sqlite3.connect(GRAPH_DB)
        c = conn.cursor()
        
        # Get concept ID
        c.execute('SELECT id FROM concepts WHERE name LIKE ?', (f'%{concept_name}%',))
        result = c.fetchone()
        
        if not result:
            conn.close()
            return []
        
        concept_id = result[0]
        
        # Find incoming relationships
        c.execute('''SELECT c.name FROM concepts c
                     JOIN relationships r ON c.id = r.from_concept
                     WHERE r.to_concept = ?''', (concept_id,))
        
        prereqs = [r[0] for r in c.fetchall()]
        conn.close()
        
        return prereqs
    
    def find_related(self, concept_name: str, max_results: int = 10) -> List[Dict]:
        """Find related concepts"""
        conn = sqlite3.connect(GRAPH_DB)
        c = conn.cursor()
        
        c.execute('SELECT id FROM concepts WHERE name LIKE ?', (f'%{concept_name}%',))
        result = c.fetchone()
        
        if not result:
            conn.close()
            return []
        
        concept_id = result[0]
        
        # Find all connected concepts
        c.execute('''SELECT c.name, c.subject, r.strength
                     FROM concepts c
                     JOIN relationships r ON (c.id = r.to_concept OR c.id = r.from_concept)
                     WHERE (r.from_concept = ? OR r.to_concept = ?)
                     AND c.id != ?
                     LIMIT ?''', (concept_id, concept_id, concept_id, max_results))
        
        related = [{"name": n, "subject": s, "strength": st} for n, s, st in c.fetchall()]
        conn.close()
        
        return related
    
    def suggest_learning_path(self, target_concept: str) -> List[str]:
        """Suggest optimal learning order"""
        # Simple BFS from prerequisites
        prereqs = self.find_prerequisites(target_concept)
        
        path = []
        visited = set()
        
        def dfs(concept):
            if concept in visited:
                return
            visited.add(concept)
            
            for prereq in self.find_prerequisites(concept):
                dfs(prereq)
            
            path.append(concept)
        
        dfs(target_concept)
        return path
    
    def get_stats(self) -> Dict:
        """Get graph statistics"""
        conn = sqlite3.connect(GRAPH_DB)
        c = conn.cursor()
        
        c.execute('SELECT COUNT(*) FROM concepts')
        concepts = c.fetchone()[0]
        
        c.execute('SELECT COUNT(*) FROM relationships')
        relationships = c.fetchone()[0]
        
        c.execute('SELECT subject, COUNT(*) FROM concepts GROUP BY subject')
        by_subject = dict(c.fetchall())
        
        conn.close()
        
        return {
            "concepts": concepts,
            "relationships": relationships,
            "by_subject": by_subject
        }
    
    def export_graph(self) -> Dict:
        """Export graph for visualization"""
        conn = sqlite3.connect(GRAPH_DB)
        c = conn.cursor()
        
        # Get nodes
        c.execute('SELECT id, name, subject FROM concepts')
        nodes = [{"id": i, "name": n, "subject": s} for i, n, s in c.fetchall()]
        
        # Get edges
        c.execute('SELECT from_concept, to_concept, strength FROM relationships')
        edges = [{"from": f, "to": t, "strength": s} for f, t, s in c.fetchall()]
        
        conn.close()
        
        return {"nodes": nodes, "edges": edges}

if __name__ == "__main__":
    import sys
    
    kg = KnowledgeGraph()
    
    if len(sys.argv) < 2:
        print("Usage: knowledge-graph.py <command> [args]")
        print("\nCommands:")
        print("  build              - Build graph from vault")
        print("  prereqs <concept>  - Find prerequisites")
        print("  related <concept>  - Find related concepts")
        print("  path <concept>     - Suggest learning path")
        print("  stats              - Show statistics")
        print("  export             - Export graph data")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "build":
        concepts = kg.extract_concepts()
        relationships = kg.build_relationships()
        print(f"✓ Built graph: {concepts} concepts, {relationships} relationships")
    
    elif cmd == "prereqs" and len(sys.argv) > 2:
        prereqs = kg.find_prerequisites(sys.argv[2])
        print(f"\nPrerequisites for '{sys.argv[2]}':")
        for p in prereqs:
            print(f"  • {p}")
    
    elif cmd == "related" and len(sys.argv) > 2:
        related = kg.find_related(sys.argv[2])
        print(f"\nRelated to '{sys.argv[2]}':")
        for r in related:
            print(f"  • {r['name']} ({r['subject']})")
    
    elif cmd == "path" and len(sys.argv) > 2:
        path = kg.suggest_learning_path(sys.argv[2])
        print(f"\nLearning path to '{sys.argv[2]}':")
        for i, concept in enumerate(path, 1):
            print(f"  {i}. {concept}")
    
    elif cmd == "stats":
        stats = kg.get_stats()
        print(json.dumps(stats, indent=2))
    
    elif cmd == "export":
        graph = kg.export_graph()
        print(json.dumps(graph, indent=2))
