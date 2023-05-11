import json

class receipt:

    def __init__(self, name, email, num_tickets, seat_type, seat_num, cost):
        self.name = name
        self.email = email
        self.num_tickets = num_tickets
        self.seat_type = seat_type
        self.seat_num = seat_num
        self.cost = cost

    def print_receipt(self):
        dash = '-' * 40
        print(dash)
        print(f"{'name': <20}", end = "")
        print(f"{self.name: >20}")
        print(f"{'email': <20}", end = "")
        print(f"{self.email: >20}")
        print(f"{'number of tickets purchased': <20}", end = "")
        print(f"{self.num_tickets: >15}")
        print(f"{'type of seats': <20}", end = "")
        print(f"{self.seat_type: >20}")
        print(f"{'seat number (start)': <20}", end = "")
        print(f"{self.seat_num: >20}")
        print(f"{'total cost': <20}", end = "")
        print(f"{self.cost: >20}")
        dash = '-' * 40
        
        

        
    
    