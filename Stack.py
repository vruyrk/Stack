class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def push(self,val):
        return self.stack.append(val)
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size() == 0

class BH:
    def __init__(self):
        self.backH = Stack()
        self.fwdH = Stack()
        self.current = ""

    def open(self, url):
        if self.current != "":
            self.backH.push(self.current)
            self.fwdH = Stack()
        self.current = url

    def back(self):
        if self.backH.is_empty():
            print ("No History")
        else:
            self.fwdH.push(self.current)
            self.current = self.backH.pop()

def main():
    bh = BH()
    bh.open("a.b")
    bh.open("c.d")
    bh.open("e.f")
    bh.back()
    print ("Current Page")

main()