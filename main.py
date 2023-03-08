# Alexander Hennecke

def encode(password):
    encoded_password = ""
    for i in range(len(password)):
        encoded_password += str(int(password[i]) + 3)
    
    print("Your password has been encoded and stored!")
    return encoded_password

def decode(password):
    decoded_password = ""
    for i in range(len(password)):
        decoded_password += str(int(password[i]) - 3)
    
    print(f"The encoded password is {password}, and the original password is {decoded_password}.")

def menu():
    print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

def main():
    while True:
        menu()

        userChoice = input("Please enter an option: ")

        if userChoice == "1":
            password = str(input("Please enter your password to encode: "))
            savedPassword = password
            password = encode(password)

        elif userChoice == "2":
            decode(password)

        elif userChoice == "3":
            exit()


if __name__ == "__main__":
    main()