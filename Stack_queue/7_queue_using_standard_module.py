########### Collection Module ##################
from collections import deque

queue = deque(maxlen=3)
print(queue)


queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.append(4)
print(queue)

queue.popleft()
print(queue)

queue.clear()
print(queue)
