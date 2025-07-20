from tabulate import tabulate as tb
class train():
    def __init__(self, train_name):
        self.train_name = train_name
        self.customers = []
        self.sections = []
        self.sections.append(sleeper(True, 20))
        for i in range(3):
            self.sections.append(sleeper(False, 20))
            
    def __str__(self):
        return self.train_name
            
    def display(self):
        for section in self.sections:
            #for i in range(4):
            print(section)
            #section.display()
            
    def TotalReservedSeats(self, seat_type=None):
        max_seats = 0
        for section in self.sections:
            max_seats += sum(section.reservedSeats(seat_type))
        return max_seats
    
    def availableSection(self, num_seats, seat_type, is_takkal=1):
        for i in range(is_takkal, 4):
            if num_seats > self.sections[i].availableSeats(seat_type):
                continue
            else:
                return i
        else:
            return None #worst case <--------------------------------
        
    def booking(self):
        rev_type = int(input("1. Takkal\n2. Reservation\nEnter (1,2): "))
        if rev_type == 1:
            if self.TotalReservedSeats() > 50:
                self.bookingType(0)
            else :
                print("Sorry Takkal is Not open till now")
            
        elif rev_type == 2:
            self.bookingType(1)
            
        else:
            print("\033[41mInvalid Input\033[0m Try To Use Only the (1 or 2)")
                     
    def bookingType(self, is_takkal):
        try:
            seat_type = int(input("1. Lower\n2. Middle\n3. Upper\nEnter (1,2,3): "))-1
            if not seat_type in range(0,3):
                print("\033[41mInvalid selection try to use only the above options\033[0m")
                return
            num_seats = int(input("How many tickets [MAX:20]: "))
            if num_seats > 20:
                print("Sorry the Maximum limit is 20")
                return
            info_type = int(input("1. Book every ticket in your\n2. Give Names for every Ticket\nOnce selected process is not Revertable\nEnter your choise (1,2): "))
        except (ValueError, TypeError):
            print("\033[41mInvalid Input\033[0m")
            return
        
        if info_type == 1:
            c = customer()
            self.customers.append(c.setInfo())
            temp = self.availableSection(num_seats, seat_type, is_takkal)
            if temp == None:
                print("Sorry, There is a Shortage of seats currently")
            for i in range(num_seats):
                self.sections[temp].book(seat_type, self.customers[-1])
                
            else:
                print(f"Succussefullly Booked {num_seats} seats\nin the Name of {self.customers[-1][0]}")
        elif info_type == 2:
            temp = self.availableSection(num_seats, seat_type, is_takkal)
            for i in range(num_seats):
                c = customer()
                self.customers.append(c.setInfo())
                self.sections[temp].book(seat_type, self.customers[-1])
                
            else:
                print(f"Succussefullly Booked {num_seats} seats\nin the Name of {self.customers[-1][0]}")

class sleeper():
    def __init__(self, is_takkal, num_seats):
        self.seating = [[],[],[]]
        self.max_seat = num_seats
        self.is_takkal = is_takkal
         
    def __str__(self):
        return( f"{'Takkal' if self.is_takkal else 'Reservation'} : {self.reservedSeats()}")
                
    def isTakkal(self):
        return self.is_takkal
    
    def availableSeats(self, seat_type):
        return self.max_seat - len(self.seating[seat_type])
    
    def reservedSeats(self, seat_type=None):
        available_seats = []
        if seat_type == None:
            for section in self.seating:
                available_seats.append(len(section))
            return available_seats
        else:
            return [len(self.seating[seat_type])]
    
    def book(self, seat_type, info):
        self.seating[seat_type].append(info)
        
    def display(self):
        print(tb(self.seating, tablefmt="fancy_grid"))
        #print(self.seating)   
            
class customer():
    def __init__(self):
        self.info = []
        
    def setInfo(self):
        name = input("Enter your Name: ")
        try :
            age = int(input("Enter your Age: "))
        except (ValueError, TypeError):
            age = 0
        self.info.append(name)
        self.info.append(age)
        # self.info.append("e")
        # self.info.append(0)
        return self.info
    
    def getInfo(self):
        return self.info
    
t = train("Chennai to Thiruchy")
t2 = train("Chennai to Madurai")   
trains = [t,t2]
def main():
    global trains
    dec = input("Are you looking to Book Ticket? (Yes[y]/No[n])").strip().lower()
    if 'y' in dec:
        pass
    
    elif "n" in dec:
        print("Your Welcome!!!")
        return
    elif "a" in dec:
        print("\033[34;47m You are currently adding a New Train Route\033[0m")
        name = input("Enter the Train Route: ")
        t = train(name)
        trains.append(t)
        main()
    else:
        print("\033[41mInvalid Input\033[0m")
    while True:        
        print("""
            Hello your Welcome to the OUR
                \033[;34mTicket Booking Service \033[0m
                """)

        for i in range(len(trains)):
            print(f"\n{i+1}. {trains[i]}")
            
        print()  
        try :
            sel = int(input("Select the Train route: "))-1
        except (ValueError, TypeError):
            print("\033[41mInvalid Input\033[0m")
            continue
        
        print(trains[sel])
        
        while True:
            print("""
                  1. Ticket Booking
                  2. Reserved Seats

                  0. Exit
                  """)
            try :
                c = int(input("Enter your choise: "))
            except (ValueError, TypeError):
                print("\033[41mInvalid Input\033[0m")
                continue
            
            if c == 1:
                trains[sel].booking()
            
            elif c == 2:
                trains[sel].display()
            elif c == 3:
                break
        
        
if __name__ == main():
    main()