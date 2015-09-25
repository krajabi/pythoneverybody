def pay(hrs, rate):
    if hrs > 40:
        hour = 40 
        left = hrs - 40 
        p = (hour * rate) + (left * (rate * 1.5))
    elif h <= 40:
        p = (hrs * rate)
    return p
    
try:
    hrs = float(raw_input("How many hours do you got: "))
    rate = float(raw_input("How much rate do you got: "))
except:
    print "Please put in numbers"
    exit()

p = computerpay(hrs, rate)

print p