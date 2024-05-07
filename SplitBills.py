n = int(input("The number of mates in flat: "))
expenses = {}

# Input expenses for each mate
for x in range(n) :
    name = input(f"The name of the {x + 1}'s mate is: ")
    amount = round(float(input(f"The amount spent by {name} is: ")), 2)
    expenses[name] = amount

print("Expenses:", expenses)

# Calculate total sum of expenses
total_expenses = round(sum(expenses.values()) / n, 2)
print("Absolute expenses per individual:", total_expenses)

# Calculate individual contribution and add to the dictionary
for name, amount in expenses.items() :
    individual_contribution = round(total_expenses - amount, 2)
    expenses[name] = {'amount' : amount, 'contribution' : individual_contribution}

print("Expenses with individual contributions:", expenses)

# Calculate net contributions
net_contributions = {name : contribution['contribution'] for name, contribution in expenses.items()}

# Redistribute the amounts
while any(value < 0 for value in net_contributions.values()) :
    # Find mates with positive and negative contributions
    debitors = {name : value for name, value in net_contributions.items() if value < 0}
    creditors = {name : value for name, value in net_contributions.items() if value > 0}

    # Sort mates by the absolute value of their contributions
    sorted_debitors = sorted(debitors.items(), key=lambda x : x[1], reverse=True)
    sorted_creditors = sorted(creditors.items(), key=lambda x : x[1])

    # Transfer money from creditors to debitors
    for debitor, debitor_amount in sorted_debitors :
        for creditor, creditor_amount in sorted_creditors :
            transfer_amount = min(-debitor_amount, creditor_amount)
            expenses[creditor]['contribution'] -= transfer_amount
            expenses[debitor]['contribution'] += transfer_amount
            net_contributions[creditor] -= transfer_amount
            net_contributions[debitor] += transfer_amount
            print(f"{creditor} pays {transfer_amount} to {debitor}")
            if net_contributions[debitor] == 0 :
                break
        if net_contributions[debitor] == 0 :
            break

print("Final expenses after redistribution:", expenses)
