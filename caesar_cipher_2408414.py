
"""
    Caesar Cipher Program
    Student Name:Shashank Pandey
    Student ID: 2408414
"""
import os
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
EXIT_MESSAGE = "\nThanks for using the program, goodbye!"
AGAIN_MESSAGE = "\nWould you like to encrypt or decrypt another message? (y/n): "
ACTION_MESSAGE = "\nWould you like to encrypt (e) or decrypt (d)?: "
#To welcome:
def welcome():
    """
    Prints the welcome message
            
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.\n")
#To enter message:
def enter_message(mode):
    """
    Returns a tuple containing user selected mode, message and shift number.

    """

    if mode=="e":
        message=input("What message would you like to encrypt (e):")
        shift = int(input("What is the shift number: "))
    elif mode=="d":
        message=input("What message would you like to decrypt (d):")
        shift = int(input("What is the shift number: "))
    else:
        print("\nInvalid Mode! Please choose 'e' or 'd'.")
    return(mode,message.upper(),shift)
#To encrypt message:
def encrypt(message,shift):
    """
    Returns encrypted version of the given message using given shift

    """


    result=""
    for char in message:
        if char.isalpha():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result
#To decrypt message:
def decrypt(message,shift):
    """
    Returns decrypted version of the given message using given shift

    """
    result=""
    for char in message:
        if char.isalpha():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char
    return result

#Takes file and read line by line and encrypt and store it.
def process_file(filename, mode,shift):
    

    if not is_file(filename):
        print("File not found.")
        return []

    with open(filename, 'r') as file:
        messages = [line.strip() for line in file]

    if mode == 'e':
        return [encrypt(message, shift) for message in messages]
    else:
        return [decrypt(message, shift) for message in messages]
    #checks file name
def is_file(filename):
    return os.path.isfile(filename)
#Write the encrypted or decrypted message to the new file.
def write_messages(messages):
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

def message_or_file():
    """
    Takes user input for if they want to enter console mode or file mode.
    """

    while True:
        mode = input(ACTION_MESSAGE).lower()

        if mode in ("e", "d"):
            console = input(
                "\nDo you want to process messages using console or file? (c or f) "
            )

            if console == "f":
                filename = input("\nEnter file name with it's extension: ")
                if is_file(filename):
                    shift = int(input("\nEnter the shift number: "))
                    write_messages(process_file(filename, mode, shift))
                    print("\nAction completed successfully.")

                    try_again = input(AGAIN_MESSAGE)

                    if try_again == "n":
                        return print(EXIT_MESSAGE)

                    main()

                else:
                    print("\nFile not found!!\nTry Again!\n")

            elif console == "c":
                return enter_message(mode)

            else:
                print('\nInvalid Choice. Please choose "f" or "c"!')

        else:
            print('Invalid Choice. Please choose "e" or "d"!')


# ? Main function to start the program and also print the output
def main():
    """
    Main function to run all other functions in order

    """

    # ? Prints the welcome message
    welcome()

    values = message_or_file()

    if values is not None:
        if values[0] == "e":
            print(encrypt(values[1], values[2]))

        elif values[0] == "d":
            print(decrypt(values[1], values[2]))

        try_again = input(AGAIN_MESSAGE)

        if try_again == "n":
            return print(EXIT_MESSAGE)

        main()

    return None


# ? Start
main()


        
        
