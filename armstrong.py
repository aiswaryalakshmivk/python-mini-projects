n = int(input("Enter a number: "))
temp = n
s = 0
digits = len(str(n))

while temp > 0:
    d = temp % 10
    s = s + d ** digits
    temp = temp // 10

if s == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
