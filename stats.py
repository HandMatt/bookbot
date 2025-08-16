def count_words(text):
    """Count the number of words in the given text."""
    return len(text.split())

def count_characters(text):
    """Count the frequency of each character in the text (case-insensitive)."""
    character_counts = {}

    for char in text.lower():
        character_counts[char] = character_counts.get(char, 0) + 1

    return character_counts

def sort_characters_by_frequency(character_counts):
    """Sort characters by their frequency in descending order."""
    # Convert dictionary to list of dictionaries for sorting
    character_list = [
        {"char": char, "num": count} 
        for char, count in character_counts.items()
    ]
    
    # Sort by frequency (descending)
    character_list.sort(reverse=True, key=lambda item: item["num"])
    
    return character_list
