# Last updated: 11/15/2025, 9:24:43 PM
class Solution(object):
    def leastInterval(self, tasks, n):
        # get the frequency of each task
        counter = Counter(tasks)
        # create a max heap for the frequencies
        max_heap = [-c for c in counter.values()]
        heapq.heapify(max_heap)

        queue = deque() # to track [(max_freq, time till add to heap)]
        max_freq = 0
        timer = 0
        '''
        - max_heap keeps tracking the frequency of the tasks
        - queue will track the frequency after a task is process, with the waiting time till adding back to heap
        '''
        while max_heap or queue:
            timer += 1

            # if we still have unprocessed tasks, we pop heap and increase the timer
            # if the timer of this task is > 0, we add it to queue
            if max_heap:
                task_freq = 1 + heapq.heappop(max_heap)
                if task_freq:
                    queue.append((task_freq, timer + n)) # timer+n is the total waiting time till adding back to heap
            
            # if we still have queue, we pop queue and push the frequency only back to heap
            if queue and queue[0][1] == timer:
                node = queue.popleft()
                heapq.heappush(max_heap, node[0])
            
        return timer
        
        