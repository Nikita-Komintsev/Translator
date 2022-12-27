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

def answer(result):
    text_box.insert(tk.END, "Результат = " + str(result) + "\n")
    text_box.insert(tk.END, "Римские = " + str(py_solution().int_to_Roman(result)) + "\n")

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
    elif "hundertund" in word:
        print("UND после сотен")
        mb.showinfo("Ошибка", "UND после разряда сотен")
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
        mb.showinfo("Ошибка", "UND после разряда десяток")
        result = -1
    else:
        print("Неправильное написание десяток")
        mb.showinfo("Ошибка", "Неправильное написание десяток")
        result = -1
    return result
#11-19
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
        print("UND после разряда 11-19")
        mb.showinfo("Ошибка", "UND после разряда 11-19")
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
        print("Ошибка в разряде единиц - ", word)
        mb.showinfo("Ошибка", "Ошибка в разряде единиц - " + word)
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
                print("После UND должен быть десятичный разряд")
                mb.showinfo("Ошибка", "После UND должен быть десятичный разряд")
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
                print("Сотни после десятичного разряда")
                mb.showinfo("Ошибка", "Сотни после десятичного разряда")
                flag_error = True
                break
            elif "zig" in word and tens_flag:
                print("Десятичный разряд после десятичного разряда")
                mb.showinfo("Ошибка", "Десятичный разряд после десятичного разряда")
                flag_error = True
                break
            elif ("zehn" in word or "elf" in word or "zwolf" in word) and tens_flag:
                print("Разрядность 11-19 после десятичного разряда")
                mb.showinfo("Ошибка", "Разрядность 11-19 после десятичного разряда")
                flag_error = True
                break
            elif (word == "eins" or word == "zwei" or word == "drei" or word == "vier" or word == "funf" or word == "sechs" or word == "sieben" or word == "acht" or word == "neun" or word == "zehn" or word == "einund" or word == "zweiund" or word == "dreiund" or word == "vierund" or word == "funfund" or word == "sechsund" or word == "siebenund" or word == "achtund" or word == "neunund") and tens_flag:
                print("Единичный разряд после десятичного разряда")
                mb.showinfo("Ошибка", "Единичный разряд после десятичного разряда")
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
                print("Единичный разряд после цифр 11-19")
                mb.showinfo("Ошибка", "Единичный разряд после цифр 11-19")
                flag_error = True
                break
            elif "zig" in word and tens_11_19_flag:
                print("Десятичный разряд после цифр 11-19")
                mb.showinfo("Ошибка", "Десятичный разряд после цифр 11-19")
                flag_error = True
                break
            elif ("zehn" in word or "elf" in word or "zwolf" in word) and tens_11_19_flag:
                print("Разрядность 11-19 после цифр 11-19")
                mb.showinfo("Ошибка", "Разрядность 11-19 после цифр 11-19")
                flag_error = True
                break
            elif "hundert" in word and tens_11_19_flag:
                print("Сотни после цифр 11-19")
                mb.showinfo("Ошибка", "Сотни после цифр 11-19")
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
                print("Единичный разряд после единичного разряда")
                mb.showinfo("Ошибка", "Единичный разряд после единичного разряда")
                flag_error = True
                break
            elif (word == "einhundert" or word == "zweihundert" or word == "dreihundert" or word == "vierhundert" or word == "funfhundert" or word == "sechshundert" or word == "siebenhundert" or word == "achthundert" or word == "neunhundert") and units_flag and join_hundert_flag:
                print("Единичный разряд после единичного разряда")
                mb.showinfo("Ошибка", "Единичный разряд после единичного разряда")
                flag_error = True
                break
            elif "zig" in word and units_flag:
                print("Между единицами и десятками должен быть UND")
                mb.showinfo("Ошибка", "Между единицами и десятками должен быть UND")
                flag_error = True
                break
            elif ("zehn" in word or "elf" in word or "zwolf" in word) and units_flag:
                print("Разрядность 11-19 после единиц")
                mb.showinfo("Ошибка", "Разрядность 11-19 после единичного разряда")
                flag_error = True
                break
            elif (word == "einhundert" or word == "zweihundert" or word == "dreihundert" or word == "vierhundert" or word == "funfhundert" or word == "sechshundert" or word == "siebenhundert" or word == "achthundert" or word == "neunhundert") and units_flag and join_hundert_flag == False:
                print("Сотни после единичного разряда")
                mb.showinfo("Ошибка", "Сотни после единичного разряда")
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
                mb.showinfo("Ошибка", "Разрядность 11-19 после UND")
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