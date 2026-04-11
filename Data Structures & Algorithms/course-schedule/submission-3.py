class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        path = set()
        visited = set()

        def dfs(crs):
            if crs in path:
                return False
            if crs in visited:
                return True
            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visited.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
