import sys
from stats import count_words, count_characters, sort_characters_by_frequency

def read_book_file(file_path):
    """Read and return the contents of a text file."""
    with open(file_path) as file:
        return file.read()

def main():
    # Check if file path is provided as command line argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_content = read_book_file(file_path)
    
    # Calculate statistics
    word_count = count_words(book_content)
    character_frequencies = sort_characters_by_frequency(count_characters(book_content))

    # Display results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Display only alphabetic characters
    for char_data in character_frequencies:
        if char_data["char"].isalpha():
            print(f"{char_data['char']}: {char_data['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()