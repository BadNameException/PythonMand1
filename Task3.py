password_list = {"chris": "helloworld", "john": "passw1", "nelly": "2hell1", "wendy": "1Passw"}


def pwfinder(pwlist):

    for value in pwlist.values():

        print(len(value))
        if not len(value) == 6:

            password_array = [password_list[value]]

            # Check if the first character is a digit.
            if password_array[0].isdigit():
                for index, character in enumerate(password_array, start=1):
                    print(character)
                    if character.isupper():
                        has_upper = True
                        break
                    else:
                        # Print out a message showing the program came to this point.
                        # This could be bad practice in a real program as it would print
                        # out all the password not matching the criteria.
                        print("The password \" {} \" has no uppercast letters".format())

            if has_upper is True:
                print("The password " + value + " matches your criteria!")
                has_upper = False
        else:
            print("Password does not have {} characters")


pwfinder(password_list)