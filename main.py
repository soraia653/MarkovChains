import random

txt = "The unicorn is a legendary creature that has been described since antiquity as a beast with a large, pointed, spiraling horn projecting from its forehead. The unicorn was depicted in ancient seals of the Indus Valley Civilization and was mentioned by the ancient Greeks in accounts of natural history by various writers, including Ctesias, Strabo, Pliny the Younger, and Aelian. The Bible also describes an animal, the re'em, which some translations have erroneously rendered with the word unicorn. In European folklore, the unicorn is often depicted as a white horse-like or goat-like animal with a long horn and cloven hooves (sometimes a goat's beard). In the Middle Ages and Renaissance, it was commonly described as an extremely wild woodland creature, a symbol of purity and grace, which could only be captured by a virgin. In the encyclopedias its horn was said to have the power to render poisoned water potable and to heal sickness. In medieval and Renaissance times, the tusk of the narwhal was sometimes sold as unicorn horn."

order = 4
ngrams = {}

# generate text based on input
def MarkovIt():
    currentGram = txt[0:order]
    result = currentGram

    for i in range(10):
        try:
            possibilities = ngrams[currentGram]
            next = random.choice(possibilities)
            result += next
            length = len(result)
            currentGram = result[length - order : length]
        except IndexError:
            break


    print(result)


for i, v in enumerate(txt[: len(txt) - order + 1]):
    gram = txt[i : i + order]

    if gram not in ngrams:
        ngrams[gram] = []
        try:
            ngrams[gram].append(txt[i + order])
        except IndexError:
            break
    else:
        try:
            ngrams[gram].append(txt[i + order])
        except IndexError:
            break

MarkovIt()
