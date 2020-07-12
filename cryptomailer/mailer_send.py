"""
Script to send an encrypted message via Gmail to the intended user.
"""
import getpass
import smtplib
import sys
from cryptomailer import crypt


def mailer_send():
    # Establish SMPT connection on port 587.
    handle = smtplib.SMTP("smtp.gmail.com", 587)
    # Start TLS handshake.
    handle.starttls()

    # Get inputs from user.
    senderemail_id = str(input("Enter sender Email ID: "))
    senderpassword = str(getpass.getpass("Enter sender Password: "))  # Hide password while typing.
    # Request login of the sender.
    try:
        print("Logging in the sender", senderemail_id, "...")
        handle.login(senderemail_id, senderpassword)
        print("Successfully logged in!")
    except:
        print("Login failed, please try again!")
        sys.exit()

    subject = str(input("Enter the subject: "))
    message = str(input("Enter the message: "))
    key = str(getpass.getpass("Enter the keyword: "))  # Hide key while typing.
    # Encrypt the messsage.
    print("Encrypting message ...")
    message = crypt.encrypto(key, message)
    print("Message encrypted!")

    recevieremail_id = str(input("Enter the receiver email id: "))
    # Generate and send mail.
    print("Generating mail ... ")
    mail = "Subject: " + subject + "\n\n" + message
    try:
        handle.sendmail(senderemail_id, recevieremail_id, mail)  # Send email to receiver.
        print("Mail sent successfully to receiver!")
    except:
        print("Error in sending mail.")
        sys.exit()

    # Close the SMTP server.
    print("Closing the SMTP server.")
    handle.quit()
