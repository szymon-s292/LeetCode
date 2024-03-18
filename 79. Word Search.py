class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r >= rows or r < 0 or c >= cols or c < 0 or (r, c) in path or board[r][c] != word[i]:
                return False

            path.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or \
            dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True

        return False
