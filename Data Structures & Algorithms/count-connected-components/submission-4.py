class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n
        res = n
        
        def find(n):
            if parents[n] != n:
                parents[n] = find(parents[n])
            return parents[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False  
                 
            if rank[p1] < rank[p2]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]

            return True

        for edge in edges:
            if union(edge[0], edge[1]):
                res -= 1
        return res
                
            
            

        