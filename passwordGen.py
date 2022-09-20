import sys
import random

original_stdout = sys.stdout
siteName = str(input("What site are you creating a password for?:\n"))
userName = str(input("What is you username for the site?:\n"))
passLength = int(input("Password Length?: \n"))
with open('/home/sourprout/.vault.txt', 'a') as f:
    sys.stdout = f
    print("Site: ", siteName)
    print("Username: ", userName)
    for x in range(passLength):
        x = (random.randint(33, 127))
        print(chr(x), end='')
    print("\n")
sys.stdout = original_stdout
