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

    # Get name (Can't be blank)
    name = not_blank("Name: ")

    # Get age (Between 12 and 130)

    # Calculate ticket prices

    # Loop to ask for snacks

    # Calculate snack prices

# Ask for payment method (and apply the surcharge)


# Calculate total sales and profit

# Output data to text files


