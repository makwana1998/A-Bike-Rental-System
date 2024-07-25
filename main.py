class Bikeshop:
    
    def __init__(self,stock):
        self.stock=stock
        
    def DisplayBike(self):
        print("Total Bikes",self.stock)
        
    def RentalBike(self,a):
        
        if a<=0:
            print("Enter The Positive Value or Greter the Zero")
            
        elif a>self.stock:
            print("Enter The Value ('less then stock')")
            
        else:
            print("Total Prices",a*100)
            print("Toatl Bikes",self.stock)
            
            
while True:

    obj=Bikeshop(100)
    uc = int(input('''
       
1) Display Stocks
2) Rental a Bike
3) Exit
                   '''))
    
    if uc ==1:
        obj.DisplayBike()  
    elif uc==2:
         n = int(input("Enter the quntity:--"))
         obj.RentalBike(n)
    else:
        break


             
       