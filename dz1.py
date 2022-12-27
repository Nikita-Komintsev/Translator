import tkinter as tk
import re
import tkinter.messagebox as mb
import sys

class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
def starorus(result):
    result = str(result)
    new_string = ''
    result = list(result)
    print(result)
    if len(result) == 3:
        f100 = False
        f10 = False
        for num in result:
            if f100 is False:
                if num == '1':
                    new_string += "Ρ"
                    f100 = True
                elif num == '2':
                    new_string += "С"
                    f100 = True
                elif num == '3':
                    new_string += "Т"
                    f100 = True
                elif num == '4':
                    new_string += "У"
                    f100 = True
                elif num == '5':
                    new_string += "Ф"
                    f100 = True
                elif num == '6':
                    new_string += "Х"
                    f100 = True
                elif num == '7':
                    new_string += "Ѱ"
                    f100 = True
                elif num == '8':
                    new_string += "Ѡ"
                    f100 = True
                elif num == '9':
                    new_string += "Ц"
                    f100 = True
            elif f100 and f10 is False:
                if num == '1':
                    new_string += "Ι"
                    f10 = True
                elif num == '2':
                    new_string += "К"
                    f10 = True
                elif num == '3':
                    new_string += "Л"
                    f10 = True
                elif num == '4':
                    new_string += "М"
                    f10 = True
                elif num == '5':
                    new_string += "Н"
                    f10 = True
                elif num == '6':
                    new_string += "Ѯ"
                    f10 = True
                elif num == '7':
                    new_string += "O"
                    f10 = True
                elif num == '8':
                    new_string += "П"
                    f10 = True
                elif num == '9':
                    new_string += "Ч"
                    f10 = True
            elif f100 and f10:
                if num == '0':
                    new_string += "0"
                if num == '1':
                    new_string += "А"
                if num == '2':
                    new_string += "В"
                if num == '3':
                    new_string += "Г"
                if num == '4':
                    new_string += "Δ"
                if num == '5':
                    new_string += "Е"
                if num == '6':
                    new_string += "S"
                if num == '7':
                    new_string += "З"
                if num == '8':
                    new_string += "И"
                if num == '9':
                    new_string += "Ѳ"
    if len(result) == 2:
        f10 = False
        for num in result:
            if f10 is False:
                if num == '1':
                    new_string += "Ι"
                    f10 = True
                elif num == '2':
                    new_string += "К"
                    f10 = True
                elif num == '3':
                    new_string += "Л"
                    f10 = True
                elif num == '4':
                    new_string += "М"
                    f10 = True
                elif num == '5':
                    new_string += "Н"
                    f10 = True
                elif num == '6':
                    new_string += "Ѯ"
                    f10 = True
                elif num == '7':
                    new_string += "O"
                    f10 = True
                elif num == '8':
                    new_string += "П"
                    f10 = True
                elif num == '9':
                    new_string += "Ч"
                    f10 = True
            else:
                if num == '0':
                    new_string += "0"
                if num == '1':
                    new_string += "А"
                if num == '2':
                    new_string += "В"
                if num == '3':
                    new_string += "Г"
                if num == '4':
                    new_string += "Δ"
                if num == '5':
                    new_string += "Е"
                if num == '6':
                    new_string += "S"
                if num == '7':
                    new_string += "З"
                if num == '8':
                    new_string += "И"
                if num == '9':
                    new_string += "Ѳ"
    if len(result) == 1:
        for num in result:
            if num == '0':
                new_string += "0"
            if num == '1':
                new_string += "А"
            if num == '2':
                new_string += "В"
            if num == '3':
                new_string += "Г"
            if num == '4':
                new_string += "Δ"
            if num == '5':
                new_string += "Е"
            if num == '6':
                new_string += "S"
            if num == '7':
                new_string += "З"
            if num == '8':
                new_string += "И"
            if num == '9':
                new_string += "Ѳ"
    return new_string
def answer(result):
    text_box.insert(tk.END, "Результат = " + str(result) + "\n")
    text_box.insert(tk.END, "Римские = " + str(py_solution().int_to_Roman(result)) + "\n")
    #text_box.insert(tk.END, "Старорусские = " + starorus(result) + "\n")

