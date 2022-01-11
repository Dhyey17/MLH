class NegativeValue(Exception):
    pass


try:
    total_bill = float(input("Enter total amount of bill: "))
    people = int(input("Enter number of people: "))
    if people < 0:
        raise NegativeValue
    share = total_bill / people
    print(f"Each person needs to pay: {share}")
except ZeroDivisionError:
    print("0 is not a valid input")
except NegativeValue:
    print("Negative value is not a valid input")
