import os
import time
import random
from weapon import Weapon
from armor import Armor
from robbery import Robbery

clear = lambda: os.system('cls')


def rob(robbery):
  clear()
  print 'Adventuring in ' + robbery.name
  
  time.sleep(1)
  
  print dashLine
  global money
  global weapon
  global armor
  stealth = random.randint(1, 20) + weapon.con + armor.con
  loot = robbery.lootMax * 1
  
  global infamy
  
  if stealth >= robbery.sec or random.randint(1, 20) >= 19:
    print 'You snuck past the monsters!'
    print 'You secured ' + str(int(loot)) + ' gold worth of ' + robbery.lootDesc + '.'
    infamy  = infamy + (robbery.lootMax/2)
    print 'You gained ' + str(int(robbery.lootMax/2)) + ' XP!'
    # global money
    money = money + loot
    print 'After selling the loot, you have ' + str(int(money)) + ' gold.'
    input('Press enter to continue...')
    mainMenu()
  else:
    print 'The monsters detected you!'
    print 'The monsters are attacking!'
    time.sleep(1)
    
    atk = random.randint(1, 20) + weapon.atk + armor.atk
    if atk >= robbery.res or random.randint(1, 20) >= 19:
      print dashLine
      money = money + (loot/2)
      print "You managed to escape and secured " + str(int(float(loot/2))) + " gold worth of " + robbery.lootDesc + "."
      infamy  = infamy + (robbery.lootMax/2)
      print 'You gained ' + str(int(robbery.lootMax/2)) + ' XP!'
      print 'After selling the loot, you have ' + str(int(money)) + ' gold.'
      input('Press enter to continue...')
      mainMenu()
    else:
      global lives
      
      lives = lives - 1
      
      print dashLine
      print 'You were slain by monsters.'
      
      if lives == 0:
        print 'Game Poopie'
        c = input('Play again? [y/n]')
        if c == 'y':
          # global weapon
          # global armor
          weapon = weaponList[0]
          armor = armorList[0]
          money = 0
          infamy = 0
          lives = 3
          clear()
          titleScreen()
          return()
        else:
          while True:
            time.sleep(0.1)
      
      print 'You have ' + str(lives) + ' lives remaining.'
      bail = (money/10) * 6
      money = money - bail
      infamy = infamy/4
      print 'The monsters stole ' + str(int(bail)) + ' gold.'
      print 'You lost ' + str(int(infamy * 3)) + ' XP.'
      input('Press enter to continue...')
      
      

def shop():
  global money
  
  clear()
  print "Welcome to the store! Here's what's available:"
  print dashLine
  
  for i in range(len(weaponList)):
    print str(i) + '. ' + str(weaponList[i]) + ' - ' + str(weaponList[i].price)  + ' gold'
  print dashLine
  for i in range(len(armorList)):
    print str(i) + '. ' + str(armorList[i]) + ' - ' + str(armorList[i].price) + ' gold'
  print dashLine
  
  print 'You have ' + str(int(money)) + ' gold'
  
  print 'Would you like to buy a [w]eapon, [a]rmor, or [r]eturn to the main menu?'
  choice = input()
  
  options = ['w', 'a', 'r']
  while not choice in options:
    print dashLine
    print 'You must enter one of the following: ' + str(options)
    print 'Would you like to buy a [w]eapon, [a]rmor, or [r]eturn to the main menu?'
    choice = input()
    
    # Weapon
  if choice == 'w':
    print 'Enter the number of the weapon you wish to buy.'
    choice = input()
    
    while not choice.isdigit():
      print dashLine
      print 'You must enter a number.'
      print 'Enter the number of the weapon you wish to buy.'
      choice = input()
      
    choice = int(choice)
    
    while choice < 0 or choice >= len(weaponList):
      print dashLine
      print 'Invalid weapon ID'
      print 'Enter the number of the weapon you wish to buy.'
      choice = input()
      while not choice.isdigit():
        print dashLine
        print 'You must enter a number.'
        print 'Enter the number of the weapon you wish to buy.'
        choice = input()
      choice = int(choice)
      
    if money > weaponList[choice].price:
      print dashLine
      print 'You can afford that weapon.'
      input('Press enter to continue...')
      shop()
      return
      
    else:
      print 'Purchased ' + weaponList[choice].name + '!'
      global weapon
      weapon = weaponList[choice]
      money = money - weapon.price
      input('Press enter to continue...')
      shop()
      return
    
  # Armor
  elif choice == 'a':
    print 'Enter the number of the armor you wish to buy.'
    choice = input()
    
    while not choice.isdigit():
      print dashLine
      print 'You must enter a number.'
      print 'Enter the number of the armor you wish to buy.'
      choice = input()
      
    choice = int(choice)
    
    while choice < 0 or choice >= len(armorList):
      print dashLine
      print 'Invalid armor ID'
      print 'Enter the number of the armor you wish to buy.'
      choice = input()
      while not choice.isdigit():
        print dashLine
        print 'You must enter a number.'
        print 'Enter the number of the armor you wish to buy.'
        choice = input()
      choice = int(choice)
      
    if money < armorList[choice].price:
      print dashLine
      print 'You cannot afford that armor.'
      input('Press enter to continue...')
      shop()
      return
      
    else:
      print 'Purchased ' + armorList[choice].name + '!'
      global armor
      armor = armorList[choice]
      money = money - armor.price
      input('Press enter to continue...')
      shop()
      return
    
  # Return to menu
  elif choice == 'r':
    return
  
