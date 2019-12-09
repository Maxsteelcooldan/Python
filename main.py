
#IMPORTATION
import time
#Characters
player = {'name':'Godsplan','attack':1,'health':100}
Monster = {'name':'EvilGodsplan','attack':1,'health':100}

#Asking if your want to play
print('Hi, what\'s your name')
player['name'] = input()
time.sleep(1)
print('You have a nice name,' + player['name'])
time.sleep(3)
print('You want to play my new game')
play = input("")

#IF SAY YES OR NO
if play == "yes" or play == "Yes":
  print('It will boot up in a few seconds')
  print('thanks for saying yes by the way')
elif play == "no" or play == "No":
  print("you suck, now restart if you want to play")
else:
  print("NOT AN OPTION, now restart kid or adult") 

#Begenning
  print("Someguy said your trash,You want to kill")
  Kill = input("")
  if Kill == "Yes" or Kill == "yes":
    print("That guy is way stronger than you so you got beaten up")
  elif Kill == "No" or Kill == "no":
    print("Good Option")
    print("You would have goten beaten up")
  else:
    print("That\'s not an option ")
    time.sleep(2)
    print("I will pick it for you")
    time.sleep(2)
    print("That guy is way stronger than you so you got beaten up")
    time.sleep(2)
    print("I\'m so evil")
    
      
      
    







