N = int(input())


# Node 구현 클래스
class ListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


# LinkedList 구현 클래스
class LinkedList:
    def __init__(self):
        self.head = None
        self.current = self.head

    # < 입력
    def left(self):
        if self.current.prev:
            self.current = self.current.prev
        return self.current

    # > 입력
    def right(self):
        if self.current.next:
            self.current = self.current.next
        return self.current

    # - 입력
    def deleteNode(self):
        if self.current:
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
        return self.current

    # 일반 알파벳 입력
    def addNode(self, node):
        if not self.current:  # 최초 연결리스트일 때
            self.head = node
            self.current = node
        else:
            node.next = self.current.next
            self.current.next = node
            self.current = node

    def result(self):
        result = []
        while self.current.next:
            result.append(self.current.value)
            self.current = self.current.next
        result.append(self.current.value)
        return result


# keyLogger 구현 함수
def keyLogger(input):
    linkedList = LinkedList()

    for i in range(len(input)):
        if input[i] == "<":
            linkedList.left()
        elif input[i] == ">":
            linkedList.right()
        elif input[i] == "-":
            linkedList.deleteNode()
        else:
            node = ListNode(value=input[i])
            linkedList.addNode(node)
    return linkedList.result()


for _ in range(N):
    str = input()
    print(keyLogger(str))
