import os
import random
import time


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def inputIntInRange(text, x, y, default=None):
    while 1:
        try:
            string = input(text)
            if string == "" and default:
                return default
            num = int(string)
            if not x <= num <= y:
                raise Exception(f"{num} not between {x} and {y}")
        except Exception as e:
            print(e)
        else:
            return num


class TicTac:
    "X = 1, O = 2, X goes first"

    def __init__(self, grid=3, aiEnabled=True, board=None):
        self.grid = grid
        self.squares = grid ** 2
        self.board = board or [0] * self.squares
        self.winner = 0
        self.xIsActive = True
        self.aiEnabled = aiEnabled
        self.aiPlayerId = random.randint(1, 2)
        self.turn = 1
        self.lastMove = ""
        self.combos = TicTac.findCombos(grid)

    def printBoard(self):
        clearScreen()
        # print(self.combos)
        print(f"Tic-Tac-Toe {self.grid}x{self.grid}")
        aiText = "X" if self.aiPlayerId == 1 else "O"
        print(f"AI{' is ' + aiText if self.aiEnabled else ': off'}")

        for i, v in enumerate(self.board):
            filler = " "
            if v == 1:
                filler = "X"
            elif v == 2:
                filler = "O"
            print(f"[{filler}]", end="")
            if (i + 1) % self.grid == 0:
                print("")

        print(self.lastMove)

    def playerTurn(self):
        pos = 0

        if self.isAiActive():
            pos = self.findAiPos()
        else:
            while not (1 <= pos <= self.squares):
                text = f"Place {'X' if self.xIsActive else 'O' } [1-{self.squares}] "
                pos = inputIntInRange(text, 1, self.squares)
                if self.board[pos - 1] != 0:
                    print(f"Square {pos} is taken")
                    pos = 0
                    continue
        self.board[pos - 1] = 1 if self.xIsActive else 2
        self.lastMove = f"{'X' if self.xIsActive else 'O'}{'(AI)' if self.isAiActive() else ''} placed on {pos}"
        self.xIsActive = not self.xIsActive
        self.turn += 1

    def isAiActive(self):
        return self.aiEnabled and (
            (self.aiPlayerId == 1 and self.xIsActive)
            or ((not self.aiPlayerId == 1) and (not self.xIsActive))
        )

    def findAiPos(self):
        time.sleep(1.0)
        pos = 0
        gameCopy = TicTac(grid=self.grid, board=self.board.copy())
        boardCache = gameCopy.board.copy()

        def findWinningPos(gameCopy, id):
            for i, square in enumerate(gameCopy.board):
                if square == 0:
                    gameCopy.board[i] = id
                    if TicTac.findWinner(gameCopy):
                        # print("win found", i + 1, id, "wins")
                        return i + 1
                        break
                    else:
                        gameCopy.board[i] = 0
            return 0

        def randomPos(board):
            pos = 0
            while pos == 0:
                randPos = random.randint(1, len(board))
                if board[randPos - 1] == 0:
                    pos = randPos
            return pos

        # try to win
        pos = findWinningPos(gameCopy, self.aiPlayerId)

        # block other players win but not always
        if pos == 0 and (random.random()) < 0.8:
            gameCopy.board = boardCache
            humanPlayerId = 1 if self.aiPlayerId != 1 else 2
            pos = findWinningPos(gameCopy, humanPlayerId)

        # no winners, so pick a random free square
        if pos == 0:
            pos = randomPos(self.board)

        return pos

    @staticmethod
    def findWinner(game):
        def isWin(board, grid, combo):
            win = False
            for i in range(grid - 1):
                win = board[combo[i]] == board[combo[i + 1]]
                if win == False:
                    break
            return win

        winner = 0
        for combo in game.combos:
            if isWin(game.board, game.grid, combo) and game.board[combo[0]] != 0:
                winner = game.board[combo[0]]
                break
        return winner

    @staticmethod
    def findCombos(grid):
        def comboCreator(grid, start, n, direction):
            combo = []
            for i in range(grid):
                if direction == "hor":
                    combo.append(start + i)
                elif direction == "vert":
                    combo.append(grid * i + n)
                elif direction == "diagTopLeft":
                    combo.append((grid + 1) * i)
                elif direction == "diagTopRight":
                    combo.append((grid - 1) * (i + 1))
            return combo

        combos = []
        for n in range(grid):
            start = n * grid
            combos.append(comboCreator(grid, start, n, "hor"))
            combos.append(comboCreator(grid, start, n, "vert"))
        combos.append(comboCreator(grid, start, n, "diagTopLeft"))
        combos.append(comboCreator(grid, start, n, "diagTopRight"))
        return combos


def main():
    clearScreen()
    print("Tic-Tac-Toe")
    grid = inputIntInRange("Enter grid size [2-6] (3) ", 2, 6, 3)
    aiEnabled = input("Enable AI? [y/n] (y) ").lower() in {"y", ""}
    game = TicTac(grid, aiEnabled)

    while game.winner == 0:
        game.printBoard()
        if game.turn > game.squares:
            print("Board is full, game is a draw")
            break
        game.playerTurn()
        if game.turn >= (game.grid * 2) - 1:
            game.winner = TicTac.findWinner(game)
    else:
        game.printBoard()
        print(f"{'X' if game.winner == 1 else 'O'} won the game!")
    if input("Restart? [y/n] (y) ").lower() in {"y", ""}:
        main()


if __name__ == "__main__":
    main()
