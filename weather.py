degree=int(input("Enter the degree:"))
if degree <=20:
    print("cold weather")
elif degree >20 and degree <=38:
    print("normal Weather")
else:
    print("hot! Weather")
fahrenheit=((degree*1.8)+32)
print("The fahrenheit value is ",fahrenheit,"F")