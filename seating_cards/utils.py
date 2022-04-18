import constants

def unaccent_word(word):
    unaccented_word = ''
    for c in word:
        unaccented_word = unaccented_word + constants.character_counterparts.get(c,c)
    return unaccented_word