def hundreds(word, result):
    if word == "einhundert":
        result+=100
    elif word == "zweihundert":
        result+=200
    elif word == "dreihundert":
        result+=300
    elif word == "vierhundert":
        result+=400
    elif word == "funfhundert":
        result+=500
    elif word == "sechshundert":
        result+=600
    elif word == "siebenhundert":
        result+=700
    elif word == "achthundert":
        result+=800
    elif word == "neunhundert":
        result+=900
    elif "und" in word:
        print("UND после сотен")
        mb.showinfo("Ошибка", "UND после сотен")
        result = -1
    else:
        print("Неправильное написание сотен")
        mb.showinfo("Ошибка",  "Неправильное написание сотен")
        result = -1
    return result
#20-90
def tens(word, result):
    if word == "zwanzig":
        result+=20
    elif word == "dreizig":
        result+=30
    elif word == "vierzig":
        result+=40
    elif word == "funfzig":
        result+=50
    elif word == "sechzig":
        result+=60
    elif word == "siebzig":
        result+=70
    elif word == "achtzig":
        result+=80
    elif word == "neunzig":
        result+=90
    elif "zigund" in word:
        print("UND после десяток")
        mb.showinfo("Ошибка", "UND после десяток")
        result = -1
    else:
        print("Неправильное написание десяток")
        mb.showinfo("Ошибка", "Неправильное написание десяток")
        result = -1
    return result
#10,13-19
def tens_11_19(word,result):
    if word == "elf":
        result += 11
    elif word == "zwolf":
        result += 12
    elif word == "dreizehn":
        result+=13
    elif word == "vierzehn":
        result+=14
    elif word == "funfzehn":
        result+=15
    elif word == "sechzehn":
        result+=16
    elif word == "siebzehn":
        result+=17
    elif word == "achtzehn":
        result+=18
    elif word == "neunzehn":
        result+=19
    elif ("zehnund" in word) or ("elfund" in word) or ("zwolfund" in word) or ("zehnund" in word):
        print("UND после 11-19")
        mb.showinfo("Ошибка", "Непрвильное написание")
        result = -1
    else:
        print("Ошибка в слове - ", word)
        mb.showinfo("Ошибка", "Ошибка в слове - " + word)
        result = -1
    return result
def units(word,result):
    if word == "eins":
        result+=1
    elif word == "zwei":
        result+=2
    elif word == "drei":
        result+=3
    elif word == "vier":
        result+=4
    elif word == "funf":
        result+=5
    elif word == "sechs":
        result+=6
    elif word == "sieben":
        result+=7
    elif word == "acht":
        result += 8
    elif word == "neun":
        result += 9
    elif word == "zehn":
        result+=10
    else:
        print("Ошибка в единицах - ", word)
        mb.showinfo("Ошибка", "Ошибка в единицах - " + word)
        result = -1
    return result
