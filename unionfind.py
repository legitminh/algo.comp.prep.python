class UnionFind:
    def __init__(self, size):
        # initially, every element is its own parent (root)
        self.parent = list(range(size))
        # rank is used to keep the tree flat during unions
        self.rank = [1] * size

    def find(self, i):
        # path compression optimization
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # union by rank optimization
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True  # a merge successfully occurred
        return False  # they were already in the same set
