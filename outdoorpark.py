#Naomi Gong
#Outdoor Park 

import json
from receipt import receipt


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

    #prints X
    for c in range(num_tickets):
        if open:
            new_seat[row][col + c] = "X"

    #prints e in row above
    while n <= num_tickets + 3 and col + n - 1 < 27:
        new_seat[row - 1][col - 2 + n] = "e"
        new_seat[row + 1][col -  2 + n] = "e"
        if col - 2 + n < 0:
            new_seat[row - 1][col - 2 + n] = "."
            new_seat[row + 1][col -  2 + n] = "."
        n = n + 1
    
    if col - 2 >= 0:
        n = 0
        while n < 2:
            new_seat[row][col - 1 - n] = "e"
            n = n + 1
    if col + num_tickets + 2 < 26:
        n = 0
        while n < 2:
            new_seat[row][col + num_tickets + n] = "e"
            n = n + 1
    seating = new_seat
    return None


def check_seats(num_tickets, seat_num):
    open = True
    col = seat_num[len(seat_num) - 1]
    row = int(seat_num[:-1])
    col = ord(col) - 97

    for c in range(num_tickets):
       if col + c > 26:
           return False
       if seating[row][col + c] != ".":
           return False
    return True


def buy_tickets():
    num_tickets = int(input("How many tickets would you want to buy? "))
    seat_num = input("Which seats would you like to buy ex. 0A ")
    seats_avail = check_seats(num_tickets, seat_num)
    if seats_avail:
        update(seating, seat_num, num_tickets)
    if seats_avail == False:
        print("This seat is not available")
        return None
    name = input("what is your name? ").lower()
    email = input("what is your email address? " )

    col = seat_num[len(seat_num) - 1]
    row = int(seat_num[:-1])
    
    if row >= 1 and row <= 5:
        seat_type = "front"
    elif row >= 5 and row <= 10:
        seat_type = "middle"
    else:
        seat_type = "back"
    seatcost = 0
    if seat_type == "front":
        seatcost = 80
    elif seat_type == "middle":
        seatcost = 50
    else:
        seatcost = 25
    total_cost = seatcost * int(num_tickets) * 1.0725
     
    p = receipt(name, email, num_tickets, seat_type, seat_num, total_cost)

    purchase.append(p)
    #change code here
    
    print(f"{'name: ': <15}", name)
    print(f"{'email: ': <15}", email)
    print(f"{'number of tickets: ': <15}", num_tickets)
    print(f"{'total: ': <15}", total_cost)


def update_json():
    recieptList = [p.__dict__ for p in purchase]
    with open ('purchase.json', 'w') as json_file:
        json.dump(recieptList, json_file)
    json_file.close()
    



def search_buyer():
    name = input("Please enter your name to see the tickets purchased: ")
    for person in purchase:
        if person.name == name:
            person.print_receipt()
            return None
    print("Person not found")

def display_All():
    for person in purchase:
        person.print_receipt()
    total = 0 
    for person in purchase:
        total = total + person.cost
    dash = "-" * 40
    print(dash)
    print("The total income is " + str(total))

purchase = []
try: 
    with open('purchase.json', 'r') as json_file:
        purchase_data = json.load(json_file)
    purchase = [receipt(p['name'], p['email'], p['num_tickets'], p['seat_type'], p['seat_num'], p['cost']) for p in purchase_data]
except (Exception):
    pass

for p in purchase:
    update(seating, p.seat_num, p.num_tickets)

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
    elif command == "d":
        display_All()
    elif command == 'q':
        update_json()
        userquit = True
    else:
        print("command not found")

