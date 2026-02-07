banner = (5*"="+" Circle Area Finder "+5*"=")
print(banner)

diameter = float(input("=> Enter your circle's diameter (in CM): "))
radius = diameter / 2
pi = 22 / 7

result =  pi * radius * radius
message = (f"=> The result is {result} CM")
print(message)
