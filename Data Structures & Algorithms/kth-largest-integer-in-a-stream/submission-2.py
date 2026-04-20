class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kunle, self.k = nums, k 
        heapq.heapify(self.kunle)
        while len(self.kunle) > self.k:
            heapq.heappop(self.kunle)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.kunle,val)
        while len(self.kunle) > self.k:
            heapq.heappop(self.kunle)

        return self.kunle[0]
        
