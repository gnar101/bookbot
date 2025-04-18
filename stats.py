def count_words(text):
     word_split = text.split()
     return len(word_split)

def character_count(text):
    character_split = list(text)
    characters = {}
    for character in character_split:
        character =character.lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sorted_list(text):
    character_counts = character_count(text)
    list_of_dicts = []
    for char, count in character_counts.items():
        if str.isalpha(char) == True:
            list_of_dicts.append({"char": char, "count": count})
    list_of_dicts.sort(reverse=True, key=lambda x: x["count"])
    
    return list_of_dicts

