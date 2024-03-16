# JP0030

from langdetect import detect

def detect_language(text):
    return detect(text)

text = "வணக்கம்"

codes={
 'ar': 'Arabic', 'et': 'Armenian', 'art': 'Artificial Langauge',
 'sq': 'Albanian','bn': 'Bangla', 'bh': 'Bhojpuri',
'bul': 'Bulgarian', 'cai': 'Central American Indian Language',
 'cze': 'Caech', 'dan': 'Danish', 'ger': 'German', 'eg': 'Egyptian', 'en': 'English',
 'fre': 'french', 'gon': 'Gondi', 'grc': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
 'ind': 'Indonesian', 'ita': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
 'kas': 'Kashmiri', 'geo': 'Georgian', 'kor': 'Korean', 'lat': 'Latin',
 'mar': 'Marathi', 'mni': 'Manipuri', 'mul': 'Multiple Languages', 'dut': 'Dutch',
'te': 'Telugu', 'ta': 'Tamil','cy':'Welsh'}

print("The language of the text is:", codes[detect_language(text)])