"""Requirements:
    pip install requests, lxml, cssselect

    На странице jetlend.ru всего 30 видов различных тегов. Из них 19 тегов с атрибутами.
    Общее количество всех встречающихся тегов: 965. Из них 886 тегов с атрибутами.
"""


import requests
from lxml import html


url: str = 'https://jetlend.ru/borrower/'
web_page = requests.get(url)
content = html.fromstring(web_page.content)
elements = content.cssselect('*')

all_tags: list = [el.tag for el in elements]
tags_with_attrib: list = [el.tag for el in elements if el.attrib]

print(f'\nНа странице jetlend.ru всего {len(set(all_tags))} видов различных тегов.'
      f' Из них {len(set(tags_with_attrib))} тегов с атрибутами.')
print(f'Общее количество всех встречающихся тегов: {len(all_tags)}.'
      f' Из них {len(tags_with_attrib)} тегов с атрибутами.\n')

