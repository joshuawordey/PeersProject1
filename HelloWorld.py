# print ("Hello World!")

# temp = int (input ("Input Temperature in Farenhieghts: "))
# deg = round(((temp) - 32) * 5/9 , 2)
# print ("Your Temperature is: " , deg , " degree Celcius")

# input ("Names: ")
# input ("Age: ")
# input ("Location: ")
# input ("Symptoms: ")

unit = input ("Enter unit of your Temp (C for Celcius and F for Farenhieghts): ")

if unit == "F":
    temp = int (input ("Input Temperature in Farenhieght: "))
    deg = round(((temp) - 32) * 5/9 , 2)
    print ("Your Temperature is: " , deg , " degree Celcius")
elif unit == "C":
    temp = int (input ("Input Temperature in Celcius: "))
    far = round (((9/5 * temp) + 32) , 2)
    print ("Your Temperature is: " , far , " degree Farenhieghts")
else:
    print("Enter a correct unit")


# print (d)
