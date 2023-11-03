# Реализуйте класс StrExtension, описывающий набор функций для работы со строками.
# При создании экземпляра класс не должен принимать никаких аргументов.
# Класс StrExtension должен иметь три статических метода:
# remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные латинские буквы без учета регистра и возвращает полученный результат
# leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы, не являющиеся латинскими буквами, и возвращает полученный результат
# replace_all() — метод, который принимает три строковых аргумента string, chars и char,
#   заменяет в строке string все символы из chars на char с учетом регистра и возвращает полученный результат.

from re import sub, IGNORECASE


class StrExtension:

    @staticmethod
    def remove_vowels(s):
        pattern = r'[aeiouy]'
        return sub(pattern, '', s, flags=IGNORECASE)

    @staticmethod
    def leave_alpha(s):
        pattern = r'[^a-z]'
        return sub(pattern, '', s, flags=IGNORECASE)

    @staticmethod
    def replace_all(s, chars, char):
        return sub(fr'[{chars}]', char, s)


print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
