class UnionFind:
    def __init__(self, size):
        # Initially, every element is its own parent (root)
        self.parent = list(range(size))
        # Rank is used to keep the tree flat during unions
        self.rank = [1] * size

    def find(self, i):
        # Path compression optimization
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Union by rank optimization
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True  # A merge successfully occurred
        return False  # They were already in the same set
