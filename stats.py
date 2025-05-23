def count_words_in_book(text):
    return len(text.split())

def count_chars_in_text(text):
    char_count = {}
    for word in text:
        for c in word:
            c_ignore = c.lower()
            if c_ignore in char_count:
                char_count[c_ignore] += 1
            else:
                char_count[c_ignore] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def create_list(char_dict):
    sorted_list = []
    for key in char_dict:
        dict_entry = {}
        dict_entry["char"] = key
        dict_entry["num"] = char_dict[key]
        sorted_list.append(dict_entry)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list