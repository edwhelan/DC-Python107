from sample import characters


print(characters.characters[1]['died'])


dead_count = 0
for person in characters.characters:
    if person['died'] != '':
        dead_count += 1

print(dead_count)

how_many_start_alpha = 0
for person in characters.characters:
    if person['name'].startswith('A'):
        how_many_start_alpha += 1

print(how_many_start_alpha)

how_many_start_zebra = 0
for person in characters.characters:
    if person['name'].startswith('Z'):
        how_many_start_zebra += 1

print(how_many_start_zebra)