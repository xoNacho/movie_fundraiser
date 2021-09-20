valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]


check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":


        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        snack_choice = string_check(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)


        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)


print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered:")

for item in snack_order:
    print(item)
