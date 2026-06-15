class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)
        
        visited = [False] * n
        count = 0

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for node in range(n):
            if not visited[node]:
                dfs(node)
                count += 1
        
        return count
