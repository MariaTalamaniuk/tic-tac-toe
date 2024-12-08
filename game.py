def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Вітаю в грі Хрестики-Нолики!")
    print_board(board)

    while True:
        print(f"Гравець {players[current_player]}, ваш хід!")
        try:
            row = int(input("Введіть номер рядка (0, 1, 2): "))
            col = int(input("Введіть номер стовпця (0, 1, 2): "))

            if board[row][col] == " ":
                board[row][col] = players[current_player]
                print_board(board)

                if check_winner(board, players[current_player]):
                    print(f"Гравець {players[current_player]} виграв!")
                    break
                elif is_draw(board):
                    print("Нічия!")
                    break
                current_player = 1 - current_player
            else:
                print("Це місце вже зайняте. Спробуйте інше.")
        except (ValueError, IndexError):
            print("Некоректний ввід. Будь ласка, введіть числа від 0 до 2.")

if __name__ == "__main__":
    main()
