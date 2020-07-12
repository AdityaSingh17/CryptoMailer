"""
Script to receive an encrypted message via Gmail and decode it.
"""
import getpass
import imaplib
import email
import sys
from cryptomailer import crypt


def mailer_receive():
    # Start IMAP server over SSL connection.
    M = imaplib.IMAP4_SSL("imap.gmail.com")

    # Get user inputs.
    recevieremail_id = str(input("Enter the receiver Email ID: "))
    recevierpassword = str(getpass.getpass("Enter receiver Password: "))  # Hide password while typing.
    # Request login of the receiver.
    try:
        print("Logging in the receiver:", recevieremail_id)
        M.login(recevieremail_id, recevierpassword)
        print("Successfully logged in!")
    except:
        print("Login failed, please try again.")
        sys.exit()

    senderemail = str(input("Enter the intended sender whose email you want to read: "))

    try:
        M.select()  # Select all mails.
        typ, data = M.search(None, "FROM", senderemail)  # Search and select all emails from intended sender.
        # Iterate through the selected mails and print information.
        for num in data[0].split():
            typ, data = M.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])
            hdr = email.header.make_header(email.header.decode_header(msg["Subject"]))
            subject = str(hdr)
            print("\n")
            print("Email number:", int(num))
            print("Subject:", subject)
            print("Received message:", msg.get_payload().strip())
            key = str(getpass.getpass("Enter the keyword: "))
            decoded = crypt.decrypto(key, msg.get_payload().strip())
            print("Decoded message:", decoded)
    except:
        print("Error reading mails, please try again!")
        sys.exit()

    # Close the server.
    M.close()
    # Send request to logout.
    M.logout()

