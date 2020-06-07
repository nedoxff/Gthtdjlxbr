english = ['`', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
           ';', "'", 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '`', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
           '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.']
russian = ['Ё', 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д',
           'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', 'ё', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з',
           'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю']


def toEnglish(prompt):
    new_string = list()
    for j in prompt:
        if j in russian:
            new_string.append(english[russian.index(j)])
        else:
            new_string.append(j)
    return "".join(new_string)


def toRussian(prompt):
    new_string = list()
    for j in prompt:
        if j in english:
            new_string.append(russian[english.index(j)])
        else:
            new_string.append(j)
    return "".join(new_string)

if __name__ == "__main__":
    choose = ""
    enter_phrase = ""
    error = ""
    result = ""
    language = input("Language/Язык:\n1.) Русский\n2.) English\n: ")
    if language == "1":
        choose = "Введите тип перевода:\n1.) из русского в английский\n2.) из английского в русский\nВыбор: "
        enter_phrase = "Введите фразу: "
        error = "Неизвестный выбор."
        result = "Результат: "
    elif language == "2":
        choose = "Choose the type of translation:\n1.) from russian to english\n2.) from english to russian\nChoice: "
        enter_phrase = "Enter phrase: "
        error = "Unknown Choice."
        result = "Result: "
    i = input(choose)
    if i == "1":
        k = input(enter_phrase)
        print(result + toEnglish(k))
    elif i == "2":
        k = input(enter_phrase)
        print(result + toRussian(k))
    else:
        print(error)
        exit(1)
