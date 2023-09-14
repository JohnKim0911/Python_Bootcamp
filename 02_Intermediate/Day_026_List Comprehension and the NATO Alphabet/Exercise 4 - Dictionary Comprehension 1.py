sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words_list = sentence.split()

result = {word: len(word) for word in words_list}

print(result)
# {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
