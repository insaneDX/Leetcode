class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # build heap
        heap = [-x for x in freq.values()]
        heapq.heapify(heap)

        time = 0
        cooldown = deque() # available_time, count  
        while heap or cooldown:
            time += 1

            # if task is ready from cooldown? then push it to heap
            if cooldown and cooldown[0][0] <= time:
                heapq.heappush(heap, cooldown.popleft()[1])
            
            # remove top frequent task and execute it
            if heap:
                task_count = heapq.heappop(heap) + 1
            
                # if after execution still has some more tasks left put it in cooldown
                if task_count != 0:
                    cooldown.append((time+n+1, task_count))

        return time