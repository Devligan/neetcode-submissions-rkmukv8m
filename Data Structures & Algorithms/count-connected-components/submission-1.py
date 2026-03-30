class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                self.dfs(node, graph, visited)
        return components

    def dfs(self, node, graph, visited):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for nei in graph[curr]:
                    if nei not in visited:
                        stack.append(nei)
