import argparse
import csv
from collections import Counter

def create_zero_matrix(count_edges):
    ans = []
    for i in range (0, count_edges+1):
        tmp = []
        for j in range(1, 5+1):
            tmp.append(0)
        ans.append(tmp)
    return ans

def create_graph(edges):
    graph = {}
    for u, v in edges:
        if (u-1) not in graph:
            graph[u-1] = []
        graph[u-1].append(v-1)
    return graph

def find_subnodes_with_levels(graph, start_node):
    def dfs(node, level, visited):
        visited[node] = level
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, level + 1, visited)

    visited = {}
    dfs(start_node, 0, visited)
    
    visited.pop(start_node, None)

    return visited

def task(edges):
    count_edges = len(edges)

    ans = create_zero_matrix(count_edges)
    graph = create_graph(edges)

    for i in graph:
        for j in graph[i]:
            ans[j][4] = len(graph[i]) - 1

    for i in range(0, count_edges+1):
        # print(i)
        subnodes = find_subnodes_with_levels(graph, i)

        for j in subnodes:
            if subnodes[j] == 1:
                ans[j][1] += 1 
            else:
                ans[j][3] += 1

        subnodes_counter = Counter(find_subnodes_with_levels(graph, i).values())
        # print(subnodes)
        ans[i][0] = subnodes_counter[1]
        ans[i][2] = sum(value for key, value in subnodes_counter.items() if key >= 2)
    csv_str = "\n".join([",".join(map(str, row)) for row in ans])
    print(csv_str)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    with open(args.filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        edges = [tuple(int(value) for value in row) for row in reader]

    task(edges)

if __name__ == '__main__':
    main()