totalGallons = 0
totalMiles = 0
gallons_used = 0
miles_driven = 0

while gallons_used != -1:
    gallons_used =  float (input('Enter the gallons used (-1 to end): '))
    if gallons_used == -1:
        break
    miles_driven = float (input('Enter the miles driven: '))
    print('The miles/gallon for this tank was' , miles_driven / gallons_used)

    totalGallons += gallons_used
    totalMiles += miles_driven
    
print('The overall average miles/gallon was' , totalMiles / totalGallons )