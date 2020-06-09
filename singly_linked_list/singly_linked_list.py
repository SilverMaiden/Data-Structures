
class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None
        self.tailval = None

    def listprint(self):
        print(self.headval.dataval)
        printval = self.headval.nextval
        while printval is not self.tailval:
            print(printval.dataval)
            printval = printval.nextval
        print(printval.dataval)
        return

    def insert(self, value):
        if not isinstance(value, Node):
            nodetoadd = Node(value)
        else:
            nodetoadd = value
        if self.headval is None:
            self.headval = nodetoadd
        else:
            self.tailval.nextval = nodetoadd
        self.tailval = nodetoadd

    def insertBetween(self, prevnode, value):
        printval = self.headval
        while printval is not prevnode:
            printval = printval.nextval
        ahead = printval.nextval
        printval.nextval = Node(value)
        printval = printval.nextval
        printval.nextval = ahead

    def insertAtStart(self, value):
        nodetoadd = Node(value)
        nodetoadd.nextval = self.headval
        self.headval = nodetoadd








myList = LinkedList()

node1 = Node("Apple")
node2 = Node("Banana")
node3 = Node("Carrot")
node4 = Node("Durian")


myList.insert(node1)
myList.insert(node2)
myList.insert(node3)
myList.insert(node4)


print("\n")
myList.listprint()

myList.insert("Eggplant")

print("\n")
myList.listprint()

myList.insertBetween(node4, "Bat")

print("\n")
myList.listprint()

myList.insertAtStart("Squash")

print("\n")
myList.listprint()

