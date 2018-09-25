from sample import characters


print(len(characters.characters[1]['titles']))

#Print how many characters are dead
dead_count = 0
for person in characters.characters:
    if person['died'] != '':
        dead_count += 1

print(dead_count)
#Print how many characters start with the letter A
how_many_start_alpha = 0
for person in characters.characters:
    if person['name'].startswith('A'):
        how_many_start_alpha += 1

print(how_many_start_alpha)


#print how many characters start with the letter Z
how_many_start_zebra = 0
for person in characters.characters:
    if person['name'].startswith('Z'):
        how_many_start_zebra += 1

print(how_many_start_zebra)

#detect who has the most titles and print that
current_most = ''
the_most_titles = 0
for person in characters.characters:
    if len(person['titles']) > the_most_titles:
        current_most = person['name']
        the_most_titles = len(person['titles'])
        
print('%s has the most titles with %d' % (current_most, the_most_titles))