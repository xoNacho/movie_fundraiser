# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tell users how many seats are left
    if count < 4:
        print("You have {} seats "
              "left".format(MAX_TICKETS - count ))

    # warns users that only one seat is left
    else:
        print("*** There is one seat left!! ***")

    # Get details...
    name = input("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the avaliable tickets! ")
else:
    print(" You have {} tickets.    \n"
          "There are {} places still avaliable"
          .format(count, MAX_TICKETS - count))
