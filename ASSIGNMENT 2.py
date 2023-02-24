"""
CIVIL ENGINEERING YEAR 2
ODOI AUNT ESI
6943221


"""
# Names of cars and their prices allocation
Cars={
"Range Rover": 1000,
"Land Cruiser": 2000,
"Toyota Corolla": 3000,
"Audi 08": 4000,
"BMW X6": 5000,
"Chevrolet": 6000,
"G-Wagon": 7000,
"Honda Civic":8000,
"Mercedes Benz":9000,
"Limousine":10000,
"Ferrari Carlifornia":11000,
"Honda S 200":12000,
"Suzuki Cervo":13000,
"Honda Life":14000,
"Fiat Panda":15000,
"Opel Astra":16000,
"Hyundai Santa Fe":17000,
"Mazda CX-5":18000,
"Nissan Titan":19000,
"Ford F-250":20000,
"Audi A5":21000,
}
#provide client car name
Car_Name=input("Enter your preferred car:")
#check if car name is in the list of cars
if Car_Name in Cars:
    print("Available")
#if car name is present, get the cost
    Car_Cost=Cars[Car_Name]
    print(f"The price of {Car_Name} is ${Car_Cost}.")
else:
    #if car name is not present,inform client
    print(f"Sorry, {Car_Name} is not availabe.")
    
    


    
    
