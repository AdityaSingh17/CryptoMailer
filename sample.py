from cryptomailer.mailer_send import mailer_send
from cryptomailer.mailer_receive import mailer_receive

print("1. Send mail")
print("2. Receive mail")

choice = int(input("Enter your choice: "))

if choice == 1:
    mailer_send()
elif choice == 2:
    mailer_receive()
else:
    print("Please enter a valid choice.")
