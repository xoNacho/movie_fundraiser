

# functions go here
def string_check(choice, options):

    for var_list in options:

        #if the snack is in one of the lists, return the full
        if choice in var_list:

            chosen = var_list[0].title()
            is_valid = "yes"
            break


        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)




for item in range (0, 6):

    desired_snack = input("Snack: ").lower()

    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)
