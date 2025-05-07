import string

paragraph = """
Cycling is an excellent form of exercise that provides numerous health benefits. 
It is not only great for improving cardiovascular fitness, but it also helps in building strength and endurance. 
Cycling can be done at a leisurely pace or as a competitive sport. 
Whether it's commuting to work, enjoying a scenic ride, or competing in races, cycling is a versatile and eco-friendly activity that people of all ages can enjoy.
"""

num_characters = len(paragraph)

num_sentences = sum(1 for char in paragraph if char in ".!?")

words = paragraph.split()
num_words = len(words)

unique_words = set(word.strip(string.punctuation).lower() for word in words)
num_unique_words = len(unique_words)


print(f"Analysis of the paragraph:")
print(f"Number of characters: {num_characters}")
print(f"Number of sentences: {num_sentences}")
print(f"Number of words: {num_words}")
print(f"Number of unique words: {num_unique_words}")