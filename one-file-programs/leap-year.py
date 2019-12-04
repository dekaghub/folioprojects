test = [2000, 2006, 2008, 2092, 2090, 2091, 2952, 1952, 1956]

def leapYear(t):
    if t%4 == 0 or (t%100 == 0 and t%400 == 0):
        return True
    else:
        return False

for t in test:
    print(leapYear(t))