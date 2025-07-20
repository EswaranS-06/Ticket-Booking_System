    def takkalBook(self):
        seat_type = int(input("1. Lower\n2. Middle\n3. Upper\nEnter (1,2,3): "))-1
        if not seat_type in range(0,3):
            print("Invalid selection try to use only the above options")
            return
        num_seats = int(input("How many tickets [MAX:20]: "))
        info_type = int(input("1. Book every ticket in your\n2. Give Names for every Ticket\nOnce selected process is not Revertable\nEnter your choise (1,2): "))
        if info_type == 1:
            c = customer()
            self.customers.append(c.setInfo())
            temp = self.availableSection(num_seats, seat_type, 0)
            for i in range(num_seats):
                self.sections[temp].book(seat_type, self.customers[-1])
                
            else:
                print(f"Succussefullly Booked {num_seats} seats\nin the Name of {self.customers[-1][0]}")
        elif info_type == 2:
            temp = self.availableSection(num_seats, seat_type, 0)
            for i in range(num_seats):
                c = customer()
                self.customers.append(c.setInfo())
                self.sections[temp].book(seat_type, self.customers[-1])
                
            else:
                print(f"Succussefullly Booked {num_seats} seats\nin the Name of {self.customers[-1][0]}")