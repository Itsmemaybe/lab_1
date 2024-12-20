# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    dict_letters = {}
    for let in text:
        if let.isalpha():
            if dict_letters.get(let) == None:
                dict_letters[let] = 1
            else:
                dict_letters[let] += 1

    return dict_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_letters):
    frequency_dict = {}
    all_letters = sum(list(dict_letters.values()))
    for let in list(dict_letters.keys()):
        frequency_dict[let] = dict_letters[let] / all_letters
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
result = calculate_frequency(count_letters(main_str))
for i in result: print(f"{i}: {format(result[i], '.2f')}")