import os


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def inputIntInRange(text, x, y):
    while 1:
        try:
            num = int(input(text))
            if not x <= num <= y:
                raise Exception
        except:
            pass
        else:
            return num


class TicTac:
    "X = 1, O = 2, X goes first"

    def __init__(self, grid=3):
        self.grid = grid
        self.squares = grid ** 2
        self.board = [0] * self.squares
        self.winner = 0
        self.xIsActive = True
        self.turn = 1
        self.lastMove = ""
        self.combos = TicTac.generateCombos(grid)

    def printBoard(self):
        clearScreen()
        # print(self.combos)
        print(f"Tic-Tac-Toe x{self.grid}")

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
        while not (1 <= pos <= self.squares):
            text = f"Place {'X' if self.xIsActive else 'O' }, input 1-{self.squares}: "
            pos = inputIntInRange(text, 1, self.squares)
            if self.board[pos - 1] != 0:
                print(f"Square {pos} is not free")
                pos = 0
                continue
        else:
            self.board[pos - 1] = 1 if self.xIsActive else 2
            self.lastMove = f"{'X' if self.xIsActive else 'O'} placed on {pos}"
            self.xIsActive = not self.xIsActive
            self.turn += 1

    def findWinner(self):
        winner = 0
        board = self.board

        for combo in self.combos:
            if self.findWinnerHelper(combo) and board[combo[0]] != 0:
                winner = board[combo[0]]
                break

        return winner

    def findWinnerHelper(self, combo):
        if self.grid == 3:
            return self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]
        elif self.grid == 4:
            return (
                self.board[combo[0]]
                == self.board[combo[1]]
                == self.board[combo[2]]
                == self.board[combo[3]]
            )
        elif self.grid == 5:
            return (
                self.board[combo[0]]
                == self.board[combo[1]]
                == self.board[combo[2]]
                == self.board[combo[3]]
                == self.board[combo[4]]
            )

    @staticmethod
    def generateCombos(grid):
        combos = []
        for n in range(grid):
            start = n * grid
            combos.append(TicTac.comboGeneratorHelper(grid, start, n, "hor"))
            combos.append(TicTac.comboGeneratorHelper(grid, start, n, "vert"))
        combos.append(TicTac.comboGeneratorHelper(grid, start, n, "diagTopLeft"))
        combos.append(TicTac.comboGeneratorHelper(grid, start, n, "diagTopRight"))
        return combos

    @staticmethod
    def comboGeneratorHelper(grid, start, n, direction):
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


def main():
    clearScreen()
    print("Tic-Tac-Toe")
    game = TicTac(inputIntInRange("Enter grid size from 3 to 5: ", 3, 5))

    while game.winner == 0:
        game.printBoard()

        if game.turn > game.squares:
            print("Board is full, game is a draw")
            break
        game.playerTurn()
        if game.turn >= (game.grid * 2) - 1:
            game.winner = game.findWinner()
    else:
        game.printBoard()
        print(f"{'X' if game.winner == 1 else 'O'} won the game!")
    if input("Restart? y/n ").lower() == "y":
        main()


if __name__ == "__main__":
    main()
