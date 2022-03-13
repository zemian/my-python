# https://stackoverflow.com/questions/19709026/how-can-i-list-all-available-windows-locales-in-python-console
# https://stackoverflow.com/questions/53320311/how-do-i-find-all-available-locales-in-python
#
import locale
locales = locale.locale_alias
for (name, locale) in locales.items():
    print(name, locale)
