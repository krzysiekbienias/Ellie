import heapq as h
from typing import List

class Heap:

    @staticmethod
    def lastStoneWeight(stones: List[int]) -> int:
        """lastStoneWeight
        Description
        -----------
        This function returns weight of the last remaining stone. Each turn two heaviest stones are smashed. The results of smashing might be one one of the following:
        1) both stones are destroyed if x=y
        2) heavier stone weight is replaced by y-x.

        Parameters
        ----------
        stones : List[int]
            weight of stones

        Returns
        -------
        int
            _description_

        Example
        -------
        >>>  lastStoneWeight(self, stones=[2,7,4,1,8,1])=1
        We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
        we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
        we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
        we combine 1 and 1 to get 0 so the array converts to [1] then that is the value of the last stone. 
        """
        if len(stones)==2:
            if stones[0]==stones[1]:
                return 0
            else:
                return stones[1]-stones[0] if stones[1]>stones[0] else -stones[1]+stones[0]  
        scaledStones=[e*-1 for e in stones]
        h.heapify(scaledStones)
        while len(scaledStones)>1:
            stone1=h.heappop(scaledStones)
            stone2=h.heappop(scaledStones)
            if stone1!=stone2:
                h.heappush(scaledStones,stone1-stone2)
        if scaledStones:
            return -h.heappop(scaledStones)
        else:
            return 0