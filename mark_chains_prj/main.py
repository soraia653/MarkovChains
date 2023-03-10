"""Generate pokemon names using Markov Chains algorithm."""
import random
import sys

ORDER = 2

# import .txt file based on user preference
OPTIONS = ["-hp", "-pkm"]
FILE_OPTIONS = {"-hp": "data/hp_spells.txt", "-pkm": "data/pokemon_names.txt"}

try:
    ARG = sys.argv[1]
except IndexError as exc:
    raise SystemExit(
        "Use CL argument -hp to generate a Harry Potter spell or -pkm to generate a Pokemon name."
    ) from exc

if ARG in OPTIONS and len(sys.argv) == 2:
    with open(FILE_OPTIONS[ARG], "r", encoding="utf-8") as f:
        data = f.readlines()
        f.close()
else:
    raise SystemExit("Available options are -hp or -pkm. You can't use both.")

ngrams = {}
beginnings = []


def markov_it():
    """generate text based on input"""
    current_gram = random.choice(beginnings)
    result = current_gram

    for _ in range(10):
        try:
            possibilities = ngrams[current_gram]
            next = random.choice(possibilities)
            result += next
            length = len(result)
            current_gram = result[length - ORDER : length]
        except IndexError:
            break

    print(result)


def prepare_data(dt):
    for j, v in enumerate(dt):
        txt = dt[j]

        for i, v in enumerate(txt[: len(txt)]):
            gram = txt[i : i + ORDER]

            if i == 0:
                beginnings.append(gram)

            if gram not in ngrams:
                ngrams[gram] = []
                try:
                    ngrams[gram].append(txt[i + ORDER])
                except IndexError:
                    break
            else:
                try:
                    ngrams[gram].append(txt[i + ORDER])
                except IndexError:
                    break


def main():
    prepare_data(data)
    markov_it()


if __name__ == "__main__":
    main()
