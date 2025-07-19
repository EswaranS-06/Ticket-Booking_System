class train():
    def __init__(self):
        self.customers = []
        self.sections = []
        self.sections.append(sleeper(True, 20))
        for i in range(3):
            self.sections.append(sleeper(False, 20))
            
        for i in range(4):
            print(self.sections[i])
            
        
    def TotalReservedSeats(self, seat_type=None):
        max_seats = 0
        for section in self.sections:
            max_seats += sum(section.numSeats(seat_type))
        return max_seats
        
    def booking(self):
        rev_type = input("1. Takkal\n2. Reservation\nEnter (1,2): ")
        if rev_type == 1 and self.TotalReservedSeats() > 50:
            pass

        # customer_info = customer().set_info()
        # for section in self.sections:
        #     if section.isTakkal() == (seat_type == 0):
        #         if section.numSeats(seat_type) > 0:
        #             section.book(seat_type, customer_info)
        #             print("Booking successful")
        #             return
        # print("Booking failed")
        
    def takkalBook(self):
        num_seat = int(input("How many tickets [MAX:20]: "))
        info_type = input("1. Book every ticket in your\n2. Give Names for every Ticket\nOnce selected process is not Revertable\nEnter your choise (1,2): ")
        if info_type == 1:
            self.customers.append(customer.set_info())
            for i in range(num_seat):
                pass
    def reserveBook(self):
        pass

class sleeper():
    def __init__(self, is_takkal, num_seats):
        self.seating = [[],[],[]]
        self.max_seat = num_seats
        self.is_takkal = is_takkal
         
    def __str__(self):
        return( f"{'Takkal' if self.is_takkal else 'Reservation'} : {self.numSeats()}")
                
    def isTakkal(self):
        return self.is_takkal
    
    def numSeats(self, seat_type=None):
        available_seats = []
        if seat_type == None:
            for section in self.seating:
                available_seats.append(len(section))
            return available_seats
        else:
            return list(len(self.seating[seat_type]))
    
    def book(self, seat_type, info):
        self.seating[seat_type].append(info)
            
            
class customer():
    def __init__(self):
        self.info = []
        
    def set_info(self):
        #self.info.append(input("Enter your Name: "))
        #self.info.appendint((input("Enter your Age: ")))
        self.info.append("Rex")
        self.info.append(20)
        return self.info
        
t = train()
