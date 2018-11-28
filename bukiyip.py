# convert a decimal number to bukiyip.
def decimal_to_bukiyip(a):  
    bukiyip = ''
    quotient = 2000000
    while quotient > 0:
        quotient = a // 3
        remainder = a % 3
        bukiyip += str(remainder) 
        a = quotient
    return bukiyip[::-1]

# convert a bukiyip number to decimal
def bukiyip_to_decimal(a):
    decimal = 0
    string_a = str(a)
    power = 0
    for i in string_a[::-1]:
        decimal += int(i) * pow(3, power)
        power += 1
    return int(decimal)
# add two Bukiyip numbers.
def bukiyip_add(a, b):
    return decimal_to_bukiyip(bukiyip_to_decimal(a) + bukiyip_to_decimal(b))

# multiply two Bukiyip numbers.
def bukiyip_multiply(a, b):
    return decimal_to_bukiyip(bukiyip_to_decimal(a) * bukiyip_to_decimal(b))