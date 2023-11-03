# Реализуйте класс DateFormatter, экземпляры которого позволяют преобразовывать даты
# в формат определенной страны из таблицы выше.
# При создании экземпляра класс должен принимать один аргумент:
# country_code — код страны
# Экземпляр класса DateFormatter должен являться вызываемым объектом и принимать один аргумент:
# d — дата (тип date)
# Экземпляр класса DateFormatter должен возвращать строку с датой d в формате страны с кодом country_code.

class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        __data = {
            "ru": r"%d.%m.%Y",
            "us": r"%m-%d-%Y",
            "ca": r"%Y-%m-%d",
            "br": r"%d/%m/%Y",
            "fr": r"%d.%m.%Y",
            "pt": r"%d-%m-%Y"
        }
        return d.strftime(__data[self.country_code])