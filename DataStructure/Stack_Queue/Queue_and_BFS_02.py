# <Open the Lock>

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # bfs
        level = 0  
        visited = set()
        queue = collections.deque()
        queue.appendleft("0000")
        visited.add("0000")
        
        while queue : # not empty
            size = len(queue)
            for i in range(size):
                front = queue.pop()
                if front == target: 
                    return level
                if front in deadends:
                    continue
                for i in range(4): # add paths(childs)
                    to1 = front[:i] + str((int(front[i])+1)%10) + front[i+1:]
                    to2 = front[:i] + str((int(front[i])-1)%10) + front[i+1:]
                    if to1 not in visited:
                        queue.appendleft(to1)
                        visited.add(to1)
                    if to2 not in visited:
                        queue.appendleft(to2)
                        visited.add(to2)
            level += 1        
        return -1