def get_word_count(text):
    return len(text.split())


def get_character_frequency(text):
    frequency = {}
    for character in text.lower():
        if not character.isalpha():
            continue
        if not character in frequency:
            frequency[character] = 1
        else:
            frequency[character] += 1
    return frequency


def sort_by_num(items):
    return items["num"]


def sort_frequencies(frequencies):
    characters = []
    for name, count in frequencies.items():
        character = {"char": name,  "num": count}
        characters.append(character)
    characters.sort(reverse=True, key=sort_by_num)
    return characters