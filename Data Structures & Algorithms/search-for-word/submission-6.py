class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(coord, depth) -> bool:
            x, y = coord
            if word[depth] != board[x][y] or depth == len(word):
                return False
            elif word[depth] == board[x][y] and depth == len(word) - 1:
                return True
            visited.add((x, y))
            neighbours = [
                (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)
            ]
            for n in neighbours:
                xn, yn = n
                if xn >= 0 and xn < len(board)\
                    and yn >= 0 and yn < len(board[0]):
                    if n not in visited:
                        found = dfs(n, depth + 1)
                        if found: 
                            return True
            visited.remove((x, y))
            return False

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                # found initial
                if board[i][j] == word[0]:
                    # start dfs, only expand to depth = len(word)
                    found = dfs((i, j), 0)
                    if found: return True

        return False