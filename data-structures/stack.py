class Stack:


    def __init__(self):
        self.silo = []


    def isEmpty(self):
        return self.silo == []


    def push(self, item):
        self.silo.append(item)


    def pop(self):
        return self.silo.pop()


    def peek(self):
        return self.silo[-1]


    def size(self):
        return len(self.silo)



if __name__ == '__main__':

    # Some simple tests
    s = Stack()
    assert s.isEmpty()
    assert s.size() == 0

    s.push(4)
    assert s.peek() == 4
    assert s.size() == 1

    s.push(8.4)
    assert s.size() == 2

    s.pop()
    assert s.peek() == 4
    assert s.pop() == 4

    assert s.size() == 0
    assert s.isEmpty()
