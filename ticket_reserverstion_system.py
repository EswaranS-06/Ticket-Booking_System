class train():
    def __init__(self):
        self.section = []
        self.section.append(sleeper(True, 20))
        for i in range(3):
            self.section.append(sleeper(False, 20))
            
        print(self.section[0].numSeats())
        
    
class sleeper():
    def __init__(self, is_takkal, num_seats):
        self.seating = [[],[],[]]
        self.max_seat = num_seats
        self.is_takkal = is_takkal
                
    def isTakkal(self):
        return self.is_takkal
    
    def numSeats(self, seat_type=None):
        available_seats = []
        if seat_type == None:
            for section in self.seating:
                available_seats.append(len(section))
            return available_seats
        else:
            return len(self.seating[seat_type])
    
    def book(self, seat_type, info):
        self.seating[seat_type].append(info)\
            
            
class customer():
    def __init__(self):
        self.info = []
        
    def set_info(self):
        name = "Rex" #input("Enter your Name: ")
        age = 20 #int(input("Enter your Age: "))
        
t = train()
