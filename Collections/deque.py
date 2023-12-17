"""deque | Queue"""
from collections import deque

people = ["mario", "luigi", "Toad"]
queue = deque(people)

queue.append("Bowser")
print(queue, queue[1])

print("pop: ", queue.popleft())
print(queue)

queue.appendleft("Daisy")
print(queue)

queue.rotate(-1)  # every index = index -1
print(queue)

queue.extend(["Shy Guy", "Yoshi"])
print(queue)

queue.reverse()
print(queue)
