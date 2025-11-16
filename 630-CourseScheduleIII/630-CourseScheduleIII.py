# Last updated: 11/15/2025, 11:43:59 PM
class Solution(object):
    def scheduleCourse(self, courses):
        courses.sort(key = lambda x : x[1]) # sort by lastDay, cause we want to take lesser deadline ones first
        max_heap = []
        days = 0

        for duration,deadline in courses:
            # add the duration to max_heap, will keep the longest duration on top
            heapq.heappush(max_heap, -duration)

            days += duration

            # when days > deadline, we need to remove the longest durated course, to have more space for shorter dura
            if days > deadline:
                longest_course = -heapq.heappop(max_heap)
                days -= longest_course
        
        return len(max_heap)
        

        