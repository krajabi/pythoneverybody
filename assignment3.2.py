try:
    s = raw_input("Please enter a score between 0.0 and 1.0")
except: 
    print "Try again. Please enter a score between 0.0 and 1.0"
    quit()

s = float(s)

if s >= 0.9:
    print "A"
elif s >= 0.8:
    print "B"
elif s >= 0.7:
    print "C"
elif s >= 0.6:
    print "D"
elif s < 0.6:
    print "F"