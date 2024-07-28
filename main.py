# Преобразовать строку в нижний регистр
# Чтобы игнорировать различия между строчными и прописными буквами.
# Удалить из строки все неалфавитные символы:
# Чтобы учитывать только буквы (без пробелов, знаков препинания и т.д.).
# Сравнить строку с её перевернутой версией:
# Если строка равна своей перевернутой версии, то она является палиндромом.

import re


def is_palindrome(s):
    s = s.lower()
    s = re.sub(r'[^a-z]', '', s)
    return s == s[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome("Madam"))
print(is_palindrome("No lemon, no melon"))
