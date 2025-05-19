# importing the sys module
import sys
import time

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
sys.setrecursionlimit(10**8)


class Solution:
    def part1(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        alter: dict[tuple] = {
            (-1, 0): (1, 1),
            (0, 1): (1, -1),
            (1, 0): (-1, -1),
            (0, -1): (-1, 1),
        }
        turn: dict[tuple] = {
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
        }
        res = 0

        def checkCell(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False
            return True

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "^":
                    s = grid[row][:col] + "." + grid[row][col + 1 :]
                    grid[row] = s
                    r, c = row, col
        dir = (-1, 0)
        while checkCell(r, c):
            if grid[r][c] == "." or grid[r][c] == ",":
                if grid[r][c] == ".":
                    res += 1
                    s = grid[r][:c] + "," + grid[r][c + 1 :]
                    grid[r] = s
                r, c = r + dir[0], c + dir[1]
            elif grid[r][c] == "#":
                alteration = alter[dir]
                dir = turn[dir]
                r, c = r + alteration[0], c + alteration[1]
        return res

    def part2(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        dirs = {
            "v": (1, 0),
            "^": (-1, 0),
            ">": (0, 1),
            "<": (0, -1),
        }
        alter: dict[tuple] = {
            (-1, 0): (1, 1),
            (0, 1): (1, -1),
            (1, 0): (-1, -1),
            (0, -1): (-1, 1),
        }
        turn: dict[tuple] = {
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
        }

        upSet = set()
        downSet = set()
        rightSet = set()
        leftSet = set()

        dictOfSets = {
            (1, 0): downSet,
            (-1, 0): upSet,
            (0, 1): rightSet,
            (0, -1): leftSet,
        }
        res = 0

        def dfs(r, c, dir: tuple):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if grid[r][c] == ".":
                s = grid[r][:c] + "," + grid[r][c + 1 :]
                grid[r] = s
                dictOfSets[dir].add((r, c))
            turnDir = turn[dir]
            if (0 <= r + turnDir[0] < ROWS) and (0 <= c + turnDir[1] < COLS):
                toMyRight = (r + turnDir[0], c + turnDir[1])
                toMyRightGrid = grid[r + turnDir[0]][c + turnDir[1]]
                if toMyRightGrid == ",":
                    if toMyRight in dictOfSets[turnDir]:
                        nonlocal res
                        res += 1
            if (0 <= r + dir[0] < ROWS) and (0 <= c + dir[1] < COLS):
                if grid[r + dir[0]][c + dir[1]] == "#":
                    dfs(
                        r + turnDir[0],
                        c + turnDir[1],
                        turnDir,
                    )
            dfs(
                r + dir[0],
                c + dir[1],
                dir,
            )

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in dirs:
                    dir = dirs[grid[r][c]]
                    s = grid[r][:c] + "," + grid[r][c + 1 :]
                    grid[r] = s
                    upSet.add((r, c))
                    dfs(r, c, dir)
                    return res


grid = []
with open("day6RawInput.txt") as f:
    for line in f:
        grid.append(line.rstrip())

obj = Solution()
t1 = time.time()
print(obj.part1(grid.copy()))  # 0.01 seconds
t2 = time.time()
print(t2 - t1)
# print(obj.part2(grid))
