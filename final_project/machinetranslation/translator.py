from deep_translator import MyMemoryTranslator

def english_to_french (englishText):

    frenchText = MyMemoryTranslator (source= 'english', target= 'french'). translate (englishText)

    return frenchText

def french_to_english(frenchText):

    englishText = MyMemoryTranslator (source= 'french', target= 'english'). translate (frenchText)
    
    return englishText
