import random
from time import sleep


print("")
print("")
print("")
print("\033[1;36;40m \n ")
print("▒█▀▀█ ▒█░░▒█ ▒█▀▀█ ▒█▀▀▀ ▒█▄░▒█ ")
print("▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ ▒█▀▀▀ ▒█▒█▒█")
print("▒█░░░ ▒█▄▀▄█ ▒█▄▄█ ▒█▄▄▄ ▒█░░▀█")
print("\033[1;35;40m 𝒞𝑅𝐸𝒜𝒯𝐸𝒟 𝐵𝒴 𝐻𝒰𝒩𝒯𝐸𝑅 \n")
print("")
print("\033[1;31;40m \n")
print("[ IMPORTANT: THIS GENERATOR IS LOCAL. I CANT SEE YOUR PASSWORD! ]")
print("")
print("\033[1;32;40m ꜱᴀꜰᴇ ᴘᴀꜱꜱᴡᴏʀᴅ ɢᴇɴᴇʀᴀᴛᴏʀ \n")
print("                   Type -start to get one")
print("                   Type exit to close it")
print("\033[1;36;40m  \n")

def mainfunc():
    user = input("User > ")
    if user == "-start":
        passw = input("Type a random word for your password > ")
        rn = random.randint(1, 100000)
        rn_2 = random.randint(1, 1000)
        rl = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        rl_2 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        rl_3 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        sleep(1)
        print("")
        print("Your Password > " "\033[1;32;40m" + str(rn) + rl + passw + rl_2 + str(rn_2) + rl_3 + "\n")
        print("\033[1;36;40m  \n")
        return mainfunc()

    if user == "exit":
        exit()

    else:
        print("\033[1;31;40m \n")
        print(user + " was not found.")
        print("\033[1;36;40m  \n")
        return mainfunc()

mainfunc()
