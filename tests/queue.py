from collections import deque

queue = deque([10, 20, 30, 40, 50])
stack = []
print(f"Queue: {queue}")
 # Step 1: Remove each item from the front of the queue
# and push it onto the stack.
while queue: 
    stack.append(queue.popleft())
# Step 2: Pop each item from the stack
print(f"Stack: {stack}")
for i in range(len(stack)):
    queue.append(stack.pop())
# and add it to the rear of the queue.

# 3 Output:
print(f"Stack: {stack}")
print(f"Reversed Queue: {queue}")   