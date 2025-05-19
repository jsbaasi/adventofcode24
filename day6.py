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

        dirToArrow = {
            (0, 1): ">",
            (0, -1): "<",
            (1, 0): "v",
            (-1, 0): "^",
        }

        res = 0

        def checkCell(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False
            return True

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "^":
                    # s = grid[row][:col] + "." + grid[row][col + 1 :]
                    # grid[row] = s
                    r, c = row, col
        dir = (-1, 0)

        f = open("Day6Debug.txt", "a")
        while checkCell(r, c):
            if grid[r][c] == "#":
                alteration = alter[dir]
                dir = turn[dir]
                r, c = r + alteration[0], c + alteration[1]
            else:
                turnRightDir = turn[dir]
                turnRightTuple = (r + turnRightDir[0], c + turnRightDir[1])
                if (
                    grid[turnRightTuple[0]][turnRightTuple[1]]
                    == dirToArrow[turnRightDir]
                ):
                    res += 1

                if grid[r][c] == ".":
                    s = grid[r][:c] + dirToArrow[dir] + grid[r][c + 1 :]
                    grid[r] = s
                else:
                    s = grid[r][:c] + dirToArrow[dir] + grid[r][c + 1 :]
                    grid[r] = s

                r, c = r + dir[0], c + dir[1]

            gridcopy = "\n".join(grid)
            f.write(gridcopy + "\n" + str(res) + "\n\n")
        return res


grid = []
with open("day6TestInput.txt") as f:
    for line in f:
        grid.append(line.rstrip())

obj = Solution()
# print(obj.part1(grid.copy()))  # 0.01 seconds
t1 = time.time()
print(obj.part2(grid.copy()))
t2 = time.time()
print(t2 - t1)
