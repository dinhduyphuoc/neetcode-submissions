class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ""
        val = self.store[key]
        l, r = 0, len(val) - 1
        res = ""

        while l <= r:
            pivot = (l + r) // 2
            if val[pivot][1] <= timestamp:
                res = val[pivot][0]
                l = pivot + 1
            else:
                r = pivot - 1
        
        return res
                