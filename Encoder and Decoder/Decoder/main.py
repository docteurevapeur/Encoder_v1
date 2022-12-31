def deTransFunction(x):
  ruChar = "абцдеэфФгйяюёижклмныртвьъзщЩшчхсуоп"
  engDeRu = ["a", "b", "c", "d", "ye", "e", "f", "ph", "g", "y", "ya", "yu", "yo", "i", "j", "k", "l", "m", "n", "q", "r", "t", "v", "w", "x", "z", " ", "sh", "sh", "ch", "h", "s", "u", "o", "p"]
  for i in range(len(ruChar)):
    if(x == ruChar[i]):
      return engDeRu[i]
def unShiftFunction(x, y):
  good = "абцдеэфФгйяюёижклмныртвьъзщЩшчхсуоп"
  for i in range(len(good)):
    if(x == y[i]):
      return good[i]
#code = input("Enter coded message: ")
readMessage = open('finishedmessage.txt', 'r', encoding="utf8")
code = readMessage.read()
readMessage.close()
openKey = open('key.txt', 'r', encoding="utf8")
decodeKey = openKey.read()
openKey.close()
unShiftMessage = ""
for n in range(len(code)):
  unShiftMessage = unShiftMessage + str(unShiftFunction(code[n], decodeKey))
deTransMessage = ""
for i in range(len(unShiftMessage)):
  deTransMessage = deTransMessage + str(deTransFunction(unShiftMessage[i]))
writeMessage = open('decodedmessage.txt', 'w', encoding="utf8")
writeMessage.write(deTransMessage)
writeMessage.close()