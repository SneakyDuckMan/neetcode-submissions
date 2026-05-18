class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permutation(arr):
            
            if len(arr) == 0:
                return [[]]

            perm = []
            split = arr[1:]

            perms = permutation(split)

            for p in perms:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, arr[0])
                    perm.append(copy)
            
            return perm

        return permutation(nums)

    
