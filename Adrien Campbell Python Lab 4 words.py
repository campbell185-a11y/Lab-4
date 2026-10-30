#Adrien Campbell Python Lab 4 words

def countWords(sentence):
    #splits the sentence into a list of words
    wordlist = sentence.split()
    # returns how many words are in the list by counting the length
    return len(wordlist)

userSentence = input("Enter a sentence: ")

numWords = countWords(userSentence)
print("The number of words in the sentence is: ", numWords)