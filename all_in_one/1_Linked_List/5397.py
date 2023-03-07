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
        self.current = None

    # < 입력
    def left(self):
        if self.current and self.current.prev:
            self.current = self.current.prev

    # > 입력
    def right(self):
        if self.current and self.current.next:
            self.current = self.current.next

    # - 입력
    def deleteNode(self):
        if self.current:
            if not self.current.next:  # 1,3
                if self.current.prev:  # 3
                    self.current = self.current.prev
                    self.current.next = None
                else:  # 1
                    self.current = None
            else:  # 2,4
                if self.current.prev:  # 4
                    self.current.prev.next = self.current.next
                    self.current.next.prev = self.current.prev
                    self.current = self.current.prev
                else:  # 2
                    self.head = self.current.next
                    self.current = self.head

    # 일반 알파벳 입력
    def addNode(self, node):
        if not self.current:  # 최초 연결리스트일 때
            self.head = node
            self.current = node
        else:
            if self.current.next:  # 전,후 노드가 모두 존재하는 경우
                node.next = self.current.next
                node.prev = self.current
                self.current.next, node.prev.prev = node, node
                self.current = node
            else:
                # 전 노드만 존재하는 경우 (맨 마지막 노드)
                self.current.next = node
                node.prev = self.current
                self.current = node

    def result(self):
        result = []
        if self.head:
            node = self.head
            while node.next:
                result.append(node.value)
                node = node.next
            result.append(node.value)
            return "".join(result)
        else:
            return ""


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


# 풀이 출력부
answer = []
for _ in range(N):
    str = input()
    answer.append(keyLogger(str))
for ans in answer:
    print(ans)
