def password_encoder(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

# Alejandro A Decoder

def decoder(password):

    # empty list to fill
    decoded_password = []

    # creates list with int values from string given
    for i in password:
        decoded_password.append(int(i))

        # loops over password to alter object
    for index, i in enumerate(decoded_password):

        decoded_password[index] = i - 3

        if decoded_password[index] < 0:
            # makes sure that its one digit
            decoded_password[index] = decoded_password[index] + 10

    # empty string to add too
    str_decode_password = ''

    # iterates over encoded password and turns into string
    for i in decoded_password:
        str_decode_password += str(i)


    return str_decode_password

while True:
    print("Menu\n-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")

    if option == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = password_encoder(password)
        print("Your password has been encoded and stored!")


    elif option == "2":
        # Implement password decoding logic here
        decoded_password = decoder(encoded_password)

        print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')

    elif option == "3":
        break

    else:
        print("Invalid option. Please try again.\n")

