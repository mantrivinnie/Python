def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniform comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]   # Compare with the reversed string

# Take input
string = input("Enter a string: ")

if is_palindrome(string):
    print("✅ The string is a palindrome.")
else:
    print("❌ The string is not a palindrome.")



#Enter a string: Madam
#The string is a palindrome.

#Enter a string: OpenAI
#The string is not a palindrome.

