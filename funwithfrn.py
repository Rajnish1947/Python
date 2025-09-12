sentence = input("Enter your sentence: ")
print("Your sentence: " + sentence)

word1 = input("Enter the word you want to replace: ")
word2 = input("Enter the new word to use instead: ")

# Replace word1 with word2 in the sentence
updated_sentence = sentence.replace(word1, word2)
print("Updated sentence: " + updated_sentence)
