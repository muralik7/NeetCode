import heapq

class Solution:
    def carPoolingTripsKnown(self, trips: list[list[int]], capacity: int) -> bool:
        # Complexity O(n) - As number of trips is <= 1000
        numPass = [0] * 1001

        for t in trips:
            passengers, start, end = t
            numPass[start] += passengers
            numPass[end] -= passengers

        currPass = 0
        for i in range(len(numPass)):
            currPass += numPass[i]
            if currPass > capacity:
                return False
        
        return True
    
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # Complexity O(nlogn)
        trips.sort(key = lambda t: t[1])
        
        minHeap = [] # pair of [end, numPass]
        currPass = 0

        for t in trips:
            numPass, start, end = t
            while minHeap and minHeap[0][0] <= start:
                currPass -= minHeap[0][1]
                heapq.heappop(minHeap)

            currPass += numPass
            if currPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
                 
        return True
    
if __name__ == "__main__":
    s = Solution()

    print("Car pooilng possible: ", s.carPoolingTripsKnown([[2, 1, 5], [3, 1, 7]], 4))
    print("Car pooilng possible: ", s.carPoolingTripsKnown([[2, 1, 5], [3, 3, 7]], 5))

    print("Car pooilng possible: ", s.carPooling([[2, 1, 5], [3, 1, 7]], 4))
    print("Car pooilng possible: ", s.carPooling([[2, 1, 5], [3, 3, 7]], 5))
