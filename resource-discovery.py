#!/usr/bin/env python3
"""
Resource Discovery Agent
Finds educational content from web sources
"""
import json
import urllib.parse
from typing import List, Dict

class ResourceDiscovery:
    def __init__(self):
        self.sources = {
            'youtube': 'https://www.youtube.com/results?search_query=',
            'khan': 'https://www.khanacademy.org/search?page_search_query=',
            'brilliant': 'https://brilliant.org/search/?q=',
            'arxiv': 'https://arxiv.org/search/?query=',
            'mit_ocw': 'https://ocw.mit.edu/search/?q='
        }
    
    def find_videos(self, topic: str, max_results: int = 10) -> List[Dict]:
        """Find educational videos"""
        query = urllib.parse.quote(topic)
        
        results = [
            {
                "title": f"{topic} - Khan Academy",
                "url": f"{self.sources['khan']}{query}",
                "source": "Khan Academy",
                "type": "video_series",
                "quality": 0.95
            },
            {
                "title": f"{topic} - 3Blue1Brown",
                "url": f"{self.sources['youtube']}{query}+3blue1brown",
                "source": "YouTube",
                "type": "video",
                "quality": 0.98
            },
            {
                "title": f"{topic} Tutorial",
                "url": f"{self.sources['youtube']}{query}+tutorial",
                "source": "YouTube",
                "type": "video",
                "quality": 0.85
            },
            {
                "title": f"{topic} - MIT OpenCourseWare",
                "url": f"{self.sources['mit_ocw']}{query}",
                "source": "MIT OCW",
                "type": "course",
                "quality": 0.92
            }
        ]
        
        return results[:max_results]
    
    def find_exercises(self, topic: str, difficulty: str = "medium") -> List[Dict]:
        """Find practice exercises"""
        query = urllib.parse.quote(f"{topic} {difficulty} exercises")
        
        return [
            {
                "title": f"{topic} Practice - Khan Academy",
                "url": f"{self.sources['khan']}{query}",
                "difficulty": difficulty,
                "type": "interactive",
                "quality": 0.90
            },
            {
                "title": f"{topic} Problems - Brilliant",
                "url": f"{self.sources['brilliant']}{urllib.parse.quote(topic)}",
                "difficulty": difficulty,
                "type": "problem_set",
                "quality": 0.88
            }
        ]
    
    def find_papers(self, topic: str, max_results: int = 5) -> List[Dict]:
        """Find academic papers"""
        query = urllib.parse.quote(topic)
        
        return [
            {
                "title": f"Papers on {topic}",
                "url": f"{self.sources['arxiv']}{query}",
                "source": "arXiv",
                "type": "academic",
                "quality": 0.85
            }
        ]
    
    def create_resource_note(self, topic: str, resources: List[Dict]) -> str:
        """Generate markdown note with resources"""
        content = f"""# Resources: {topic}

**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}

## Videos

"""
        videos = [r for r in resources if r['type'] in ['video', 'video_series', 'course']]
        for r in videos:
            content += f"- [{r['title']}]({r['url']}) - {r['source']} (Quality: {r['quality']:.0%})\n"
        
        content += "\n## Practice Problems\n\n"
        exercises = [r for r in resources if r['type'] in ['interactive', 'problem_set']]
        for r in exercises:
            content += f"- [{r['title']}]({r['url']}) - Difficulty: {r.get('difficulty', 'N/A')}\n"
        
        content += "\n## Academic Papers\n\n"
        papers = [r for r in resources if r['type'] == 'academic']
        for r in papers:
            content += f"- [{r['title']}]({r['url']})\n"
        
        return content
    
    def discover_all(self, topic: str) -> Dict:
        """Discover all resource types"""
        videos = self.find_videos(topic)
        exercises = self.find_exercises(topic)
        papers = self.find_papers(topic)
        
        all_resources = videos + exercises + papers
        note_content = self.create_resource_note(topic, all_resources)
        
        return {
            "topic": topic,
            "total_found": len(all_resources),
            "videos": len(videos),
            "exercises": len(exercises),
            "papers": len(papers),
            "note_content": note_content
        }

if __name__ == "__main__":
    import sys
    
    rd = ResourceDiscovery()
    
    if len(sys.argv) < 3:
        print("Usage: resource-discovery.py <command> <topic> [args]")
        print("\nCommands:")
        print("  videos <topic> [max]")
        print("  exercises <topic> [difficulty]")
        print("  papers <topic> [max]")
        print("  discover <topic>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    topic = sys.argv[2]
    
    if cmd == "videos":
        max_results = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        results = rd.find_videos(topic, max_results)
        print(json.dumps(results, indent=2))
    
    elif cmd == "exercises":
        difficulty = sys.argv[3] if len(sys.argv) > 3 else "medium"
        results = rd.find_exercises(topic, difficulty)
        print(json.dumps(results, indent=2))
    
    elif cmd == "papers":
        max_results = int(sys.argv[3]) if len(sys.argv) > 3 else 5
        results = rd.find_papers(topic, max_results)
        print(json.dumps(results, indent=2))
    
    elif cmd == "discover":
        result = rd.discover_all(topic)
        print(f"\n✓ Found {result['total_found']} resources for '{topic}'")
        print(f"  Videos: {result['videos']}")
        print(f"  Exercises: {result['exercises']}")
        print(f"  Papers: {result['papers']}")
        print(f"\nNote preview:\n{result['note_content'][:500]}...")
