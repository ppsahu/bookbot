def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        word_count = count_words(file_content)
        character_count = count_characters(file_content)
        chaacter_sort = sort(character_count)

def count_words(file):
    word_list = file.split()
    return len(word_list)

def count_characters(file):
    lower_case = file.lower()
    word_dict = {}
    for word in lower_case:
        for chr in word:
            if chr in word_dict:
                word_dict[chr] += 1
            else:
                word_dict[chr] = 1
    return word_dict

def sort_on(word_dict):
    return word_dict["num"]

def sort(character_count):
    character_count = character_count.items()
    dict_to_list = []
    for item in character_count:
        temp_dict = {}
        temp_dict["character"] = item[0]
        temp_dict["num"] = item[1]
        dict_to_list.append(temp_dict)

    dict_to_list.sort(reverse=True, key=sort_on)
    print(dict_to_list)

main()