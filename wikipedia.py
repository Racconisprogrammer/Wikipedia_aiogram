import wikipedia

def wiki(key):
    wikipedia.set_lang('uz')
    try:
        result = wikipedia.summary(key)
    except wikipedia.exceptions.DisambiguationError:
        result = "Juda k'op ma'lumot topildi.Ba'tafsilroq kiriting."
    except wikipedia.exceptions.PageError:
        result = "Siz kiritgan kalit so'z wikipediada topilmadi."
    return result
