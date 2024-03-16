def main():
    a = input("Enter string: ")
    b = [x.lower() for x in a if x.isalnum()]
    if b == b[::-1]: print("It is a palindrome.") 
    else: print("It is not a palindrome.")

if __name__ == '__main__':
    main()