import os


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


class TicTac:
    "X = 1, O = 2, X goes first"

    def __init__(self):
        self.board = [0] * 9
        self.winner = 0
        self.xIsActive = True
        self.turn = 1
        self.lastMove = ""


def printBoard(game):
    clearScreen()
    print("Tic-Tac-Toe")
    for i, v in enumerate(game.board):
        filler = " "
        if v == 1:
            filler = "X"
        elif v == 2:
            filler = "O"
        print(f"[{filler}]", end="")
        if (i + 1) % 3 == 0:
            print("")
    print(game.lastMove)


def inputIntInRange(text, x, y):
    while 1:
        try:
            num = int(input(text))
        except:
            pass
        else:
            return num if x <= num <= y else 0


def playerTurn(game):
    pos = 0

    while not (1 <= pos <= 9):
        text = f"Place {'X' if game.xIsActive else 'O' }, input 1-9: "
        pos = inputIntInRange(text, 1, 9)
        if game.board[pos - 1] != 0:
            print(f"Square {pos} is not free")
            pos = 0
            continue
    else:
        game.board[pos - 1] = 1 if game.xIsActive else 2
        game.lastMove = f"{'X' if game.xIsActive else 'O'} placed on {pos}"
        game.xIsActive = not game.xIsActive
        game.turn += 1


def findWinner(game):
    winner = 0
    board = game.board
    combos = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    for combo in combos:
        if (
            board[combo[0]] == board[combo[1]] == board[combo[2]]
            and board[combo[0]] != 0
        ):
            winner = board[combo[0]]
            break
    return winner


def main():
    game = TicTac()

    while game.winner == 0:
        printBoard(game)
        if game.turn > 9:
            print("Board is full, game is a draw")
            break
        playerTurn(game)
        game.winner = findWinner(game)
    else:
        printBoard(game)
        print(f"{'X' if game.winner == 1 else 'O'} won the game!")


main()
