# https://stackoverflow.com/questions/19709026/how-can-i-list-all-available-windows-locales-in-python-console
# https://stackoverflow.com/questions/53320311/how-do-i-find-all-available-locales-in-python
#
import locale
locales = list(locale.locale_alias.keys())
locales.sort()
for locale in locales:
    print(locale)
print(f"Total {len(locales)} locales found.")