def robberies():
  clear()
  print 'Where would you like to adventure? (Enter [r] to go back to the menu)'
  for i in range(len(robberyList)):
    print str(i) + '. ' + robberyList[i].name + ' - Requires ' + str(robberyList[i].infamy) + ' XP'
  print 'XP: ' + str(infamy)
    
  choice = input()
  
  if choice == 'r':
    mainMenu()
  
  while not str(choice).isdigit():
    print dashLine
    print 'You must enter a number (or [r]).'
    print 'Enter the number of the location you wish to explore.'
    choice = input()
    
    if choice == 'r':
      mainMenu()
      
    while not str(choice).isdigit():
      print dashLine
      print 'You must enter a number (or [r]).'
      print 'Enter the number of the location you wish to explore.'
      choice = input()
      
    choice = int(choice)
    
    while choice < 0 or choice >= len(armorList):
      print dashLine
      print 'Invalid location ID'
      print 'Enter the number of the location you wish to explore.'
      choice = input()
      while not choice.isdigit():
        print dashLine
        print 'You must enter a number (or [r]).'
        print 'Enter the number of the location you wish to explore.'
        choice = input()
      choice = int(choice)
      
  if infamy >= robberyList[int(choice)].infamy:
    rob(robberyList[int(choice)])
  else:
    print 'You do not have enough XP.'
    input('Press enter to continue...')
    robberies()

def mainMenu():
  clear()
  print 'Weapon: ' + str(weapon)
  print 'Armor: ' + str(armor)
  print 'You have ' + str(int(money)) + ' gold.'
  print dashLine
  print 'Concealment: ' + str(weapon.con + armor.con)
  print 'Attack: ' + str(weapon.atk + armor.atk)
  print 'XP: ' + str(int(infamy))
  print 'Lives: ' + str(lives)
  print dashLine
  print 'What would you like to do?'
  print '[s]hop'
  print '[a]dventure'
  
  choice = input()
  options = ['s', 'a']
  while not choice in options:
    print dashLine
    print 'You must enter one of the following: ' + str(options)
    print 'What would you like to do?'
    choice = input()
    
  if choice == 's':
    shop()
    mainMenu()
  elif choice == 'a':
    robberies()
    mainMenu()

def titleScreen():
  print 'Welcome to'
  time.sleep(0.3)
  print 'Adventure Simulator\n'
  input('Press enter to play...')
  mainMenu()
  
weaponList = []
weaponList.append(Weapon('Dagger', 0, 5, 2))
weaponList.append(Weapon('Shortsword', 1000, 4, 5))
weaponList.append(Weapon('Longsword', 3500, 1, 9))
weaponList.append(Weapon('Invisible Dagger', 4000, 7, 1))
weaponList.append(Weapon('Invisible Shortsword', 7500, 7, 3))
weaponList.append(Weapon('Broadsword', 7000, -2, 14))
weaponList.append(Weapon('Greatsword', 12000, -3, 18))
weaponList.append(Weapon('Ethereal Sword', 12000, 12, 6))

armorList = []
armorList.append(Armor('None', 0, 5, 0))
armorList.append(Armor('Leather Armor', 1500, 3, 4))
armorList.append(Armor('Plate Armor', 5000, -2, 10))
armorList.append(Armor('Monster Disguise', 2000, 8, 0))
armorList.append(Armor('Better Monster Disguise', 6000, 12, -1))
armorList.append(Armor('Chain Shirt', 2500, 5, 6))

robberyList = []
robberyList.append(Robbery('Forest', 12, 12, 500, 'poop wood', 0))
robberyList.append(Robbery('Desert', 17, 14, 1000, 'scales', 0))
robberyList.append(Robbery('Deep Forest', 19, 15, 2000, 'elder wood', 1500))
robberyList.append(Robbery('Mountains', 20, 17, 3200, 'hardened snow', 2500))
robberyList.append(Robbery('Dark Woods', 20, 15, 4000, 'dark wood', 3000))
robberyList.append(Robbery('Dungeon', 23, 18, 6000, 'ancient treasures', 4500))
robberyList.append(Robbery('Volcano', 24, 22, 8000, 'magic embers', 7000))
robberyList.append(Robbery('Dwarven Ruins', 26, 30, 10000, 'gemstones', 10000))
robberyList.append(Robbery('Corrupted Wilds', 28, 36, 15000, 'tentacles', 20000))
robberyList.append(Robbery('Fortress of Evil', 32, 42, 100000, 'evil', 35000))

weapon = weaponList[0]
armor = armorList[0]
money = 0
infamy = 0
lives = 3

dashLine = '------------------'

titleScreen()
