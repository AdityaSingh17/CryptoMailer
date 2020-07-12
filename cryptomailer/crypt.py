"""
Keyword cipher algorithm.
"""

import sys

# Define the alphabets.
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

# Generate update aplhabets after adding the keyword.
# Keyword should preferably contain unique alphabets.
def alphakey_gen(Keyword):
    keyword = Keyword.upper()
    temp = ""
    for i in range(len(keyword)):
        temp += keyword[i]
    for i in range(26):
        temp += chr(i+65)
    AlphaKey = ""
    # Remove non unique elements from Keyword and store the updated alphabets in AlphaKey.
    for i in range(len(temp)):
        found = False   # IGNORE FLAG
        for j in range(len(AlphaKey)):
            if temp[i] == AlphaKey[j]:
                found = True
                break
        if not found:
            AlphaKey += temp[i]

    return AlphaKey


def encrypto(Key, Message):
    AlphaKey = alphakey_gen(Key) # Generate AlphaKey.
    message = Message.upper()
    encrypted_text = ""
    for i in range(len(message)):
        if message[i] == chr(32):
            encrypted_text += " "
        else:
            counter = 0
            for j in range(len(Alpha)):
                if message[i] == Alpha[j]:
                    encrypted_text += AlphaKey[counter]
                    break
                else:
                    counter += 1
                    
    return(encrypted_text)


def decrypto(Key, Message):
    AlphaKey = alphakey_gen(Key)
    message = Message.upper()
    decrypted_text = ""
    for i in range(len(message)):
        if message[i] == chr(32):
            decrypted_text += " "
        else:
            counter = 0
            for j in range(len(Alpha)):
                if message[i] == AlphaKey[j]:
                    decrypted_text += Alpha[counter]
                    break
                else:
                    counter += 1

    return(decrypted_text)
