import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # BF: calculate all distance, sort then select to return
        # TC: O(nlogn) SC: O(n)

        # Optimized: use a min heap to keep track of distance
        # insert every distance, keep length of k, then pop k items out to return
        # TC: O(nlogk) each insert, pop is log k -> nlogk
        # SC: O(k) for the heap
        # caveat: store (-dist, coordinate) in heap as default is min-heap not max-heap
    
        heap = []

        def get_dist(pt):
            x,y = pt[0],pt[1]
            return math.sqrt(x*x + y*y)

        for i in range(len(points)):
            heapq.heappush(heap, (-get_dist(points[i]), points[i]))
            if i >= k:
                heapq.heappop(heap)
        print(heap)
        return [pt for _,pt in heap]
            
        
