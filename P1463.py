# 6이하 일때 생각해봐야함
# 가장 가까운 3의 제곱, 2의 제곱수로 이동하기
# 인수분해 트리 만들기

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # 3 나누기
        self.center = None  # 2 나누기
        self.right = None  # 1 빼기

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def makeRoot(self, node, left_node, center_node, right_node):
        if self.root is None:
            self.root = node
        node.left = left_node
        node.center = center_node
        node.right = right_node

    def getHeight(self, root):
        if root is None:
            return -1
        left_height = self.getHeight(root.left) + 1
        center_height = self.getHeight(root.center) + 1
        right_height = self.getHeight(root.right) + 1

        return max(left_height, center_height, right_height)

    def find1(self):





def P1463():
    num = int(input())


if __name__ == '__main__':
    P1463()
