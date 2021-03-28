
import random
print('Welcome to the Rock, scissors and paper game.')
username = input('what is your name? ')
choice_user = input('¿scissors, rock or paper? ')
choice_pc = random.choice(['rock', 'scissors', 'paper'])

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if choice_user == 'scissors' and choice_pc == 'paper' :
	print('Machine choise ' + choice_pc)
	print(username + ' won!')
elif choice_user == 'scissors' and choice_pc == 'rock' :
	print('Machine choise ' + choice_pc)
	print(username +' lose!')
elif choice_user == 'paper' and choice_pc == 'scissors' :
	print('Machine choise ' + choice_pc)
	print(username +' lose!')
elif choice_user == 'paper' and choice_pc == 'rock' :
	print('Machine choise ' + choice_pc)
	print('{username} won!')
elif choice_user == 'rock' and choice_pc == 'scissors' :
	print('Machine choise ' + choice_pc)
	print(username + ' won!')
elif choice_user == 'rock' and choice_pc == 'scissors' :
	print('Machine choise ' + choice_pc)
	print(username + ' won!')
else :
	print('drawm')