# 인접 리스트를 이용하여 구현
import sys
from collections import deque


def dfs(graph, start_node):         # stack
    visited = list()
    stack = list()

    stack.append(start_node)        # insert the start-node

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                stack.extend(sorted(graph[node], reverse=True))
            # stack.extend(sorted(graph[node], reverse=True))

    return visited


def bfs(graph, start_node):
    visited = list()
    queue = deque()

    queue.append(start_node)        # start
    while queue:
        node = queue.popleft()      # instead of 'node = queue.pop(0)'
        if node not in visited:
            visited.append(node)
            if node in graph:
                queue.extend(sorted(graph[node]))
            # queue.extend(sorted(graph[node]))
    return visited


def P1260():
    node, edge, start = map(int, input().split())
    # g = Graph(node)
    # g = {i: None for i in range(1, node+1)}

    graph = {}
    for _ in range(edge):
        src, dst = map(int, input().split())
        # g.make_nodes(src, dst)
        if src not in graph.keys():
            graph[src] = {dst}
        else:
            graph[src].add(dst)

        if dst not in graph.keys():
            graph[dst] = {src}
        else:
            graph[dst].add(src)

    # print(' '.join(map(str, dfs(graph, start))))
    print(*dfs(graph, start), sep=' ')
    # print(' '.join(map(str, bfs(graph, start))))
    print(*bfs(graph, start), sep=' ')


if __name__ == '__main__':
    input = sys.stdin.readline
    P1260()

# class Graph:
#     def __init__(self, node):
#         self.adj_list = [[] for _ in range(node + 1)]
#
#     def make_nodes(self, src, dst):
#         self.adj_list[src].append(dst)
#         self.adj_list[dst].append(src)
#
#     # def get_graph(self):
#     #     return self.adj_list
