from deep_translator import GoogleTranslator

fr_list = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translations = {}

for word in fr_list:
    translated = GoogleTranslator(source='french', target='english').translate(word)
    translations[word] = translated

print(translations)
