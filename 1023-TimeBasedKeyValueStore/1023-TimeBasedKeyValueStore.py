# Last updated: 6/17/2025, 10:34:28 PM
class TimeMap(object):

    def __init__(self):
        self.timeMap = {}

    def set(self, key, value, timestamp):
        if key in self.timeMap:
            self.timeMap[key].append((timestamp, value))
        else:
            self.timeMap[key] = [(timestamp, value)]

    def get(self, key, timestamp):
        res = ""
        d = self.timeMap.get(key)
        if d:
            left = 0
            right = len(d)-1
            while left <= right:
                mid = (left+right)//2
                if d[mid][0] == timestamp:
                    return d[mid][1]
                if d[mid][0] < timestamp:
                    res = d[mid][1]
                    left = mid+1
                if d[mid][0] > timestamp:
                    right = mid-1
        return res
         
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)