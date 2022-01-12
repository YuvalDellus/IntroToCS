BOARD_SIZE = 9
FILENAME = "SUDOKU_SOL.txt"


def initboard(n):
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    return board


def legal_placment(board,col,row):
    for i in range(BOARD_SIZE):
        if i != row:
            if board[col][i] == board[col][row]:
                return False
        if i != col:
            if board[i][row] == board[col][row]:
                return False

    start_point_row = int(row // BOARD_SIZE**0.5)
    start_point_col = int(col // BOARD_SIZE ** 0.5)

    for i in range(int(BOARD_SIZE**0.5)):
        for j in range(int(BOARD_SIZE ** 0.5)):
            if start_point_col + i == col and start_point_row + j == row:
                print(start_point_col + i,start_point_row + j)
                pass
            else:
                if board[start_point_col + i][start_point_row + j] == board[col][row]:
                    # print("row: ", row, "col: ", col)
                    # print_board(board,"k")
                    print("jnjnj",board[col][row])

                    return False
    return True


def print_board(board,file_name):
    # file = open(file_name,"w")
    for i in range(BOARD_SIZE):
        row = ["|"]
        for j in range(BOARD_SIZE):
            row.append(str(board[i][j]))
            if not (j+1)%3:
                row.append("|")
        row = ",".join(row)
        print(row,end="\n")
        if not (i+1)%3:
            print("_"*BOARD_SIZE*3)
        # file.write(row)
        # file.write("\n")
    # file.close()


def play_game(board):
    if play_game_helper(board,0,0):
        print_board(board,FILENAME)
    else:
        print("There’s no solution for this board”")


def play_game_helper(board,c,r):
    for number in range(1,10):
        board[c][r] = number
        if legal_placment(board,c,r):
            print_board(board, "k")
            print("\n")
            if c == r and c == BOARD_SIZE -1:
                return True
            if c < BOARD_SIZE-1:
                play_game_helper(board, c+1, r)
            else:
                play_game_helper(board, 0, r+1)
    return False


def factorial(n):
    z=1
    if n>1:
        z=(n-1)*factorial(n-1)
    return z

def flat(list1):
    print(list1)
    # print(list1[0])
    if len(list1) == 0:
        return []
    if type(list1) == list:
        if type(list1[0]) != tuple:
            return [list1[0]] + flat(list1[1:])
    else:
        return [list1] + flat(list1[1:])


L = [1,[2,['a',(3,'b')]],(5,6),([11,22],)]
# L = [1,[2,[3]]]
print(flat(L))

