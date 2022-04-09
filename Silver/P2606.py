import sys


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

    return len(visited)-1
    # return visited


def P2606():
    n = int(input())
    edges = int(input())
    graph = {i: set() for i in range(1, n+1)}

    for _ in range(edges):  # 연결된 컴퓨터 표현
        src, dst = map(int, input().split())
        if src not in graph.keys():
            graph[src] = {dst}
        else:
            graph[src].add(dst)

        if dst not in graph.keys():
            graph[dst] = {src}
        else:
            graph[dst].add(src)

    print(dfs(graph, 1))



if __name__ == '__main__':
    input = sys.stdin.readline
    P2606()