import time
guestlist = []

while True:
  
    guestdata = dict()

    guestdata['name'] = input("What is your name? Or Q to exit.")
    if guestdata['name'] == "Q":
        break 
    guestdata['timestamp'] = time.time()


    guestlist.append(guestdata)
print(guestlist)




