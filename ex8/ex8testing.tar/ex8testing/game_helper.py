BOARD_LEGEND = 'legend'
MESSAGE_GAME_OVER = 'gameover'

def report(s):
    print(s)


def board_to_string(board_length, hits, bombs, hit_ships, ships):
    row = ['_']*board_length
    inner_board = [row[:] for i in range(board_length)]
    for (x, y) in ships: inner_board[y][x] = 'X'
    for (x, y) in hit_ships: inner_board[y][x] = 'O'
    for (x, y) in bombs.keys(): inner_board[y][x] = str(bombs[(x, y)])
    for (x, y) in hits: inner_board[y][x] = '*'
    return ','.join([''.join(row) for row in inner_board])


targets = [(2,3),(0,1),(0,0),(0,3),(4,4),(4,4),(1,3),(3,1),(0,0)]
targets_src = [(2,3),(0,1),(0,0),(0,3),(4,4),(4,4),(1,3),(3,1),(0,0)]
def get_target(board_size):
    if targets:
        res = targets.pop()
        print('target:'+str(res))
        return res
    raise Exception('Reading too many inputs')


def report_turn(hits, terminations):
    report(str(hits) + ' hits, ' + str(terminations) + ' terminations')

def report_gameover():
    report(MESSAGE_GAME_OVER)

def report_legend():
    report(BOARD_LEGEND)
    global targets
    targets = targets_src[:]
