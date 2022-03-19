# https://stackoverflow.com/questions/19709026/how-can-i-list-all-available-windows-locales-in-python-console
# https://stackoverflow.com/questions/53320311/how-do-i-find-all-available-locales-in-python
#
import locale
import re
from collections import defaultdict

#locale._print_locale()
# not very useful info.

def parse_locale_with_regex():
    for name in locale.locale_alias.values():
        # The "(?:){0,1}" pattern is for non-capturing group
        m = re.match('(\w\w)_(\w\w)(?:\.+(.+)){0,1}(?:@(\w+)){0,1}', name)
        if m:
            record = dict(zip(('lang', 'country', 'encoding', 'script'), m.groups()))
            print(record)

def parse_locale_manually():
    # Example value: zh_TW.big5 ir tt_RU.UTF-8@iqtelif
    locales = list(locale.locale_alias.values())
    locales.sort()
    summary_counts = defaultdict(set)
    for locale_str in locales:
        #print(locale_str)

        lang_country, *encoding_list = locale_str.split('.', 2)
        lang, *country_list = lang_country.split('_', 2)

        # Skip lang that does not have two chars
        if len(lang) < 2:
            continue

        record = {'lang': lang}
        summary_counts['lang'].add(lang)

        if len(country_list) > 0:
            record['country'] = country_list[0]
            summary_counts['country'].add(record['country'])

        if len(encoding_list) > 0:
            encoding, *script_list = encoding_list[0].split('@', 2)
            record['encoding'] = encoding
            summary_counts['encoding'].add(record['encoding'])

            if len(script_list) > 0:
                record['script'] = script_list[0]
                summary_counts['script'].add(record['script'])

        print(record)

    print("===Summary counts")
    print(f"Language count: {len(summary_counts['lang'])}")
    print(f"Country count: {len(summary_counts['country'])}")
    print(f"Encoding count: {len(summary_counts['encoding'])}")
    print(f"Script count: {len(summary_counts['script'])}")

    # Output by Python 3.9.10
    # ===Summary counts
    # Language count: 203
    # Country count: 156
    # Encoding count: 46
    # Script count: 4


parse_locale_with_regex()
