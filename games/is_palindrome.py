import time


def palindromeGame():
    while True:
        userWord = input("Enter a palindrome: ")
        if userWord == userWord[::-1]:
            print("Yes, it is!")
            break
        else:
            print("No, its not!")
    time.sleep(2)