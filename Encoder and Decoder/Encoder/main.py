def transFunction(x, y):   #function to change to cyrillic
  def lastTest(x, y):      #might delete, but tests if letter is last letter
    if(len(x) - 1 == y):
      return 0
    else:
      return 1
  easy = ["b", "d", "f", "g", "i", "j", "k", "l", "m", "n", "q", "r", "t", "v", "w", "x", "z", " "]        #creating a list of easier letters
  easyRu = ["б", "д", "ф", "г", "и", "ж", "к", "л", "м", "н", "ы", "р", "т", "в", "ь", "ъ", "з", "щ"]
  for i in range(0, 18):    #testing if the number happens to be an easy letter
    if(x[y] == easy[i]):
      return easyRu[i]
  if(x[y] == "a"):         #these letters are a bit more complicated
    if(y == 0):
      return "а"
    elif(x[y-1] == "y"):
      return "я"
    else:
      return "а"
  if(x[y] == "c"):
    if(lastTest(x, y) == 0):
      return "ц"
    elif(x[y+1] == "h"):
      return "ч"
    else:
      return "ц"
  if(x[y] == "e"):
    if(y == 0):
      return "э"
    elif(x[y-1] == "y"):
      return "е"
    else:
      return "э"
  if(x[y] == "h"):
    if(y == 0):
      return "х"
    elif(x[y-1] == "c" or x[y-1] == "s" or x[y-1] == "p"):
      return ""
    else:
      return "х"
  if(x[y] == "o"):
    if(y == 0):
      return "о"
    elif(x[y-1] == "y"):
      return "ё"
    else:
      return "о"
  if(x[y] == "p"):
    if(lastTest(x, y) == 0):
      return "п"
    elif(x[y+1] == "h"):
      return "Ф"
    else:
      return "п"
  if(x[y] == "s"):
    if(lastTest(x, y) == 0):
      return "с"
    elif(x[y + 1] == "h"):
      if(len(x) - 2 == y):
        return "ш"
      elif(x[y+2] == "i" or x[y+2] == "e"):
        return "Щ"
      else:
        return "ш"
    else:
      return "с"
  if(x[y] == "u"):
    if(y == 0):
      return "у"
    elif(x[y-1] == "y"):
      return "ю"
    else:
      return "у"
  if(x[y] == "y"):
    if(lastTest(x, y) == 0):
      return "й"
    elif(x[y+1] == "o" or x[y+1] == "e" or x[y+1] == "a" or x[y+1] == "u"):
      return ""
    else:
      return "й"

def shiftFunction(x):
  firstList = "абцдеэфФгйяюёижклмныртвьъзщЩшчхсуоп"
  global secondList
  for i in range(0, len(firstList)):
    if(x == firstList[i]):
      return secondList[i]

count = 0
#code = input("Enter code (no caps or punctuation): ")
openMessage = open('message.txt', 'r', encoding="utf8")
code = openMessage.read()
openMessage.close()
codedMessage = ""
while(count < len(code)):
  codedMessage = codedMessage + str(transFunction(code, count))
  count = count + 1      #loop to turn phrase to cyrillic
openKey = open('key.txt', 'r', encoding="utf8")
secondList = openKey.read()      #reads key
openKey.close()
shiftedCodedMessage = ""
for i in range(0, len(codedMessage)):
  shiftedCodedMessage = shiftedCodedMessage + str(shiftFunction(codedMessage[i]))    #shifting message using key.txt
createMessage = open('finishedmessage.txt', 'w', encoding="utf8")
createMessage.write(shiftedCodedMessage)
createMessage.close()