class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        curr = [0, 0, 0]
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            curr = [max(triplet[0], curr[0]), max(triplet[1], curr[1]), max(triplet[2], curr[2])]

            if curr == target:
                return True
        
        return False
                
