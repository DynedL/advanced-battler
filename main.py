import time
import random

player1 = {
	'name': 'Player',
	'maxhp': 100,
	'maxmp': 100,
	'hp': 100,
	'mp': 100,
	'atk': 30,
	'xp': 0,
	'level': 1,
}

player2 = {
	'name': 'CPU',
	'maxhp': 50,
	'maxmp': 50,
	'hp': 50,
	'mp': 50,
	'atk': 15,
	'xp': 0,
	'level': 1,
}

isPlaying = True

print('Enter the name of your character:')
player1['name'] = input('> ')

print('----------- BATTLE SIMULATOR ----------')
print(player1['name'], 'vs', player2['name'])

while isPlaying:
	
	print(' --', player1['name'] + '\'s turn --')	
	print()
	if player1['mp'] < player1['maxmp']:
		mprestore = random.randint(10,int(player1['maxmp']/4))
		temp = player1['mp']
		player1['mp'] += mprestore
		if player1['mp'] > player1['maxmp']:
			player1['mp'] = player1['maxmp']
		print(player1['name'], 'gained back', player1['mp']-temp, 'MP!')
		print()
	if player2['mp'] < player2['maxmp']:
		mprestore = random.randint(10,int(player2['maxmp']/4))
		temp = player2['mp']
		player2['mp'] += mprestore
		if player2['mp'] > player2['maxmp']:
			player2['mp'] = player2['maxmp']
		print(player2['name'], 'gained back', player2['mp']-temp, 'MP!')
		print()
	print(player1['name']+ "\'s HP:",player1['hp'])
	print(player1['name']+ "\'s MP:",player1['mp'])
	print()
	print(player2['name']+ "\'s HP:",player2['hp'])
	print(player2['name']+ "\'s MP:",player2['mp'])
	print()

	print('What would you like to do?')
	print('1. 0 MP   Melee Attack:', int(player1['atk']/2),'-',player1['atk'], "Damage")
	print('2.', player1['atk'],'MP', ' Magic Attack:', player1['atk'], "Damage")
	print('3. 20 MP  Heal')

	choice = input('> ')

	if choice == '1':
		print(player1['name'], "chose MELEE ATTACK")
		time.sleep(0.5)
		damage = random.randint(int(player1['atk']/2),player1['atk'])
		player2['hp'] -= damage
		print(' ** POW ** ')

		time.sleep(0.5)
		print(player1['name'], 'did', damage, 'damage!')
		print(player2['name'], 'hp:', player2['hp'])
	elif choice == '2':
		print(player1['name'], "chose MAGIC ATTACK")
		time.sleep(0.5)
		if player1['mp'] >= player1['atk']:
			damage = player1['atk']
			player1['mp'] -= damage
			player2['hp'] -= damage
			print(' ** ZAP ** ')
		else:
			print(player1['name'], 'did a weakend magic attack')
			damage = player1['mp']
			player1['mp'] = 0
			player2['hp'] -= damage
			print(' ** zoop ** ')
		time.sleep(0.5)
		print(player1['name'], 'did', damage, 'damage!')
		print(player2['name'], 'hp:', player2['hp'])
	elif choice == '3':
		print(player1['name'],'chose HEAL')
		time.sleep(0.5)
		if player1['mp'] >= 20:
			heal = random.randint(20, int(player1['maxhp']/2))
			temp = player1['hp']
			player1['hp'] += heal
			if player1['hp'] > player1['maxhp']:
				player1['hp'] = player1['maxhp']
			player1['mp'] -= 20
		else:
			print(player1['name'], 'did a weakend heal')
			heal = player1['mp']
			temp = player1['hp']
			player1['hp'] += heal
			if player1['hp'] > player1['maxhp']:
				player1['hp'] = player1['maxhp']
			player1['mp'] = 0
		healed = player1['hp'] - temp
		print(' ** HEALING ** ')

		time.sleep(1)
		print(player1['name'], 'healed', healed, 'points!')
		print(player1['name'], 'hp:', player1['hp'])
	else:
		print(player1['name'], 'slipped and fell!')

	if player2['hp'] <= 0:
		print('You defeated', player2['name'], '!')
		time.sleep(1)	
		xp = random.randint(30, 50)*player2['level']
		player1['xp'] += xp
		print(player1['name'], 'received', xp, 'xp! Total:', player1['xp'])
		time.sleep(1)
		#put levelup code here
		if player1['xp'] >= 100*player1['level']:
			player1['xp'] -= 100*player1['level']
			player1['level'] += 1

			atkup = random.randint(5,10)
			hpup = random.randint(10,20)
			mpup = random.randint(15,30)
			player1['atk'] += atkup
			player1['maxhp'] += hpup
			player1['maxmp'] += mpup
			player1['hp'] = player1['maxhp']
			player1['mp'] = player1['maxmp']

			print(player1['name'], 'leveled up!!')
			print('HP went up by ', hpup, ' points!! total:', player1['maxhp'])
			print('MP went up by ', mpup, ' points!! total:', player1['maxmp'])
			print('Attack went up by ', atkup, ' points!! total:', player1['atk'])
			print(player1['name'], 'is now level', player1['level'])
			input('press enter to continue')
		#put levelup code here
		print('New enemy has appeared!')
		time.sleep(1)
		player2['maxhp'] += random.randint(5,10)
		player2['maxmp'] += random.randint(5,10)
		player2['hp'] = player2['maxhp']
		player2['mp'] = player2['maxmp']
		player2['atk'] += random.randint(2,6)
		player2['level'] += 1
	else:
		#CPU Turn
		print()
		print(' --', player2['name']+'\'s TURN -- ')
		print('Hmm...')

		time.sleep(0.5)

		comChoice = random.randint(1, 100)

		if 1 <= comChoice <= 30 and player2['mp'] > 0:
			print(player2['name'],'chose HEAL')
			time.sleep(0.5)

			if player2['mp'] >= 20:
				heal = random.randint(20, int(player2['maxhp']/2))
				temp = player2['hp']
				player2['hp'] += heal
				if player2['hp'] > player2['maxhp']:
					player2['hp'] = player2['maxhp']
				player2['mp'] -= 20
			else:
				print(player2['name'], 'did a weakend heal')
				heal = player2['mp']
				temp = player2['hp']
				player2['hp'] += heal
				if player2['hp'] > player2['maxhp']:
					player2['hp'] = player2['maxhp']
				player2['mp'] = 0
			
			healed = player2['hp'] - temp
			print(' ** HEALING ** ')

			time.sleep(1)
			print(player2['name'], 'healed', healed, 'points!')
			print(player2['name'], 'hp:', player2['hp'])
		elif 31 <= comChoice <= 50 and player2['mp'] > 0:
			print(player2['name'], "chose MAGIC ATTACK")
			time.sleep(0.5)
			if player2['mp'] >= player2['atk']:
				damage = player2['atk']
				player2['mp'] -= damage
				player1['hp'] -= damage
				print(' ** ZAP ** ')
			else:
				print(player2['name'], 'did a weakend magic attack')
				damage = player2['mp']
				player2['mp'] = 0
				player1['hp'] -= damage
				print(' ** zoop ** ')
			time.sleep(0.5)
			print(player2['name'], 'did', damage, 'damage!')
			print(player1['name'], 'hp:', player1['hp'])
		else:
			print(player2['name'], "chose MELEE ATTACK")
			time.sleep(1)
			damage = random.randint(int(player2['atk']/2),player2['atk'])
			player1['hp'] -= damage
			print(' ** POW ** ')

			time.sleep(1)
			print(player2['name'], 'did', damage, 'damage!')
			print(player1['name'], 'hp:', player1['hp'])
	if player1['hp'] <= 0:
		print(player1['name'], 'fainted!')
		time.sleep(2)
		quit()
