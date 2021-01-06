"""
Write a Python program to implement
queue using a list data-structure.
"""


class Queue:
    def __init__(self):
        self.parts = []

    def dequeue(self):
        return self.parts.pop(0)

    def enqueue(self, data):
        self.parts.append(data)

    def peekall(self):
        return self.parts

    def peek(self):
        return self.parts[-1]

    def empty_queue(self):
        return self.parts == []


qe = Queue()
while True:
    print("What would you like to do?\n1. Enqueue <Value>\n2. Dequeue\n3. Peek\n4. PeekAll\n5. Exit\n")
    option = str(input())
    do = option.split()[0].lower()

    if do == "1" or do == "enqueue":
        qe.enqueue(option.split()[1:])

    elif do == "2" or do == "dequeue":
        if qe.empty_queue():
            print('Nothing is in Queue!\nAdd Something First to Remove it.')
        else:
            print(qe.dequeue())

    elif do == "3" or do == "peek":
        if qe.empty_queue():
            print('Nothing is in Queue!\nAdd Something First to See it.')
        else:
            print(qe.peek())
    elif do == "4" or do == "peekall":
        if qe.empty_queue():
            print('Nothing is in Queue!\nAdd Something First to See it.')
        else:
            print(qe.peekall())
    elif do == "5" or do == "exit":
        break

    else:
        tmp = str(input("No Valid Input! Do you want to continue? [Y/N]: "))
        if tmp.lower() != 'y':
            break
