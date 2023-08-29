# Write a Python program that computes the net amount of a bank account based a 
# transaction log from console input. The transaction log format is shown as following: D 
# 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for 
# withdraw and deposit) D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program: 
# D 300 
# D 300 
# W 200 
# D 100 
# Then, the output should be: 500

def process_transactions():
    net_amount = 0
    
    while True:
        transaction = input("Enter transaction (D/W amount or 'done' to finish): ")
        
        if transaction.lower() == "done":
            break
        
        trans_type, amount = transaction.split()
        amount = int(amount)
        
        if trans_type == "D":
            net_amount += amount
        elif trans_type == "W":
            if net_amount >= amount:
                net_amount -= amount
            else:
                print("Withdrawal not allowed, insufficient balance.")
        else:
            print("Invalid transaction type. Use D for deposit and W for withdrawal.")
    
    return net_amount

def main():
    net_amount = process_transactions()
    print(f"Net amount in the bank account: {net_amount}")

if __name__ == "__main__":
    main()
