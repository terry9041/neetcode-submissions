from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.records = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.records[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        target_arr = self.records[key]
        if target_arr == []:
            return ""
        l, r = 0, len(target_arr)-1
        while l <= r:
            m = l + (r-l)//2
            if target_arr[m][0] == timestamp:
                return target_arr[m][1]
            elif target_arr[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        return target_arr[r][1] if r >= 0 else ""
