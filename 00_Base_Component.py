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

# Checks for an integer more than 0
def int_check(question):

    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)




#   * * * * * * * * * * Main Routine * * * * * * * * * *

#  Set up dictionaries / lists needed to hold data

#  Ask user if they have used the program before & show if necessary

# Loop to get ticket details
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

while name != "xxx" and ticket_count < MAX_TICKETS:

    # tell users how many seats are left
    if ticket_count < 4:
        print("You have {} seats "
              "left".format(MAX_TICKETS - ticket_count ))

    # warns users that only one seat is left
    else:
        print("*** There is one seat left!! ***")

    # Get details...

    # Get name (Can't be blank)
    name = not_blank("Name: ")


    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # Get age (Between 12 and 130)
    age = int_check("Age: ")

    # check age is valid
    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price

# End of ticket loop
# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))



# Tell user if they have unsold tickets...
if ticket_count == MAX_TICKETS:
    print("You have sold all the avaliable tickets! ")
else:
    print(" You have {} tickets.There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))



# start of loop

# initialise loop so that it runs at least once




    # Calculate ticket prices

    # Loop to ask for snacks

    # Calculate snack prices

# Ask for payment method (and apply the surcharge)


# Calculate total sales and profit

# Output data to text files


