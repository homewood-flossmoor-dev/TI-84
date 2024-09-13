dec = int(input("Decimal number: "))
def dectoBin(dec):
    if dec > 1:
        dectoBin(dec // 2)
    print(dec % 2, end='')
dectoBin(dec)
print()