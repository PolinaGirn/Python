"""
Задание 7.
Задание на закрепление навыков работы с деком
В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'
Но могут быть и такие палиндромы, как 'молоко делили ледоколом'
Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
Примечание:
Вам не нужно писать код с нуля. Вам нужно доработать пример с урока.
"""


# дек из урока
class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


#####################################################


def pal_checker(string):
    str_copy = DequeClass()

    for el in string:
        if el != ' ':                      # добавила только эту строку
            str_copy.add_to_rear(el)

    still_equal = True

    while str_copy.size() > 1 and still_equal:
        first = str_copy.remove_from_front()
        last = str_copy.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


# немного украсила вывод
text = 'молоко делили ледоколом'
print(text, ' - ',  pal_checker(text))
