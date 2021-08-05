# import statements

# functions go here

# check that ticket name is not blank
def not_blank(question):
    valid = False


    while not valid:
        response = input(question)

        # if name is not blank, program continues
        if response != "":
            return response

        # if name is blank, show error(& repeat loop)
        else:
            print("Sorry - this can't be blank, "
                 "Please enter your name ")




#   * * * * * * * * * * Main Routine * * * * * * * * * *

#  Set up dictionaries / lists needed to hold data

#  Ask user if they have used the program before & show if necessary

# Loop to get ticket details

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

    # Get name (Can't be blank)
    name = not_blank("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the avaliable tickets! ")
else:
    print(" You have {} tickets.    \n"
          "There are {} places still avaliable"
          .format(count, MAX_TICKETS - count))

    # Get name (Can't be blank)
    name = not_blank("Name: ")

# start of loop

# initialise loop so that it runs at least once


    # Get age (Between 12 and 130)

    # Calculate ticket prices

    # Loop to ask for snacks

    # Calculate snack prices

# Ask for payment method (and apply the surcharge)


# Calculate total sales and profit

# Output data to text files


