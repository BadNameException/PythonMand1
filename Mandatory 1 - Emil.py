
import random


def oppgave_1():

    names = ["Snorre", "Marius", "Emil"]
    usernames = ["Sannitie", "Granno", "Emle"]
    for i in range(len(names)):
        print (names[i] + ": " + usernames[i])

def oppgave_2():
    password = []  # type:

    for i in range(3):

        password.append(random.randint(0, 9))

    password_as_string = ""
    for x in password:
        password_as_string = password_as_string + str(x)

    print ("\nA little peak to know the algorithm works: " + str(password_as_string))

    i_as_string = ""
    i = 0

    while i < 1000:
        if i < 10:
            i_as_string = "00" + str(i)
            if i_as_string == password_as_string:
                break
            else:
                i_as_string = i_as_string[2:]
                i += 1
                continue

        elif 10 < i < 100:
            i_as_string = "0" + str(i)
            if i_as_string == password_as_string:
                break
            else:
                i_as_string = i_as_string[1:]
                i += 1
                continue

        else:
            i_as_string = str(i)
            if i_as_string == password_as_string:
                break
            else:
                i += 1
                continue

    print("Password i plain text: " + password_as_string)

    print ("Cracked password: " + i_as_string)

def oppgave_3():

    password_list = {"chris":"helloworld", "john":"passw1", "nelly":"2hell1", "wendy":"1Passw"}  # type
    counter = 0
    for i in password_list.values():
        if i[0].isdigit(): # Checks if first letter is digit
            chars = set(i[1:]) # Temporary variable to make a substring
            cap_letter = sum(1 for c in chars if c.isupper()) # Counts number of capital letters
            if cap_letter == 1: # Checks if substring has one capital letter
                if i.__len__() == 6: # Checks if the password consists of 6 letters
                    counter += 1
                    print ("Possible password nr" + str(counter) + ":  " + i)
                    break
                else:continue
            else:continue
        else:continue


oppgave_1()
oppgave_2()
oppgave_3()

