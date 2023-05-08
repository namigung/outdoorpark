#Naomi Gong
#Outdoor Park 
def create_seating():
    """
    This example code creates a 2d list (2d matrix) that can store seating.
    The matrix is populated with . since all seats are available
    """
    # our test matrix has 4 rows and 10 columns
     # available seat
    available_seat = '.'
    # create some available seating
    seating = []
    for r in range(n_row):
        row = []
        for c in range(n_col):
            row.append(available_seat)
        seating.append(row)
    return seating 

def print_seating(seat_data):
    let = "a"
    let_array = ["a"]
    for letetr in range(25):
        i = ord(let)
        i = i + 1
        let = chr(i)
        let_array.append(let)
    print(end="\t")
    for l in let_array:
        print(l + " ", end="")
    print()
    # print available seating
    for r in range(n_row):
        print(r+1, end="\t")
        for c in range(n_col):
            print(seat_data[r][c], end=" ")
        print()
    return None

# our test matrix has 4 rows and 10 columns
n_row = 20
n_col = 26
dash = "-" * 40
print(dash)
print("Outdoor Park")
print(dash)

userquit = False
while (not userquit):
    print("[b] buy" )
    print("[v]view seating" )
    print("[s] search for a customer by name and display their tickets purchased" )
    print("[d] display all the purchases made and total income")
    command = input("Enter command: ")

    if command == "v":
        new_seat = create_seating()
        print_seating(new_seat)

