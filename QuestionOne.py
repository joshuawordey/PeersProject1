#create a variable (temp) to accept inputs of the temperature
temp = float (input ("Input Temperature in Farenhieghts: "))

#Set the result of the conversion to a new variable (deg)
deg = round(((temp) - 32) * 5/9 , 2)

#Print the result of the conversion
print ("Your Temperature is: " , deg , " degree Celcius")
