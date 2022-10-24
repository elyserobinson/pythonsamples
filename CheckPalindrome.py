def main():
    # Prompt the user to enter a string
    s = input("Enter a string: ").strip()

    if isPalindrome(s):
        print(s, "is a palidrome")
    else:
        print(s, "is not a palindrome")

# Check if a string is a palindrome
def isPalindrome(s):
    # The Index of the first character in the string
    low = 0

    # The index of the last character in the string
    high = len(s) - 1

    while low < high:
        if s[low] != s[high]:
            return False # not a palindrome
        low += 1
        high -= 1

    return True # The string is a palindrome

main() # Call the main function
