count_transactions = int(input())
bank_account = 0
counter = 0

while counter < count_transactions:
    current_transaction = float(input())
    if current_transaction < 0:
        print("Invalid operation")
        break
    bank_account += current_transaction
    print (f"Increase {current_transaction}")
    counter += 1
print (f"Total : {bank_account}")