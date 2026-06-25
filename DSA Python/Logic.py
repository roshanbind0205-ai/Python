n=int(input("Enter the number : "))
print("palindrom" if str(n) == str(n)[::-1] else "not palindrom")