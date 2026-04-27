import os
def encode():
  os.system("clear")
  encode = input("What should I encode?: ")
  dictionary = {"a": " hell", "b": " six", "c": " sex", "d": " health", "e": " fix", "f": " spirit", "g": " denounce", "h": " basketball", "i": " football", "j": " soccerball", "k": " doom", "l": " park", "m": " bird", "n": " wildlife", "o": " elderly", "p": " extra", "q": " recreational", "r": " word", "s": " prop", "t": " game", "u": " okay", "v": " duty", "w": " computer", "x": " test", "y": " paper", "z": " life"}
  table = str.maketrans(dictionary)
  ev = encode.translate(table)
  print(ev)