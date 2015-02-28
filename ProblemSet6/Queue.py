__author__ = 'vnellore'

class Queue(object):

    def __init__(self):
        self.contents = []

    def insert(self, a):
        self.contents.append(a)

    def remove(self):

        if len(self.contents) == 0:
            raise ValueError("Queue is empty")
        else:
            return self.contents.pop(0)

    def __str__(self):
        return '{' + ','.join([str(e) for e in self.contents]) + '}'


q = Queue()
q.insert(5)
print q

q.insert(6)
print q

q.insert(7)
print q

print q.remove()
print q.remove()
print q.remove()
