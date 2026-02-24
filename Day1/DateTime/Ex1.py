from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

print('Date Formatting: ')
print("Formatted date:", now.strftime("%Y-%m-%d"))
print("Formatted date and time:", now.strftime("%d/%m/%Y"))
print("Formatted date and time:", now.strftime("%B %d, %Y")) 
print("Formatted time:", now.strftime("%H:%M:%S"))
print("IST time:", now.strftime("%I:%M %p"))   
print(now.strftime("%A, %B %d %Y"))  