import re

# Functions go here
def string_check(choice, options):
    for var_list in options:

        is_valid = ""
        chosen = ""

        # if the snack is in one of the lists, return the full
        if choice in var_list:
            #Get full name of snack and put it in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"


number_regex = "^[1-9]"

# valid snacks holds list of all snacks
# Each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# , and possible abbreviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "o", "juice", "e"],
]


yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Holds snack order for a single user
snack_order = []

#ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks?").lower()
    check_snack = string_check(want_snack, yes_no)

if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break


        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)

        if amount >= 5:
            print("Sorry - we have a four snack minimum")
            snack_choice = "invalid choice"

        snack_row.append(amount)
        snack_order.append(snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)

print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")


else:
    print("Snacks Ordered")

    ''' for item in snack_order:
    print(item)
    '''

    print(snack_order)

