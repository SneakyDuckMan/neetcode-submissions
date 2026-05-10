class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append([timestamp, value])
        
        else:
            self.hashmap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hashmap:
            return ""

        arr = self.hashmap[key]

        if len(arr) == 0:
            return ""

        l, r = 0, len(arr) - 1

        while l <= r:

            mid = (l + r)//2
            
            if arr[mid][0] == timestamp:
                return arr[mid][1]

            if arr[mid][0] < timestamp:
                l = mid + 1
            
            else:
                r = mid - 1
        
        if arr[r][0] < timestamp:
            return arr[r][1]
        
        else:
            return ""
        
