# CryptoMailer

A package to send and receive encrypted emails via Gmail.

Encryption and decryption are done with the help of **Keyword Cipher** algorithm.

**NOTE:** Make sure to allow less secure app access for the Gmail account(s) that will be used to send/receive emails through this package.

Provide less secure app access from [here](https://myaccount.google.com/lesssecureapps).

## Package Details

PyPI link to package: https://pypi.org/project/cryptomailer/

### Directory Structure:

```
CryptoMailer/
├── cryptomailer
│   ├── crypt.py
│   ├── __init__.py
│   ├── mailer_receive.py
│   └── mailer_send.py
├── LICENSE
├── README.md
└── setup.py
```

-   `CryptoMailer`: [GitHub repository](https://github.com/AdityaSingh17/CryptoMailer).
-   `cryptomailer`: Package directory.
-   `cryptomailer/crypt.py`: Module used for encryption and description.
-   `cryptomailer/mailer_receive.py`: Module to receive emails.
-   `cryptomailer/mailer_send.py`: Module to send emails.
-   `setup.py`: File responsible to manage package.

### Using the package.

View file [sample.py](https://github.com/AdityaSingh17/CryptoMailer/blob/master/sample.py) to understand how to import and run the package.

Use the following command to run the send and receive emails using the package `cryptomailer`.

```
python3 sample.py
```
