from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True
        graph ={i:[] for i in range(numCourses)}
        in_degree=[0]*numCourses
        course_count=0
        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1
        q=deque()

        for i in range(numCourses):
            if in_degree[i]==0:
                q.append(i)
        while q:
            temp = q.popleft()
            course_count+=1
            for nei in graph[temp]:
                in_degree[nei]= in_degree[nei]-1
                if in_degree[nei]==0:
                    q.append(nei)
        return course_count==numCourses

        