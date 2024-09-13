binary = int(input("Binary Number: "))

def binToDec(binary):
    l_bin = len(str(binary))
    dec = 0
    for i in range(l_bin):
        dec += binary % 10 * 2 ** i
        binary = binary // 10
    print(dec)
binToDec(binary)