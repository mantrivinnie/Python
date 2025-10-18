#  Program to count the frequency of words in a string. 

def word_frequency(text):
    # Convert to lowercase and split into words
    words = text.lower().split()
    freq = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1   # count occurrences
    
    return freq

# Take input
text = input("Enter a string: ")
result = word_frequency(text)

print("Word frequency:")
for word, count in result.items():
    print(f"{word}: {count}")

#Enter a string: This is a test This is simple
#Word frequency:
#this: 2
#is: 2
#a: 1
#test: 1
#simple: 1


#Alternate Code using collections.Counter
from collections import Counter

text = input("Enter a string: ")
words = text.lower().split()
freq = Counter(words)

print("Word frequency:")
print(freq)
