# Reverse a string using slicing
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


# Reverse a string using loop
text = input("Enter a string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text   # prepend each character

print("Reversed string:", reversed_text)


# Reverse a string using reversed()
text = input("Enter a string: ")
reversed_text = "".join(reversed(text))
print("Reversed string:", reversed_text)
