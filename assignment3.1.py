try:
    h_inp = raw_input("Please enter hours: ")
    hours=float(h_inp)
    r_inp = raw_input("Please enter rate: ")
    rate= float(r_inp)
except:
    print "Please enter a whole number!"
    quit()

def pay(h,r):
    if (h>40): 
        pay = (40*r)+(h-40)*1.5*r
    else:
        pay = (h*r)     
    return pay

print pay(hours,rate)