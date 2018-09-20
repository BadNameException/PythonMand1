import random
 
password = []
 
for i in range(3):
    password.append(random.randint(0, 9))
 
 
def comparePw(crack, pw):
    if crack == pw:
        return True
    else:
        return False
 
 
def cracker(pw):
    cracked = [0, 0, 0]
    found = False
    while not found:
        for i in range(10):
            if found:
                break
            cracked[0] = i
            if comparePw(cracked, pw):
                found = True
            for i in range(10):
                if found:
                    break
                cracked[1] = i
                if comparePw(cracked, pw):
                    found = True
                for i in range(10):
                    if found:
                        break
                    cracked[2] = i
                    if comparePw(cracked, pw):
                        found = True
 
        print("The password was found! it is: " + ''.join(str(e) for e in cracked))
 
 
print("The secret password to guess is: " + ''.join(str(e) for e in password))
cracker(password)