from cryptography.fernet import Fernet
import getpass

#Create key
key = Fernet.generate_key()
cipher_suite = Fernet(key)
username = str.encode(input("Enter the username\n"))
#Enter the password
passw = getpass.getpass("Enter the password \n")
#Generate binary password
passb = str.encode(passw)
#Generrate ciphered password
cipher_text = cipher_suite.encrypt(passb)

with open('/Users/gabriel/Desktop/Scripts/API_Training/creds.bin', 'wb') as file:
    file.write(username)
    file.write(b'\n')
    file.write(cipher_text)
