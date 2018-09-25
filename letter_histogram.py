disect_this = input('Please enter a word: ')

results = {}

#Loop through all letters
for letter in disect_this:
    print(letter)
#   if the letter is already in the dictonary
    if letter in results:
        results[str(letter)] = results[str(letter)] + 1
#   if not add it with initial value of one
    else:
        results[str(letter)] = 1

#print out results dictonary 
print(results)