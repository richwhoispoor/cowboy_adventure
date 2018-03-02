# welcome to the adventure game

# import random routine
# import random

# define sub routines
# inspect decision for result
def decision(UserDecision):
     userdecision = input()
     
     
print(' ')
print('Welcome pilgrim, this is your wild west adventure game!!!!')
print(' ')
print('The game is easy to navigate and play')
print('follow the instructions to determine your next action')
print('the results of your action will be displayed on your screen')
print('after you have entered your decision')
print(' ')
print('Think wisely for each action')
print(' ')
# define character name, horse name and country name
print('Lets start by typing your name?')
CharactorName = input()
print('Well hello there ' + CharactorName)
print('Nice to meet you')
print('Are you a male or female?')
CharaterGender = input()
#if CharaterGender == 'male' or 'female':
#    break
#else
#   print('Please use only male or female':
print(' ')
print('Now can you type your horses name?')
HorseName = input()
print('What a mighty steed you are ' + HorseName)
print(' ')
print('Can you type the name of the place that ' + CharactorName + ' lives?')
CountryName = input()
print(CountryName + ' sounds like a strange place!')
print(' ')
print('Lets get started')
print(' ')

# start the adventure
# 
print('It is a dark and stormy day in ' + CountryName)
print('The rain is very heavy and ' + CharactorName + ' is drenched.')
print(' ')
print(CharactorName + ' sees a dry cave ahead.  Type "1" if you "go in" or type "2" if you "keep going"?')
UserDecision = input()
try UserDecision == 1:
    print('Ok')
elif UserDecision == 2:
    Print('you get dry')
    


#print(HorseName + '
