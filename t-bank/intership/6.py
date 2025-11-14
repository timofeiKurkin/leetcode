relatives: list[list[int]] = []

# the number of vertices and edges in the graph
# 2 <= n <= 10^5 and 1 <= m <= 2 * 10^5
n, m = map(int, input().split())

if m % 2 != 2:
    print(-1)

edges: list[list[int]] = []
adj = [[] for _ in range(n + 1)]

for i in range(m):
    # 1 <= v,u <= n, u != v
    v, u = map(int, input().split())
    edges.append((u, v))
    adj[u].append((v, i))
    adj[v].append((u, i))

visited = [False] * (n + 1)
depth = [0] * (n + 1)
used_edge = [False] * m
out_parity = [0] * (
    n + 1
)  # 0 — чётная исходящая степень по текущей ориентации, 1 — нечётная
orient = [None] * m  # (u, v) означает направление u -> v
ok = True


def dfs(v):
    visited[v] = True
    for to, eid in adj[v]:
        if used_edge[eid]:
            continue
        used_edge[eid] = True
        if not visited[to]:
            depth[to] = depth[v] + 1
            dfs(to)
            # После обработки ребёнка to решаем направление дерева
            if out_parity[to] == 1:
                # Нужен исходящий из to, чтобы сделать его чётным
                orient[eid] = (to, v)
                out_parity[to] ^= 1
            else:
                orient[eid] = (v, to)
                out_parity[v] ^= 1
        else:
            if depth[to] < depth[v]:
                orient[eid] = (v, to)
                out_parity[v] ^= 1


# Обрабатываем все компоненты
for v in range(1, n + 1):
    if not visited[v]:
        before_edges = sum(
            1 for to, eid in adj[v]
        )  # не нужно; проверим по чётности корня после DFS
        dfs(v)
        if out_parity[v] != 0:
            ok = False
            break
if not ok:
    print(-1)
