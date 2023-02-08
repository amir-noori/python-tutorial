

class Element:

    def __init__(self, value, index=0, next=None):
        self.value = value
        self.index = index
        self.next = next


class Stack:

    def __init__(self):
        self.first = None
        self.last = None

    def push(self, value):
        element = Element(value)
        if self.first == None:
            self.first = element
            self.last = element
        else:
            element.index += 1
            self.last.next = element
            self.last = element
    
    def pop(self):
        element = self.last
        current_element = self.first
        for i in range(0, self.last.index):
            current_element = current_element.next
            if i == self.last.index - 1:
                current_element.next = None
                self.last = current_element
        return element
    
    def get(self, i):
        pass

    def __str__(self):
        result = ""
        element = self.first
        while element != None:
            result += str(element.value) + " "
            element = element.next
        return result





