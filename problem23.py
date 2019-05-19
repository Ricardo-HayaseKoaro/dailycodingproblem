import copy


def min_path(board, curr_x, curr_y, end_x, end_y, n_steps):

    if curr_x == end_x and curr_y == end_y:
        return True, n_steps

    m = len(board)  # number of rows
    n = len(board[0])  # n of columns

    # out of the board
    if curr_y < 0 or curr_y >= m or curr_x < 0 or curr_x >= n:
        return False, 0

    # hit a wall
    if board[curr_y][curr_x]:
        return False, 0

    aux_board = copy.deepcopy(board)
    aux_board[curr_y][curr_x] = True

    min_steps = []

    a, aux1 = min_path(aux_board, curr_x, curr_y - 1, end_x, end_y, n_steps + 1)
    if a:
        min_steps.append(aux1)
    a, aux2 = min_path(aux_board, curr_x + 1, curr_y, end_x, end_y, n_steps + 1)
    if a:
        min_steps.append(aux2)
    a, aux3 = min_path(aux_board, curr_x, curr_y + 1, end_x, end_y, n_steps + 1)
    if a:
        min_steps.append(aux3)
    a, aux4 = min_path(aux_board, curr_x - 1, curr_y, end_x, end_y, n_steps + 1)
    if a:
        min_steps.append(aux4)

    if not min_steps:
        return False, 0

    return True, min(min_steps)


f = False
t = True

board = [[f, f, f, f],
        [t, t, f, t],
        [f, f, f, f],
        [f, f, f, f]]

begin_x = 0
begin_y = 3

end_x = 0
end_y = 0

n_steps = 0

print(min_path(board, begin_x, begin_y, end_x, end_y, n_steps))