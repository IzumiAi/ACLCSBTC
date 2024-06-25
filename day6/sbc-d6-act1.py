print("***Palindrome Checker***")
word = input("Enter a word: ")
word = word.lower().replace(" ", "")
if word == word[::-1]:
    print("\nNice! The word is a palindrome!")
else:
    print("\nSorry, the word is not a palindrome.")