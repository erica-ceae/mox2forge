import pyperclip
import re

# list of fragments forge seems to struggle with
# any promo variant using the "P[set]" syntax, e.g. "PDOM" for "DOM" promos
# bad_words = ["*F*","PLST"]

def delist(card):
    card = card.replace("(PLST) ", "(")
    num = card[card.rfind("-")+1:]
    card = card[0:card.rfind("-")]
    card = card + ") " + str(num)
    return card

def depromo(card):
    if re.search(r"\(P[a-zA-Z0-9]{3}\)", card):
        card = card.replace("(P", "(")
    return card

def main():
    list = pyperclip.paste().split("\n")
    
    for i in range(0, len(list)):
        card = list[i]
        match card:
            case card if "*F*" in card:
                list[i] = card.replace("*F*", "")
                # catch foil promos
                list[i] = depromo(list[i])
            case card if "(PLST)" in card:
                list[i] = delist(card)
            case card if "(P" in card:
                print(card)
                list[i] = depromo(card)
            case _:
                pass
    
    pyperclip.copy("\n".join(list))

if __name__ == "__main__":
    main()
