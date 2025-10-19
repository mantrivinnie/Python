def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

# Take input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if are_anagrams(s1, s2):
    print("✅ The strings are anagrams.")
else:
    print("❌ The strings are not anagrams.")


#Alternate method
from collections import Counter

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return Counter(str1) == Counter(str2)
