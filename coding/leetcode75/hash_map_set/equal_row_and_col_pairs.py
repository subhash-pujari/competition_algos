from typing import List
from collections import Counter


class Solution:
    """
    @author: Subhash
    """

    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = grid

        rows = dict(Counter([tuple(row) for row in rows]))

        cols = [tuple([row[index] for row in grid]) for index in range(len(grid))]

        cols = dict(Counter([tuple(col) for col in cols]))

        count = 0

        # for row in rows:
        for col in cols:
            if col in rows:
                count += cols[col] * rows[col]

        return count


class Solution1:
    """
    @author: best solution from leetcode
    """

    def equalPairs(self, grid: List[List[int]]) -> int:
        tpse = Counter(zip(*grid))
        grid = Counter(map(tuple, grid))
        return sum(grid[t] * tpse[t] for t in tpse)


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

print(Solution().equalPairs(grid))

grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

print(Solution().equalPairs(grid))

print(Solution1().equalPairs(grid))
