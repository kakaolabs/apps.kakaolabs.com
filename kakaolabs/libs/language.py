# -*- coding: utf-8 -*

VIETNAMESE_LETTERS = u"áàảãạâấầẩẫậăắằẳẵặéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủủũụưứừửữựýỳỷỹỵ"
ENGLISH_LETTERS    = u"aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuuyyyyy"

def convert_vietnamese_to_english(word):
    print word
    size = len(VIETNAMESE_LETTERS)
    for i in xrange(0, size):
        viet_letter = VIETNAMESE_LETTERS[i].encode("utf-8")
        eng_letter = ENGLISH_LETTERS[i].encode("utf-8")
        word = word.replace(viet_letter, eng_letter)
    return word
