# Adrien Campbell Python Lab 4 Pirate


def toPirate(sentence):
  # Dictionary mapping English words/phrases to Pirate phrases based on Lab instructions
  pirateDict = {
      "hello": "avast",
      "excuse": "arrr",
      "sir": "matey",
      "boy": "matey",
      "man": "matey",
      "madam": "proud beauty",
      "woman": "proud beauty",
      "officer": "foul blaggart",
      "the": "th'",
      "my": "me",
      "your": "yer",
      "is": "be",
      "are": "be",
      "kitchen": "galley",
      "hotel": "fleabag inn",
  }

  # Split the sentence into words
  words = sentence.split()
  translatedWords = []

  # Loop through each word and translate if it exists in our dictionary
  for word in words:
    # Convert word to lowercase for matching, keeping original if not found
    lowerWord = word.lower()
    if lowerWord in pirateDict:
      translatedWords.append(pirateDict[lowerWord])
    else:
      translatedWords.append(word)

  # Join the translated words back into a single sentence string
  pirateSentence = " ".join(translatedWords)
  return pirateSentence


# Test the function with a sample English sentence
englishSentence = input("Enter a sentence to be translated: ")
pirateTranslation = toPirate(englishSentence)

# Print the results
print("English sentence:", englishSentence)
print("Pirate translation:", pirateTranslation)