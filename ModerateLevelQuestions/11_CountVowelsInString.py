def count_vowels(s):
    vowels = "aeiouAEIOU"   # both lowercase and uppercase
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Take input
string = input("Enter a string: ")
vowel_count = count_vowels(string)

print("Number of vowels in the string:", vowel_count)



#Enter a string: Hello World
#Number of vowels in the string: 3
