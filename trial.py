import camelcase 
import re 
def getrate(amount):
    if (amount == 1000):
        print("The amount is equal to 1000!")
    elif (amount <= 1000):
        return amount * 0.98
    else:
        print("Transaction complete!!")
def validate_pin(pin):
    for x in pin:
        if x.isalpha():
            return False
        elif re.match(".", pin):
            return False
    if len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False
        
PIN = input("Enter a PIN: ")
validate_pin(PIN) 
c = camelcase.CamelCase()
txt = "start the transaction!!!"
print(c.hump(txt))

Amount = int(input("Enter the Amount:"))

print(getrate(Amount))
