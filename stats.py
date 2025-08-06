def get_num_words(book_text: str)-> int:
    count = 0
    for word in book_text.split():
        count += 1
    return count

def get_char_count(book_text: str)->dict:
    book_text_lower = book_text.lower()
    char_count = {}

    for char in book_text_lower:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    return char_count

def dict_listdict(d:dict)-> list:
    l = []
    for char in d:
        num = d[char]
        l.append({"char": char, "num": num})
    return l

def sort_on(items):
    return items["num"]

def sorted_listdict(items:dict)-> list:
    item_list = dict_listdict(items)
    item_list.sort(reverse=True, key=sort_on)
    return item_list