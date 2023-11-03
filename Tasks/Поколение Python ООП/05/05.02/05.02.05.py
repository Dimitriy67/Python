# Реализуйте класс PhoneNumber, описывающий телефонный номер.
# При создании экземпляра класс должен принимать один аргумент:
# phone_number — телефонный номер, представляющий строку из десяти цифр в одном из следующих форматов:
# dddddddddd
# ddd ddd dddd
# Экземпляр класса PhoneNumber должен иметь следующее формальное строковое представление:
# PhoneNumber('<телефонный номер в формате dddddddddd>')
# И следующее неформальное строковое представление:
# <телефонный номер в формате (ddd) ddd-dddd>

class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number.replace(' ', '')

    def __str__(self):
        return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'

    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"
