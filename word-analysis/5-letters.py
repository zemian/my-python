def print_5letters_list():
    """
    The source of word list is from https://github.com/dwyl/english-words.git
    """
    file = '/Users/zemian/my-web/english-words/words_alpha.txt'
    words = open(file, 'r').read().split('\n')
    #print(len(words)) # count = 370103 total

    # 5 letters word count = 15918
    for w in words:
        if len(w) == 5:
            print(w)

def print_most_vowels_list():
    vowels = list('aeiou')
    file = '/Users/zemian/my-web/wordle-API/analysis/5-letters-words.txt'
    words = open(file, 'r').read().split('\n')
    for w in words:
        w = w.lower()
        w_vowels = [v for v in vowels if v in w]
        if len(w_vowels) == 4:
            print(w)

def print_most_frequent_list():
    """
    Count the most frequent of each letters in list
    Sample: {'a': 8392, 'e': 7800, 's': 6537, 'o': 5219, 'r': 5143, 'i': 5067, 'l': 4246, 't': 4189, 'n': 4043, 'u': 3361, 'd': 2811, 'c': 2744, 'y': 2521, 'm': 2494, 'p': 2299, 'h': 2284, 'b': 2089, 'g': 1971, 'k': 1743, 'f': 1238, 'w': 1171, 'v': 878, 'z': 474, 'j': 376, 'x': 361, 'q': 139}
    """
    letters_freq = {}
    file = '/Users/zemian/my-web/wordle-API/analysis/5-letters-words.txt'
    words = open(file, 'r').read().split('\n')
    for w in words:
        w = w.lower()
        for c in w:
            if c in letters_freq:
                letters_freq[c] += 1
            else:
                letters_freq[c] = 1

    letters_freq = dict(reversed(sorted(letters_freq.items(), key=lambda item: item[1])))
    print(letters_freq)

def print_high_frequency_list():
    """
    Find words with most high frequency occurance letters
    Sample: {'a': 8392, 'e': 7800, 's': 6537, 'o': 5219, 'r': 5143, 'i': 5067, 'l': 4246, 't': 4189, 'n': 4043, 'u': 3361, 'd': 2811, 'c': 2744, 'y': 2521, 'm': 2494, 'p': 2299, 'h': 2284, 'b': 2089}
    """
    allowed_letters = list('aesoriltnudcymphb')
    file = '/Users/zemian/my-web/wordle-API/analysis/5-letters-words.txt'
    words = open(file, 'r').read().split('\n')
    for w in words:
        w = w.lower()
        w_letters = [c for c in w if c in allowed_letters]
        if len(w_letters) == len(w):
            print(w)