def units_und(word, result):
    if word == "einund":
        result+=1
    elif word == "zweiund":
        result+=2
    elif word == "dreiund":
        result+=3
    elif word == "vierund":
        result+=4
    elif word == "funfund":
        result+=5
    elif word == "sechsund":
        result+=6
    elif word == "siebenund":
        result+=7
    elif word == "achtund":
        result += 8
    elif word == "neunund":
        result += 9
    elif "undund" in word:
        print("UND после UND")
        mb.showinfo("Ошибка", "UND после UND")
        result = -1
    else:
        print("Ошибка в слове - ", word)
        mb.showinfo("Ошибка", "Ошибка в слове - " + word)
        result = -1
    return result

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('500x400')

    label = tk.Label(text="Число прописью").pack(padx=15, pady=15)
    entry_string = tk.Entry(window, width=60)
    entry_string.pack()

    def Submit():
        text_box.delete(0.0, tk.END)

        units_flag = False
        tens_11_19_flag = False
        tens_flag = False
        units_und_flag = False
        hundreds_flag = False
        join_hundert_flag = False
        flag_error = False
        result = 0
        str = entry_string.get()

        if " hundert" in str:
            str = re.sub(" +hundert", "hundert", str)
            join_hundert_flag = True

        str = re.sub(" +und", "und", str)
        lst = str.split()

        for word in lst:
            # ошибка сотни после UND
            if "undhundert" in word:
                print("После UND должны быть десятки")
                mb.showinfo("Ошибка", "После UND должны быть десятки")
                flag_error = True
                break
            if "hundert" in word and units_flag == False and tens_11_19_flag == False and tens_flag == False and units_und_flag == False and hundreds_flag == False:
                result = hundreds(word, result)
                hundreds_flag = True
                if result == -1:
                    flag_error = True
                    break
            # ошибки после сотен
            elif "hundert" in word and hundreds_flag:
                print("Повторение сотен")
                mb.showinfo("Ошибка", "Повторение сотен")
                flag_error = True
                break

            elif "zig" in word and units_flag == False and tens_11_19_flag == False and tens_flag == False:
                result = tens(word, result)
                tens_flag = True
                if result == -1:
                    flag_error = True
                    break
            # ошибки после десяток
            elif "hundert" in word and tens_flag:
                print("Сотни после десяток")
                mb.showinfo("Ошибка", "Сотни после десяток")
                flag_error = True
                break
            elif "zig" in word and tens_flag:
                print("Десятки после десяток")
                mb.showinfo("Ошибка", "Десятки после десяток")
                flag_error = True
                break
            elif ("zehn" in word or "elf" in word or "zwolf" in word) and tens_flag:
                print("Неправильный состав числа")
                mb.showinfo("Ошибка", "Неправильный состав числа")
                flag_error = True
                break
            elif (word == "eins" or word == "zwei" or word == "drei" or word == "vier" or word == "funf" or word == "sechs" or word == "sieben" or word == "acht" or word == "neun" or word == "zehn" or word == "einund" or word == "zweiund" or word == "dreiund" or word == "vierund" or word == "funfund" or word == "sechsund" or word == "siebenund" or word == "achtund" or word == "neunund") and tens_flag:
                print("Единицы после десяток")
                mb.showinfo("Ошибка", "Единицы после десяток")
                flag_error = True
                break

            # 11 - 19
            elif (word == "dreizehn" or word == "vierzehn" or word == "funfzehn" or word == "sechzehn" or word == "siebzehn" or word == "achtzehn" or word == "neunzehn" or "elf" in word or "zwolf" in word or "zehnund" in word) and units_flag == False and tens_11_19_flag == False and tens_flag == False and units_und_flag == False:
                result = tens_11_19(word, result)
                tens_11_19_flag = True
                if result == -1:
                    flag_error = True
                    break

            # ошибки после 10-19
            elif (word == "eins" or word == "zwei" or word == "drei" or word == "vier" or word == "funf" or word == "sechs" or word == "sieben" or word == "acht" or word == "neun" or word == "einund" or word == "zweiund" or word == "dreiund" or word == "vierund" or word == "funfund" or word == "sechsund" or word == "siebenund" or word == "achtund" or word == "neunund") and tens_11_19_flag:
                print("Единицы после цифр 11-19")
                mb.showinfo("Ошибка", "Неправильный состав числа")
                flag_error = True
                break
            elif "zig" in word and tens_11_19_flag:
                print("Десятки после цифр 11-19")
                mb.showinfo("Ошибка", "Неправильный состав числа")
                flag_error = True
                break
            elif ("zehn" in word or "elf" in word or "zwolf" in word) and tens_11_19_flag:
                print("Разрядность 11-19 после цифр 11-19")
                mb.showinfo("Ошибка", "Неправильный состав числа")
                flag_error = True
                break
            elif "hundert" in word and tens_11_19_flag:
                print("Сотни после цифр 11-19")
                mb.showinfo("Ошибка", "Неправильный состав числа")
                flag_error = True
                break

            # 1 - 9
            elif (word == "eins" or word == "zwei" or word == "drei" or word == "vier" or word == "funf" or word == "sechs" or word == "sieben" or word == "acht" or word == "neun" or word == "zehn") and units_flag == False and tens_11_19_flag == False and tens_flag == False and units_und_flag == False:
                result = units(word, result)
                units_flag = True
                if result == -1:
                    flag_error = True
                    break

            # ошибка после единиц
            elif (word == "eins" or word == "zwei" or word == "drei" or word == "vier" or word == "funf" or word == "sechs" or word == "sieben" or word == "acht" or word == "neun" or word == "einund" or word == "zweiund" or word == "dreiund" or word == "vierund" or word == "funfund" or word == "sechsund" or word == "siebenund" or word == "achtund" or word == "neunund") and units_flag:
                print("Единицы после единиц")
                mb.showinfo("Ошибка", "Единицы после единиц")
                flag_error = True
                break
            elif (word == "einhundert" or word == "zweihundert" or word == "dreihundert" or word == "vierhundert" or word == "funfhundert" or word == "sechshundert" or word == "siebenhundert" or word == "achthundert" or word == "neunhundert") and units_flag and join_hundert_flag:
                print("Единицы после единиц")
                mb.showinfo("Ошибка", "Единицы после единиц")
                flag_error = True
                break
            elif "zig" in word and units_flag:
                print("Между единицами и десятками должен быть UND")
                mb.showinfo("Ошибка", "Между единицами и десятками должен быть UND")
                flag_error = True
                break
            elif ("zehn" in word or "elf" in word or "zwolf" in word) and units_flag:
                print("Разрядность 11-19 после единиц")
                mb.showinfo("Ошибка", "Неправильный состав числа")
                flag_error = True
                break
            elif (word == "einhundert" or word == "zweihundert" or word == "dreihundert" or word == "vierhundert" or word == "funfhundert" or word == "sechshundert" or word == "siebenhundert" or word == "achthundert" or word == "neunhundert") and units_flag and join_hundert_flag == False:
                print("Сотни после единиц")
                mb.showinfo("Ошибка", "Сотни после единиц")
                flag_error = True
                break

            # und 1 - 9 перед десятками
            elif "und" in word and word in lst[-1]:
                print("UND должен быть между единцами и десятками")
                mb.showinfo("Ошибка", "UND должен быть между единцами и десятками")
                flag_error = True
                break
            elif (word == "einund" or word == "zweiund" or word == "dreiund" or word == "vierund" or word == "funfund" or word == "sechsund" or word == "siebenund" or word == "achtund" or word == "neunund") and units_und_flag == False:
                result = units_und(word, result)
                units_und_flag = True
                if result == -1:
                    flag_error = True
                    break

            # ошибки und
            elif (word == "eins" or word == "zwei" or word == "drei" or word == "vier" or word == "funf" or word == "sechs" or word == "sieben" or word == "acht" or word == "neun") and units_und_flag:
                print("UND должен быть между единцами и десятками")
                mb.showinfo("Ошибка", "UND должен быть между единцами и десятками")
                flag_error = True
                break
            elif ("zehn" in word or "elf" in word or "zwolf" in word) and units_und_flag:
                print("Разрядность 11-19 после UND")
                mb.showinfo("Ошибка", "Неправильный состав числа")
                flag_error = True
                break
            elif "hundert" in word and units_und_flag:
                print("UND должен быть между единцами и десятками")
                mb.showinfo("Ошибка", "UND должен быть между единцами и десятками")
                flag_error = True
                break
            elif (word == "einund" or word == "zweiund" or word == "dreiund" or word == "vierund" or word == "funfund" or word == "sechsund" or word == "siebenund" or word == "achtund" or word == "neunund") and units_und_flag:
                print("UND должен быть между единцами и десятками")
                mb.showinfo("Ошибка", "UND должен быть между единцами и десятками")
                flag_error = True
                break
            elif word =="und":
                print("Число не может начинаться с UND")
                mb.showinfo("Ошибка", "Число не может начинаться с UND")
                flag_error = True
                break
            else:
                if "hundert" in word:
                    word = word.replace('hundert','')
                elif "und" in word:
                    word = word.replace('und', '')
                print("Ошибка в слове - ", word)
                mb.showinfo("Ошибка",  "Ошибка в слове - " + word)
                flag_error = True
                break
        if not flag_error:
            answer(result)

    btn_submit = tk.Button(text="Подтвердить", command=Submit)
    btn_submit.pack(padx=10, pady=10)

    text_box = tk.Text(window)
    text_box.pack()

    window.mainloop()