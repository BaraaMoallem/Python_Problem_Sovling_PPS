# Prompt user for number between 1 and 50 inclusive
num = eval(input("Enter start point: "))
while num < 1 or num > 50:
    num = int(input("Enter start point: "))
N = []

# Multiply the number by 2 to the power of its index and print list
for i in range(10):
    N.append(num * 2 ** i)
    print("N[", i, "] = ", N[i], sep = '')