def print_most_vowels_list():
    vowels = list('aeiou')
    word_per_most_vowels = {}
    file = '/Users/zemian/my-web/wordle-API/analysis/5-letters-frequent-words.txt'
    words = open(file, 'r').read().split('\n')
    for w in words:
        w = w.lower()
        w_vowels = [v for v in vowels if v in w]
        if len(w_vowels) >= 3:
            word_per_most_vowels[w] = len(w_vowels)
            print(w)
    # word_per_most_vowels = dict(reversed(sorted(word_per_most_vowels.items(), key=lambda item: item[1])))
    # print(word_per_most_vowels)
    # {'uraei': 4, 'ousia': 4, 'ourie': 4, 'ouabe': 4, 'miaou': 4, 'louie': 4, 'heiau': 4, 'aurei': 4, 'auloi': 4, 'aueto': 4, 'audio': 4, 'adieu': 4, 'utile': 3, 'utero': 3, 'uteri': 3, 'usnea': 3, 'usine': 3, 'ursae': 3, 'urnae': 3, 'urite': 3, 'urine': 3, 'uriel': 3, 'urian': 3, 'urial': 3, 'uriah': 3, 'urena': 3, 'ureid': 3, 'ureic': 3, 'uredo': 3, 'ureas': 3, 'ureal': 3, 'urate': 3, 'urase': 3, 'urari': 3, 'urare': 3, 'urali': 3, 'uptie': 3, 'upeat': 3, 'untie': 3, 'unona': 3, 'unoil': 3, 'unode': 3, 'unlie': 3, 'unite': 3, 'union': 3, 'unice': 3, 'uniat': 3, 'uncia': 3, 'unamo': 3, 'unami': 3, 'unais': 3, 'umiac': 3, 'uloid': 3, 'ulnae': 3, 'ulema': 3, 'uinta': 3, 'uinal': 3, 'udasi': 3, 'uaupe': 3, 'ualis': 3, 'uayeb': 3, 'turio': 3, 'tubae': 3, 'troue': 3, 'touse': 3, 'topia': 3, 'topau': 3, 'tomia': 3, 'toise': 3, 'toile': 3, 'todea': 3, 'tinea': 3, 'terai': 3, 'tenio': 3, 'tenia': 3, 'tenai': 3, 'teloi': 3, 'telia': 3, 'teian': 3, 'tauri': 3, 'taupo': 3, 'taupe': 3, 'tauli': 3, 'taube': 3, 'tatou': 3, 'tatie': 3, 'tarie': 3, 'talio': 3, 'taise': 3, 'taipo': 3, 'taino': 3, 'susie': 3, 'supai': 3, 'suomi': 3, 'sulea': 3, 'suite': 3, 'suine': 3, 'suina': 3, 'suade': 3, 'stoai': 3, 'stoae': 3, 'staio': 3, 'souse': 3, 'sotie': 3, 'sosie': 3, 'sosia': 3, 'solea': 3, 'soapi': 3, 'sitao': 3, 'sinae': 3, 'sieur': 3, 'siena': 3, 'sesia': 3, 'serio': 3, 'serau': 3, 'serai': 3, 'sepia': 3, 'seoul': 3, 'seora': 3, 'saute': 3, 'saudi': 3, 'sauce': 3, 'salue': 3, 'saite': 3, 'saice': 3, 'sadie': 3, 'rupie': 3, 'rupia': 3, 'rubia': 3, 'route': 3, 'rouse': 3, 'roues': 3, 'rouen': 3, 'retia': 3, 'reoil': 3, 'reina': 3, 'redia': 3, 'rebia': 3, 'raupo': 3, 'rauli': 3, 'ratio': 3, 'ramie': 3, 'raise': 3, 'raiae': 3, 'radio': 3, 'pupae': 3, 'psoai': 3, 'psoae': 3, 'poule': 3, 'pouce': 3, 'poria': 3, 'popie': 3, 'poise': 3, 'poire': 3, 'poilu': 3, 'podia': 3, 'piute': 3, 'pitau': 3, 'pious': 3, 'pilea': 3, 'pilau': 3, 'pieta': 3, 'picea': 3, 'picae': 3, 'piano': 3, 'perau': 3, 'perai': 3, 'pause': 3, 'patio': 3, 'paseo': 3, 'pareu': 3, 'papio': 3, 'paise': 3, 'paine': 3, 'paeon': 3, 'padou': 3, 'outre': 3, 'outer': 3, 'outen': 3, 'outed': 3, 'outas': 3, 'ousel': 3, 'ouphe': 3, 'ounce': 3, 'oulap': 3, 'otium': 3, 'otate': 3, 'ostia': 3, 'ossia': 3, 'ossea': 3, 'osier': 3, 'oside': 3, 'oshea': 3, 'osela': 3, 'oriya': 3, 'oriel': 3, 'orias': 3, 'oreas': 3, 'oread': 3, 'orate': 3, 'orale': 3, 'opium': 3, 'opine': 3, 'opera': 3, 'opelu': 3, 'oorie': 3, 'onium': 3, 'oncia': 3, 'omina': 3, 'omani': 3, 'olpae': 3, 'ollie': 3, 'oleum': 3, 'olena': 3, 'olein': 3, 'oleic': 3, 'oldie': 3, 'oiler': 3, 'oiled': 3, 'oidia': 3, 'ohias': 3, 'ohare': 3, 'oenin': 3, 'oecus': 3, 'odium': 3, 'odeum': 3, 'oculi': 3, 'ocrea': 3, 'ocean': 3, 'obias': 3, 'obeli': 3, 'obeah': 3, 'oater': 3, 'oaten': 3, 'oasis': 3, 'oases': 3, 'oaric': 3, 'oared': 3, 'nudie': 3, 'nubia': 3, 'norie': 3, 'noria': 3, 'noise': 3, 'noire': 3, 'noyau': 3, 'noemi': 3, 'niuan': 3, 'niota': 3, 'niobe': 3, 'niepa': 3, 'neuma': 3, 'necia': 3, 'naomi': 3, 'musie': 3, 'munia': 3, 'mouse': 3, 'moule': 3, 'moues': 3, 'morae': 3, 'monie': 3, 'moise': 3, 'moire': 3, 'moira': 3, 'moile': 3, 'moier': 3, 'mitua': 3, 'minae': 3, 'mimeo': 3, 'miaul': 3, 'meuni': 3, 'mesua': 3, 'melia': 3, 'medio': 3, 'media': 3, 'meaul': 3, 'mauri': 3, 'matie': 3, 'mario': 3, 'marie': 3, 'maori': 3, 'maniu': 3, 'manie': 3, 'manei': 3, 'mamie': 3, 'malie': 3, 'maleo': 3, 'maius': 3, 'maire': 3, 'maine': 3, 'maile': 3, 'maidu': 3, 'mahoe': 3, 'luteo': 3, 'lutea': 3, 'lutao': 3, 'luite': 3, 'luian': 3, 'lucia': 3, 'louse': 3, 'loupe': 3, 'louis': 3, 'louey': 3, 'looie': 3, 'loeil': 3, 'linea': 3, 'lieut': 3, 'lieus': 3, 'lieue': 3, 'liane': 3, 'leuma': 3, 'leuco': 3, 'leora': 3, 'lelia': 3, 'leila': 3, 'lehua': 3, 'laure': 3, 'lauia': 3, 'laude': 3, 'laius': 3, 'laine': 3, 'laeti': 3, 'issue': 3, 'iseum': 3, 'irous': 3, 'irone': 3, 'iroha': 3, 'ireos': 3, 'irena': 3, 'irate': 3, 'irade': 3, 'youse': 3, 'youre': 3, 'iotas': 3, 'iodal': 3, 'inure': 3, 'inula': 3, 'intue': 3, 'insue': 3, 'insea': 3, 'inone': 3, 'inoma': 3, 'indue': 3, 'inane': 3, 'imbue': 3, 'imaum': 3, 'iliau': 3, 'ileus': 3, 'ileum': 3, 'ileon': 3, 'ileal': 3, 'ileac': 3, 'idose': 3, 'idola': 3, 'ideta': 3, 'ideas': 3, 'idean': 3, 'ideal': 3, 'idcue': 3, 'idaho': 3, 'icaco': 3, 'ibota': 3, 'ianus': 3, 'yameo': 3, 'iambe': 3, 'hutia': 3, 'huile': 3, 'huari': 3, 'huaco': 3, 'house': 3, 'houri': 3, 'hosea': 3, 'horae': 3, 'holia': 3, 'hoise': 3, 'hinau': 3, 'hiera': 3, 'hiate': 3, 'heuau': 3, 'helio': 3, 'haute': 3, 'hause': 3, 'haori': 3, 'haole': 3, 'hanoi': 3, 'haire': 3, 'haine': 3, 'eusol': 3, 'euros': 3, 'eupad': 3, 'eucti': 3, 'etuis': 3, 'etiam': 3, 'eruca': 3, 'erica': 3, 'erian': 3, 'erbia': 3, 'erato': 3, 'epulo': 3, 'ephoi': 3, 'eosin': 3, 'eoith': 3, 'entia': 3, 'enpia': 3, 'enoil': 3, 'ennui': 3, 'ennia': 3, 'eniac': 3, 'endia': 3, 'encia': 3, 'enami': 3, 'email': 3, 'eloin': 3, 'eloah': 3, 'eliot': 3, 'elihu': 3, 'elias': 3, 'elian': 3, 'elain': 3, 'elaic': 3, 'eidos': 3, 'edoni': 3, 'ediya': 3, 'ecoid': 3, 'dusio': 3, 'durio': 3, 'duomi': 3, 'duole': 3, 'dulia': 3, 'dubio': 3, 'duane': 3, 'duali': 3, 'douse': 3, 'doura': 3, 'douma': 3, 'douce': 3, 'douar': 3, 'doria': 3, 'donia': 3, 'dolia': 3, 'doina': 3, 'dobie': 3, 'diota': 3, 'diose': 3, 'dione': 3, 'diode': 3, 'diane': 3, 'deota': 3, 'delia': 3, 'deino': 3, 'deair': 3, 'dauri': 3, 'daube': 3, 'danio': 3, 'damie': 3, 'cutie': 3, 'cusie': 3, 'curio': 3, 'curie': 3, 'curia': 3, 'cunei': 3, 'cunea': 3, 'cueca': 3, 'craie': 3, 'coupe': 3, 'couma': 3, 'coude': 3, 'couac': 3, 'cosie': 3, 'coria': 3, 'copia': 3, 'copei': 3, 'conia': 3, 'comae': 3, 'cohue': 3, 'cobia': 3, 'coati': 3, 'coaid': 3, 'citua': 3, 'chiao': 3, 'chaui': 3, 'ceria': 3, 'celia': 3, 'ceibo': 3, 'ceiba': 3, 'cause': 3, 'caupo': 3, 'cauli': 3, 'canoe': 3, 'cameo': 3, 'caite': 3, 'cairo': 3, 'cadie': 3, 'cacei': 3, 'cabio': 3, 'buteo': 3, 'butea': 3, 'burao': 3, 'bueno': 3, 'bouse': 3, 'boule': 3, 'bouet': 3, 'boite': 3, 'boise': 3, 'boyau': 3, 'bohea': 3, 'biune': 3, 'biota': 3, 'biose': 3, 'biome': 3, 'biabo': 3, 'beisa': 3, 'beira': 3, 'beaut': 3, 'beaus': 3, 'beati': 3, 'beano': 3, 'baure': 3, 'bauno': 3, 'baume': 3, 'baubo': 3, 'baroi': 3, 'barie': 3, 'balei': 3, 'bayou': 3, 'baioc': 3, 'bailo': 3, 'baile': 3, 'bahoe': 3, 'autre': 3, 'autos': 3, 'autor': 3, 'autem': 3, 'auris': 3, 'aurir': 3, 'aurin': 3, 'auric': 3, 'aures': 3, 'aurae': 3, 'aumil': 3, 'aulos': 3, 'aulic': 3, 'aulae': 3, 'audit': 3, 'aubin': 3, 'atune': 3, 'atule': 3, 'atour': 3, 'atone': 3, 'atole': 3, 'atelo': 3, 'asuri': 3, 'aside': 3, 'arulo': 3, 'artou': 3, 'artie': 3, 'arrie': 3, 'arose': 3, 'aroid': 3, 'arius': 3, 'arite': 3, 'arise': 3, 'ariot': 3, 'arion': 3, 'arioi': 3, 'aries': 3, 'ariel': 3, 'areic': 3, 'appui': 3, 'apout': 3, 'apium': 3, 'apios': 3, 'apiol': 3, 'aperu': 3, 'aouad': 3, 'aotus': 3, 'aotes': 3, 'aotea': 3, 'anous': 3, 'anour': 3, 'anoli': 3, 'anole': 3, 'anoil': 3, 'anoia': 3, 'anode': 3, 'annie': 3, 'anise': 3, 'anion': 3, 'animo': 3, 'anime': 3, 'anile': 3, 'anice': 3, 'amuse': 3, 'amour': 3, 'amole': 3, 'amire': 3, 'amino': 3, 'amine': 3, 'amies': 3, 'amido': 3, 'amide': 3, 'amice': 3, 'amelu': 3, 'alure': 3, 'aluco': 3, 'alout': 3, 'aloud': 3, 'alose': 3, 'alone': 3, 'alois': 3, 'aloin': 3, 'aloid': 3, 'aloes': 3, 'aloed': 3, 'allie': 3, 'alite': 3, 'aliso': 3, 'aline': 3, 'aliet': 3, 'alien': 3, 'alice': 3, 'aleut': 3, 'alenu': 3, 'aisle': 3, 'airer': 3, 'aired': 3, 'ayous': 3, 'aioli': 3, 'ainus': 3, 'ainoi': 3, 'ainee': 3, 'aimer': 3, 'aimee': 3, 'aimed': 3, 'ailie': 3, 'ailed': 3, 'aiery': 3, 'aides': 3, 'aider': 3, 'aided': 3, 'aesop': 3, 'aesir': 3, 'aeron': 3, 'aerie': 3, 'aeric': 3, 'aeons': 3, 'aecia': 3, 'adure': 3, 'adrue': 3, 'adore': 3, 'adobe': 3, 'adios': 3, 'adion': 3, 'adiel': 3, 'addio': 3, 'addie': 3, 'acute': 3, 'acoup': 3, 'acone': 3, 'acoin': 3, 'acies': 3, 'acier': 3, 'abuse': 3, 'abune': 3, 'about': 3, 'abote': 3, 'aboil': 3, 'abode': 3, 'abime': 3, 'abilo': 3, 'abies': 3, 'abide': 3, 'abbie': 3, 'abaue': 3}

if __name__ == '__main__':
    print_most_vowels_list()