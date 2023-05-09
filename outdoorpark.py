#Naomi Gong
#Outdoor Park 

n_row = 20
n_col = 26
global num_tickets
global seating

def create_seating():
    """
    This example code creates a 2d list (2d matrix) that can store seating.
    The matrix is populated with . since all seats are available
    """
    
    # our test matrix has 4 rows and 10 columns
     # available seatv
    seating = []
    available_seat = '.'
    # create some available seating
    for r in range(n_row):
        row = []
        for c in range(n_col):
            row.append(available_seat)
        seating.append(row)
    return seating 

seating = create_seating()

def print_seating(seat_data):
    let = "a"
    let_array = ["a"]
    for letter in range(25):
        #changes to unicode
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
    return seat_data

def update(new_seat, seat_num, num_tickets):
    col = seat_num[len(seat_num) - 1]
    row = int(seat_num[:-1])
    col = ord(col) -97
    n = 0
    while n <= num_tickets + 1 and col + n < 27:
        new_seat[row - 1][col - 1 + n] = "X"
        new_seat[row + 1][col -  1 + n] = "X"
        n = n + 1
    if col - 1 != 0:
        new_seat[row][col - 1] = "X"
    if col + num_tickets - 1 < 26:
        new_seat[row][col + num_tickets] = "X"
    print('c')
    seating = new_seat
    return None

#declared dictionary for names and emails
name_and_emailDict = {}

def check_seats(num_tickets, seat_num):
    open = True
    row = int(seat_num[0])
    col = seat_num[1]
    col = ord(col) - 97

    for c in range(num_tickets):
        if col + c > 25:
            return open
        else:
            if seating[row][col + c] != ".":
                open = False

    for c in range(num_tickets):
        if open:
            seating[row][col + c] = "e"
    return open


def buy_tickets():
    num_tickets = int(input("How many tickets would you want to buy?"))
    seat_num = input("Which seats would you like to buy ex. A0")
    seats_avail = check_seats(num_tickets, seat_num)
    if seats_avail:
        update(seating, seat_num, num_tickets)
    name = input("what is your name? ").lower()
    email = input("what is your email address?" )
    seat_type = input("What type of seats would you like to buy?").lower()
    name_and_emailDict[name] = str(num_tickets) + " starting at " + seat_num + ", " + seat_type
    seatcost = 0
    if seat_type == "front":
        seatcost = 80
    elif seat_type == "middle":
        seatcost = 50
    else:
        seatcost = 25
    total_cost = seatcost * int(num_tickets) * 1.0725
    print(f"{'name: ': <15}", name)
    print(f"{'email: ': <15}", email)
    print(f"{'number of tickets: ': <15}", num_tickets)
    print(f"{'total: ': <15}", total_cost)


def search_buyer():
    name = input("Please enter your name to see the tickets purchased")
    if name in name_and_emailDict:
        print(name +  ", you purchased: " + name_and_emailDict[name])

    else:
        print(name + "did not purchase any ticket")

        

dash = "-" * 40
print(dash)
print("Outdoor Park")
print(dash)
start = 0

userquit = False
while (not userquit):
    print("[b] buy" )
    print("[v]view seating" )
    print("[s] search for a customer by name and display their tickets purchased" )
    print("[d] display all the purchases made and total income")
    print("[q to quit")
    command = input("Enter command: ")

    if command == "v": 
        print_seating(seating)
    elif command == "b":
        buy_tickets()
    elif command == "s":
        search_buyer()

