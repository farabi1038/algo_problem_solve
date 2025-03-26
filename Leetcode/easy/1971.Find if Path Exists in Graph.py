from collections import deque, defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q= deque()
        visited = set()
        q.append(source)
        while q:
            temp_node =q.popleft()
            if temp_node in visited:
                continue
            else:
                visited.add(temp_node)
            if temp_node == destination:
                return True    
            for n in graph[temp_node]:
                if n not in visited:
                    q.append(n)
        return False            
                           
        
