try:
    Start = int(input("Enter a starting number: "))
    Last = int(input("Enter a last number:"))
    result = Start / Last
    print(result)
except ZeroDivisionError:
    print("Cannot Divide with 0")
except ValueError:
    print("Enter Number only pls")
except Exception:
    print("Something went wrong! Try again")