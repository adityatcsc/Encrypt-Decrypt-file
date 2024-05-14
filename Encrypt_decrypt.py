from cryptography.fernet import Fernet

def encrypt_file(key,file):
    f=Fernet(key)

    with open(file, "rb+") as file:
        data = file.read()
        encrypted_data = f.encrypt(data)
        file.seek(0)
        file.write(encrypted_data)
        file.truncate()


def decrypt_file(key,file):
    f=Fernet(key)

    with open(file, "rb+") as file:
        data = file.read()
        decrypted_data = f.decrypt(data)
        file.seek(0)
        file.write(decrypted_data)
        file.truncate()

def generate_key():
    key = Fernet.generate_key()

    with open("key.txt", "wb") as file:
        file.write(key)

    print("check the generated key file with the key.")




print("1) encrypt the file. ")
print("2) decrypt the file. ")
print("3) Generate the key for encrypt and decrypt the file.")
print("4) close. ")
choice=int(input("enter the value :- "))

if choice==1:
    file=input("enter the file name :- ")
    key=input("enter the key to encrypt the file :- ")
    encrypt_file(key,file)
elif choice==2:
    file=input("enter the file name :- ")
    key=input("enter the key to decrypt the file :- ")
    decrypt_file(key,file)
elif choice==3:
    generate_key()
else:
    print("thanks for using.")
    quit()