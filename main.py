slots = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
row1 = slots[0]
row2 = slots[1]
row3 = slots[2]
col1 = [slots[0][0], slots[1][0], slots[2][0]]
col2 = [slots[0][1], slots[1][1], slots[2][1]]
col3 = [slots[0][2], slots[1][2], slots[2][2]]
dia1 = [slots[0][0], slots[1][1], slots[2][2]]
dia2 = [slots[0][2], slots[1][1], slots[2][0]]

board = f"  {slots[0][0]}  |  {slots[0][1]}  |  {slots[0][2]}  \n" \
        f"-----------------\n" \
        f"  {slots[1][0]}  |  {slots[1][1]}  |  {slots[1][2]}  \n" \
        f"-----------------\n" \
        f"  {slots[2][0]}  |  {slots[2][1]}  |  {slots[2][2]}  "
turn_counter = 0


def game_end():
    if (len(set(row1)) == 1 or len(set(row2)) == 1 or len(set(row3)) == 1) or \
            (len(set(col1)) == 1 or len(set(col2)) == 1 or len(set(col3)) == 1) or \
            (len(set(dia1)) == 1 or len(set(dia2)) == 1):
        return True


def turn(player):
    global board
    if player == 1:
        print("\nPlayer X's turn")
        board = f"  {slots[0][0]}  |  {slots[0][1]}  |  {slots[0][2]}  \n" \
                f"-----------------\n" \
                f"  {slots[1][0]}  |  {slots[1][1]}  |  {slots[1][2]}  \n" \
                f"-----------------\n" \
                f"  {slots[2][0]}  |  {slots[2][1]}  |  {slots[2][2]}  "
        print(board)
        square = input("Please choose a numbered square to place an X in: ")
        if (square in slots[0] or square in slots[1] or square in slots[2]) and (square != "X") and (square != "O"):
            if int(square) <= 3:
                index = slots[0].index(square)
                slots[0][index] = "X"
            elif int(square) <= 6:
                index = slots[1].index(square)
                slots[1][index] = "X"
            else:
                index = slots[2].index(square)
                slots[2][index] = "X"
            return 1
        else:
            print("The input was invalid.")
            return 0
    elif player == 0:
        print("\nPlayer O's turn")
        board = f"  {slots[0][0]}  |  {slots[0][1]}  |  {slots[0][2]}  \n" \
                f"-----------------\n" \
                f"  {slots[1][0]}  |  {slots[1][1]}  |  {slots[1][2]}  \n" \
                f"-----------------\n" \
                f"  {slots[2][0]}  |  {slots[2][1]}  |  {slots[2][2]}  "
        print(board)
        square = input("Please choose a numbered square to place an O in: ")
        if (square in slots[0] or square in slots[1] or square in slots[2]) and (square != "X") and (square != "O"):
            if int(square) <= 3:
                index = slots[0].index(square)
                slots[0][index] = "O"
            elif int(square) <= 6:
                index = slots[1].index(square)
                slots[1][index] = "O"
            else:
                index = slots[2].index(square)
                slots[2][index] = "O"
            return 1
        else:
            print("The input was invalid.")
            return 0


print("Welcome to tic-tac-toe!")
print(input("Press enter to start the game: "))

while True:
    col1 = [slots[0][0], slots[1][0], slots[2][0]]
    col2 = [slots[0][1], slots[1][1], slots[2][1]]
    col3 = [slots[0][2], slots[1][2], slots[2][2]]
    dia1 = [slots[0][0], slots[1][1], slots[2][2]]
    dia2 = [slots[0][2], slots[1][1], slots[2][0]]
    if game_end():
        break
    elif turn_counter == 9:
        break
    else:
        if turn_counter % 2 == 0:
            if turn(1) == 1:
                turn_counter += 1
        elif turn_counter % 2 == 1:
            if turn(0) == 1:
                turn_counter += 1
        board = f"  {slots[0][0]}  |  {slots[0][1]}  |  {slots[0][2]}  \n" \
                f"-----------------\n" \
                f"  {slots[1][0]}  |  {slots[1][1]}  |  {slots[1][2]}  \n" \
                f"-----------------\n" \
                f"  {slots[2][0]}  |  {slots[2][1]}  |  {slots[2][2]}  "
        print(board)

if (turn_counter % 2 == 1) and ((len(set(row1)) == 1 or len(set(row2)) == 1 or len(set(row3)) == 1) or
                                (len(set(col1)) == 1 or len(set(col2)) == 1 or len(set(col3)) == 1) or
                                (len(set(dia1)) == 1 or len(set(dia2)) == 1)):
    print("\nPlayer X has won")
elif (turn_counter % 2 == 0) and ((len(set(row1)) == 1 or len(set(row2)) == 1 or len(set(row3)) == 1) or
                                  (len(set(col1)) == 1 or len(set(col2)) == 1 or len(set(col3)) == 1) or
                                  (len(set(dia1)) == 1 or len(set(dia2)) == 1)):
    print("\nPlayer O has won")
else:
    print("\nIt was a tie")
