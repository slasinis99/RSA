from rsa import User

def main_loop():
    u = User()
    print("Welcome new RSA user!\n\nWhat would you like to do?")
    state = 0
    state_options = {0:["Show modulus and public key","Send a message","Decrypt a message","Exit"]}
    while not state == 4:
        if state == 0:
            for i, s in enumerate(state_options[state]):
                print(f'{i}) {s}')
            print()
            state = int(input())+1
        if state == 1:
            n, e = u.public_key()
            print(f'Public Key:\n{e}\n\nModulus:\n{n}\n')
            state = 0
        if state == 2:
            n = int(input("Please enter Modulus:"))
            print()
            e = int(input("Please enter Public Key:"))
            print()
            s = input("Please input message:")
            print()
            print(f"Encrypted Message:{u.encrypt(n, e, s)}")
            print()
            state = 0
        if state == 3:
            c = int(input("Enter encrypted message:"))
            print()
            print(f"Decrypted Message: {u.decrypt(c)}")
            print()
            state = 0

if __name__ == "__main__":
    main_loop()