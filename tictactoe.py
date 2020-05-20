matriks = [[" ", " ", " "] for row in range(3)]
input_tmpl = "XOXOXOXOX"
input_tmpl_indx = 0

def print_result():
    print(f"""
---------
| {matriks[0][2]} {matriks[1][2]} {matriks[2][2]} |
| {matriks[0][1]} {matriks[1][1]} {matriks[2][1]} |
| {matriks[0][0]} {matriks[1][0]} {matriks[2][0]} |
---------""")


def win(pattern):
    if matriks[0][2] + matriks[1][2] + matriks[2][2] == pattern \
            or matriks[0][1] + matriks[1][1] + matriks[2][1] == pattern \
            or matriks[0][0] + matriks[1][0] + matriks[2][0] == pattern \
            or matriks[0][0] + matriks[0][1] + matriks[0][2] == pattern \
            or matriks[1][0] + matriks[1][1] + matriks[1][2] == pattern \
            or matriks[2][0] + matriks[2][1] + matriks[2][2] == pattern \
            or matriks[0][0] + matriks[1][1] + matriks[2][2] == pattern \
            or matriks[2][0] + matriks[1][1] + matriks[0][2] == pattern:
        return True
    else:
        return False


def search_element(element):
    for i in range(3):
        for y in range(3):
            if matriks[i][y] == element:
                return True


def game_status():
    if win("XXX") and win("OOO"):
        return "Impossible"
    elif win("XXX"):
        return "X wins"
    elif win("OOO"):
        return "O wins"
    elif not win("XXX") and not win("OOO") and search_element(" ") is not True:
        return "Draw"
    else:
        return "Game not finished"


def validate_input():
    coordinates = input("Enter the coordinates: ")
    selected: str
    global input_tmpl_indx

    try:
        row: int
        column: int
        column = int(coordinates[0])
        row = int(coordinates[2])
        if row not in (1, 2, 3) or column not in (1, 2, 3):
            print("Coordinates should be from 1 to 3!")
            return True
    except ValueError:
        print("You should enter numbers!")
        return True

    if matriks[column - 1][row - 1] != " ":
        print("This cell is occupied! Choose another one!")
        return True
    else:
        matriks[column - 1][row - 1] = input_tmpl[input_tmpl_indx]
        input_tmpl_indx += 1
        print_result()
        if game_status() == "Game not finished":
            return True
        else:
            return False


if __name__ == "__main__":
    print_result()

    while validate_input():
        pass

    print(game_status())