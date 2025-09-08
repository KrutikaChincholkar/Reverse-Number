# Take input from user
num = int(input("Enter a number: "))

reversed_num = 0
temp = num

# Reverse the number
while temp > 0:
    remainder = temp % 10
    reversed_num = reversed_num * 10 + remainder
    temp //= 10

print("Reversed number:", reversed_num)
