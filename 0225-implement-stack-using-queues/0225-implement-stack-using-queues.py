from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque() 

    def push(self, x: int) -> None:
        # Add new element
        self.q.append(x)
        
        # Rotate queue so new element is at front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()  #  Remove front element

    def top(self) -> int:
        return self.q[0]  #  Peek front

    def empty(self) -> bool:
        return len(self.q) == 0  # Check if empty


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()