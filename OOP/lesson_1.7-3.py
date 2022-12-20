from string import ascii_lowercase, digits
import re

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    def check_card_number(number):
        return bool(re.search("^\d{4}-\d{4}-\d{4}-\d{4}$", number))
        
    
    @classmethod
    def check_name(cls, name):
        return bool(re.search(f"^[{cls.CHARS_FOR_NAME}]*\s[{cls.CHARS_FOR_NAME}]*$", name))



is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(CardCheck.CHARS_FOR_NAME)
print(is_number, is_name)