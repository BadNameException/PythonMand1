password_list = {"chris": "helloworld", "john": "passw1", "nelly": "2hell1", "wendy": "1Passw", "hei": "dinsei"}


def pwfinder(pwlist, length):

    for value in pwlist.values():

        # Check if the password has length-parameter amounts of characters.
        if len(value) == length:
            password_array = list(value)

            # Check if the first character is a digit.
            if password_array[0].isdigit():
                for index, character in enumerate(password_array, start=1):
                    if character.isupper():
                        print("The password " + value + " matches your criteria!")
                        break


pwfinder(password_list, 6)
