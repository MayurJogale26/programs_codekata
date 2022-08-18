n = input()
day, month, year = n.split('/')

if (int(day) < 32 and int(month) < 13 and len(year) == 4 ):
    print("yes")
else:
    print("no")