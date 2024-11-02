# TODO  Напишите функцию count_letters

def count_letters(text_):
    dictionari_symbols = {}
    for symbols in text_:
        if symbols.isalpha():
            symbols = symbols.lower()
            if symbols in dictionari_symbols:
                dictionari_symbols[symbols] += 1
            else:
                dictionari_symbols[symbols] = 1

    return dictionari_symbols

# TODO Напишите функцию calculate_frequency




def calculate_frenquency(dictionari_symbols):
    all_symbols = sum(dictionari_symbols.values())
    frenquency = {}
    for symbol, kolichestvo in dictionari_symbols.items():
        frenquency[symbol] = round(kolichestvo / all_symbols, 2)

    return frenquency

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

kolichestvo_bukv = count_letters(main_str)
frequency = calculate_frenquency(kolichestvo_bukv)

for symbol, ch in frequency.items():
    print(f"{symbol}: {ch:.2f}")