from collections import Counter

def number_words(text):
    return len(text.split())

def count_characters(text):
    ch_list = [p.lower() for p in text]
    cc = Counter(ch_list)
    return dict(cc)

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    list_dicts = []
    for key in dict:
        if not key.isalpha():
            continue
        value = dict[key]
        list_dicts.append({"letter":key,"num":value})
    list_dicts.sort(reverse=True, key=sort_on)

    return list_dicts


