print("(1)First Free Service")
print("(2)Second Free Service")
print("(3)third Free Service")

while True:
    no = int(input("Enter the Free Service number>> "))
    if (no == 1 or no == 2 or no == 3):
        break

    
    
        
mile = float(input("Enter number of Miles    >> "))

if(no == 1):
    if(mile > 1500 and mile <= 3000):
        print("Vehicle must be serviced.")
    else :
        print("Free Service is not available")
elif(no == 2) :
     if(mile > 3001 and mile <= 4500):
          print("Vehicle must be serviced.")
     else:
          print("Free Service is not available")
else:
    if(mile > 5000 and mile <= 7000):
        print("Vehicle must be serviced.")
    else:
        print("Free service is not available")

    




