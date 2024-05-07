import heapq

def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def g_c_backt(graph, color_set):
    color = [None]*len(graph)
    g_c_util_backt(graph, color_set, color, 0)
    for i, c in enumerate(color):
        print("vertex : ", i, " color : ", c)

def g_c_util_backt(graph, color_set, color, v):
    if v == len(graph):
        return True
    for c in color_set:
        if is_safe(graph, color, v, c):
            color[v] = c
            if g_c_util_backt(graph, color_set, color, v+1):
                return True
            color[v] = None

def g_c_bnb(graph, color_set):
    def bound(v):
        max_used_color = max(color[:v]) if v>0 else 0
        return max_used_color
    def g_c():
        pq = [(0,[-1]*len(graph))]
        while pq:
            used_colors, coloring = heapq.heappop(pq)
            v = coloring.index(-1) if -1 in coloring else len(graph)
            if v == len(graph):
                return coloring
            for c in color_set:
                if is_safe(graph, coloring, v, c):
                    new_coloring = list(coloring)
                    new_coloring[v] = c
                    heapq.heappush(pq, (used_colors+1, new_coloring))
    coloring = g_c()
    for i, c in enumerate(coloring):
        print("Vertex : ", i, " color : ", c )

def main():
    vertices = int(input("Enter no of vertices : "))
    graph = []
    print("Enter adjacency matrix : ")
    for _ in range(vertices):
        row = [int(x) for x in input().split()]
        graph.append(row)

    print("Backtracking")
    color_set = input("Enter colours separated by space : ").split()
    g_c_backt(graph, color_set)
    print("Branch and Bound")
    color_set = input("Enter colours separated by space : ").split()
    g_c_bnb(graph, color_set)

main()