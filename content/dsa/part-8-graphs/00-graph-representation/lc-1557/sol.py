# LC 1557. Minimum Number of Vertices to Reach All Nodes
# In a DAG, a vertex is unreachable from any other vertex iff its in-degree
# is zero. The answer is the set of in-degree-zero vertices. No adjacency
# list is needed; an int[] of size n is sufficient. O(V + E) time, O(V) space.
from typing import List


def find_smallest_set_of_vertices(n: int, edges: List[List[int]]) -> List[int]:
    in_degree = [0] * n
    for _, v in edges:                         # only the destination matters
        in_degree[v] += 1
    return [u for u in range(n) if in_degree[u] == 0]
