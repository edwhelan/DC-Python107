disect_this = input('Please enter a sentence: ')

#split the inputed value
split_sentence = disect_this.split()

results = {}

#Loop through all the words in the sentence
for word in split_sentence:
    print(word)
#   if the word is already in the dictonary
    if word in results:
        results[str(word)] = results[str(word)] + 1
#   if not add it with initial value of one
    else:
        results[str(word)] = 1

# print out results dictonary 
print(results)