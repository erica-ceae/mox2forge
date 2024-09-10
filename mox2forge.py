import pyperclip

# list of fragments forge seems to struggle with
# bad_words = ["*F*","PLST"]

def delist(card):
    card = card.replace("(PLST) ", "(")
    num = card[card.rfind("-")+1:]
    card = card[0:card.rfind("-")]
    card = card + ") " + str(num)
    return card

list = pyperclip.paste().split("\n")

for i in range(0, len(list)):
    card = list[i]
    match card:
        case card if "*F*" in card:
            list[i] = card.replace("*F*", "")
        case card if "(PLST)" in card:
            list[i] = delist(card)
        case _:
            pass

pyperclip.copy("\n".join(list))
