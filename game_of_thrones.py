from sample import characters


print(len(characters.characters[1]['titles']))

#Print how many characters are dead
dead_count = 0
for person in characters.characters:
    if person['died'] != '':
        dead_count += 1

print(dead_count)
#Function to detect how many names start with ALPHAZED
def starts_with(letter):
    how_many_start_alphazed = 0
    for person in characters.characters:
        if person['name'].startswith(letter):
            how_many_start_alphazed += 1
    return how_many_start_alphazed


#Print how many characters start with the letter A
starts_with_alpha = starts_with('A')
print(starts_with_alpha)

#   print how many characters start with the letter Z
starts_with_zedd = starts_with('Z')
print(starts_with_zedd)


#detect who has the most titles and print that
current_most = ''
the_most_titles = 0
for person in characters.characters:
    if len(person['titles']) > the_most_titles:
        current_most = person['name']
        the_most_titles = len(person['titles'])
        
print('%s has the most titles with %d' % (current_most, the_most_titles))

#Detect if culture equals 'Valyrian'
valyrian_counter = 0
for person in characters.characters:
    if person['culture'] == 'Valyrian':
        valyrian_counter += 1

print('There are %d characters of the Valyrian culture.' % (valyrian_counter))

#Find out who plays the character 'Hot Pie'
actor = ''
for person in characters.characters:
    if person['name'] == 'Hot Pie':
        actor = person['playedBy'][0]

print('The character Hot Pie is played by %s' % (str(actor)))

#How many characters are not in the TV show
def is_not_in_tv_show():
    not_in_show = 0
    in_show = len(characters.characters)
    for person in characters.characters:
        if person['playedBy'] == ['']:
            not_in_show +=1         

    return 'There are this many chacters in the book but not in the show: %s' % (str(not_in_show))

with open('notintvshow.txt', 'w') as f:
    f.write(is_not_in_tv_show())


#Produce a list of characters with the last name 'Targaryen'

def is_in_house_targaryen():
    house_targaryen = []
    for person in characters.characters:
        if 'Targaryen' in person['name']:
            house_targaryen.append(person['name'])

    return str(house_targaryen)

with open('targaryen.txt', 'w') as f:
    f.write(is_in_house_targaryen())
