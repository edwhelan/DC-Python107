disect_this = input('Please enter a sentence: ')

#split the inputed value
split_sentence = disect_this.split()

results = {}

#Loop through all the words in the sentence
for word in split_sentence:
#   if the word is already in the dictonary
    if word in results:
        results[str(word)] = results[str(word)] + 1
#   if not add it with initial value of one
    else:
        results[str(word)] = 1

# print out the top 3 results from inputed dictonary

### Set 3 counters for order of values
number_1 = 0
number_2 = 0
number_3 = 0
### set first second and third place
third_place = ''
second_place = ''
first_place = ''

### loop through and check for values
for entries in results:
    if results[entries] > number_1:
        number_3 = number_2
        third_place = second_place
        number_2 = number_1
        second_place = first_place
        number_1 = results[entries]
        first_place = entries +': '+ str(results[entries])
    elif results[entries] > number_2 and results[entries] < number_1:
        number_3 = number_2
        third_place = second_place
        second_place = entries +': '+ str(results[entries])
    elif results[entries] > number_3 and results[entries] < number_2:
        number_3 = results[entries]
        third_place = entries + ': '+ str(results[entries])
    else:
        pass
    
 
print('The top three words are: ')
print(first_place)
print(second_place)
print(third_place)
