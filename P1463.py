# 6이하 일때 생각해봐야함
# 가장 가까운 3의 제곱, 2의 제곱수로 가야함

# def P1463():
#     num = int(input())
#
#     count = 0
#     if num > 2:
#         while num % 3 != 0:
#             num -= 1
#             count += 1
#     elif num == 2:
#         print(1)
#         exit(0)
#     else:
#         print(0)
#         exit(0)
#
#     print(count+num//3-1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.center = None
        self.right = None

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


def P1463():
    num = int(input())


if __name__ == '__main__':
    P1463()
