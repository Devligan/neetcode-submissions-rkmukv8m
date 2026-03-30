class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges) == 0):
            return True
        graph = {i: [] for i in range(n)}
        count = 0
        for a, b in edges:
            if(len(graph[a]) == 0):
                count += 1
            if(len(graph[b]) == 0):
                count += 1
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        if(not self.dfs(0, graph, visited)):
            return False
        return len(visited) == count
    def dfs(self, node, graph, visited):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr in visited:
                return False
            else:
                visited.add(curr)
                for nei in graph[curr]:
                    if nei not in visited:
                        stack.append(nei)
        return True
        
