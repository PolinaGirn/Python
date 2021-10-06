"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш
url : хеш-url
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
from uuid import uuid4
import hashlib

salt = uuid4().hex

cash = {
    'https://github.com/': hashlib.sha256(salt.encode() + 'https://github.com/'.encode()).hexdigest()
}


def web_cashing(url):
    if url in cash:
        print('такая страница есть')
        return cash.get(url)
    else:
        cash[url] = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        print('страница добавлена')
        return cash.get(url)


web_cashing('https://github.com/')
web_cashing('https://tproger.ru/translations/')
web_cashing('https://www.asus.com/ru/')
web_cashing('https://tproger.ru/translations/')

for el in cash:
    print(f'{el} : {cash[el]}')




