n = int(input("Enter number of email addresses: "))
emails = []

for i in range(n):
    email = input()
    emails.append(email)

emails.sort()
print(emails)
