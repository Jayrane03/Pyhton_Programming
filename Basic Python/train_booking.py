class Train:
    def __init__(self  , name ,fare , seats , snumber ):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def getStatus(self):
         print("**********") 
         print(f"The name of the train is{self.name} ")  
         print(f"The number of seats available in the train are {self.seats} ")  
         print("**********")
     
    def fareInfo(self):
        print(f"The fare of the ticket is Rs {self.fare}")
        
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your tickets are booked ! Your seat number is {seat.snumber}")     
            self.seats = self.seats - 1
        else:
            print("Sorry the train is full ! You can try in tatkal")
            
            
    def cancelTicket(self):
        self.seats = self.seats +1
        # print("Your seat number is "+)
    
    
k = Train("Konkan Kanya Express : 14002" , 150 , 200 , 10) 
k.getStatus()
k.fareInfo()
k.bookTicket()
k.getStatus()
k.cancelTicket()
k.getStatus()

 
