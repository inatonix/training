class Graph:
    def __init__(self, nodes):
        self.Nodes = nodes

class Node:
    def __init__(self, label, to=None):
        self.Label = label
        self.To = to
        self.Visited = False

class Queue:
    def __init__(self, data):
        self.data = data
    def pop(self):
        if len(self.data) == 0:
            print("The Queue is Empty!")
        else:
            return self.data.pop(0)
    def push(self, d):
        self.data.append(d)
    def isEmpty(self):
        return len(self.data) == 0

def bfs(g, st, dst):
    q = Queue([])

    visited = [False] * (len(g.Nodes)+1)

    for node in g.Nodes:
        if node.Label != st:
            continue
        if node.To is not None:
            for next_node in node.To:
                q.push(next_node)
                visited[node.Label] = True

    #visit
    while not q.isEmpty():
        n = q.pop()
        visited[n.Label] = True
        if n.Label == dst:
            return True
        if n.To is not None:
            for k in n.To:
                if not visited[k.Label]:
                    q.push(k)
        print(visited)
    return False    


if __name__ == '__main__':
    n3 = Node(3)
    n5 = Node(5)

    n4 = Node(4, [n3])
    n2 = Node(2, [n4,n5])
    n1 = Node(1, [n2,n3])

    g = Graph([n1,n2,n3,n4,n5])
    print(bfs(g, 1, 5))

