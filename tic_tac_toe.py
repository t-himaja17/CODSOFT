import math

board = [" " for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def make_move(square, letter):
    if board[square] == " ":
        board[square] = letter
        return True
    return False

def winner(player):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_patterns)

def is_full():
    return " " not in board

def minimax(player):
    max_player = "O"
    other_player = "X" if player == "O" else "O"

    if winner(other_player):
        return {"position": None, "score": 1 * (len(available_moves()) + 1) if other_player == max_player else -1 * (len(available_moves()) + 1)}
    elif is_full():
        return {"position": None, "score": 0}

    if player == max_player:
        best = {"position": None, "score": -math.inf}
    else:
        best = {"position": None, "score": math.inf}

    for possible_move in available_moves():
        board[possible_move] = player
        sim_score = minimax(other_player)
        board[possible_move] = " "
        sim_score["position"] = possible_move

        if player == max_player:
            if sim_score["score"] > best["score"]:
                best = sim_score
        else:
            if sim_score["score"] < best["score"]:
                best = sim_score

    return best

def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    human = "X"
    ai = "O"

    while True:
        move = int(input("Your turn! Pick a spot (0 to 8): "))
        if make_move(move, human):
            print_board()
            if winner(human):
                print("You win! 🎉")
                break
            elif is_full():
                print("It's a tie! 🤝")
                break
        else:
            print("That spot is taken. Try another!")

        print("Computer is thinking...")
        ai_move = minimax(ai)["position"]
        make_move(ai_move, ai)
        print_board()
        if winner(ai):
            print("Computer wins! 🤖")
            break
        elif is_full():
            print("It's a tie! 🤝")
            break

if __name__ == "__main__":
    play_game()
