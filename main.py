def clean_a_list(word_list):
    clean_list = []
    for word in word_list:
        symbols = "~!@#$%^&*()_+|}{:?><,.\"}"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0 :
            clean_list.append(word)
    return clean_list


list = clean_a_list(['q!!!!', 'ok...', 'hi!'])
print(list)
      
