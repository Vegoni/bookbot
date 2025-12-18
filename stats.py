def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    # Create an empty dictionary to store character counts
    char_count = {}
    # Loop through each character in the text
    for char in text:
        # Convert character to lowercase to avoid duplicates
        lower_char = char.lower()
        # If character already exists in dictionary, increment count
        if lower_char in char_count:
            char_count[lower_char] += 1
        # Otherwise, add it to dictionary with count of 1
        else:
            char_count[lower_char] = 1
    return char_count


def sort_on(dict):
    return dict["num"]


def convert_to_sorted_list(char_dict):
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    # Sort from greatest to least using helper function
    char_list.sort(reverse=True, key=sort_on)
    return char_list
