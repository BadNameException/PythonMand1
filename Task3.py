password_list = {"chris": "helloworld", "john": "passw1", "nelly": "2hell1", "wendy": "1Passw"}


def pwfinder(pwlist, length):

    global has_upper

    for value in pwlist.values():
        print(value)
        # Check if the password has length-parameter amounts of characters.
        if len(value) == length:


            password_array = list(value)

            # Check if the first character is a digit.
            if password_array[0].isdigit():
                #for index, character in enumerate(password_array, start=1):
                for character in password_array:
                    print(character)
                    if character.isupper():
                        has_upper = True
                        break

                if has_upper is True:
                    print("The password " + value + " matches your criteria!")
                    has_upper = False
        else:
            print("The password \"{}\" does not have {} characters.".format(value, length))


pwfinder(password_list, 6)
