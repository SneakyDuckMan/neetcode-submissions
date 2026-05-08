class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0]*len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] < temperatures[i+1]:
                result[i] = 1
            
            else:
                j = i + 1

                while j < len(temperatures) and temperatures[i] >= temperatures[j]:
                    
                    if result[j] == 0:
                        break
                    j += result[j]

                if result[j] == 0 and temperatures[i] >= temperatures[j]:
                    continue
                
                result[i] = j - i
        
        return result
                