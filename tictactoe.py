import os


def clear_scr():
    _ = os.system('cls')


def get_input(number_range: tuple) -> int:
    user_input = 'Wrong'
    while True:
        while user_input.isdigit() == False:
            user_input = input()
            if user_input.isdigit() == False:
                print("Wrong input.Try again: ", end='')
        if int(user_input) in range(number_range[0], number_range[1] + 1):
            break
        else:
            print("Out of range.Try again: ", end='')
            user_input = 'Wrong'
    return int(user_input)


def game_init() -> tuple:
    print("Choose board size (3 - 1000): ", end='')
    n = get_input((3, 1000))
    grid = [[' ' for _ in range(n)] for _ in range(n)]

    print("Choose your sign 1st player: ")
    print('1: X')
    print('2: O')
    print("Choice: ", end='')
    choice = get_input((1, 2))
    if choice == 1:
        p1 = 'X'
        p2 = 'O'
    else:
        p1 = 'O'
        p2 = 'X'
    return p1, p2, grid, n


def check_winner_move(grid: list, last_move: tuple, player: str) -> bool:
    if len(grid) < 5:
        n = len(grid)
    else:
        n = 5
    count = 0

    # check row
    for i in range(len(grid)):
        if grid[last_move[0]][i] == player:
            count += 1
            if count == n:
                return True
        else:
            count = 0

    # check column
    count = 1
    for i in range(len(grid)):
        if grid[i][last_move[1]] == player:
            count += 1
            if count == n:
                return True
        else:
            count = 0
    count = 0

    row_t = last_move[0] - min(last_move)
    col_t = last_move[1] - min(last_move)
    # diagonals
    for _ in range(len(grid)):
        if row_t >= len(grid) or col_t >= len(grid):
            break
        if grid[row_t][col_t] == player:
            count += 1
            if count == n:
                return True
        else:
            count = 0
        row_t += 1
        col_t += 1

    # anti diagonals
    row_t = last_move[0] + min(len(grid) - last_move[0], last_move[1])
    col_t = last_move[1] - min(len(grid) - last_move[0], last_move[1])
    for _ in range(len(grid)):
        if row_t >= len(grid) or col_t < 0:
            break
        if grid[row_t][col_t] == player:
            count += 1
            if count == n:
                return True
        else:
            count = 0
        row_t += 1
        col_t -= 1

    return False


def print_grid(grid):
    clear_scr()
    for i in grid:
        print(i)


if __name__ == '__main__':
    p1, p2, grid, n = game_init()
    clear_scr()
    cur_p = p1
    while True:
        print(f"{cur_p}'s turn: ")
        while True:
            print("row: ")
            row = get_input((1, n)) - 1
            print("column: ")
            col = get_input((1, n)) - 1
            # check if this move is existed
            if grid[row][col] != ' ':
                print_grid(grid)
                print("Cannot make this move.Try again ")
            else:
                grid[row][col] = cur_p
                break
        print_grid(grid)
        if check_winner_move(grid, (row, col), cur_p) == True:
            print(f"Player {cur_p} win!")
            break
        if cur_p == p1:
            cur_p = p2
        else:
            cur_p = p1
