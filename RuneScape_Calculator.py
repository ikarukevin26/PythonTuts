#!/usr/bin/pythonr

lifepoints = raw_input('How many lifepoints does the monter have?')
currentxp = raw_input('How much EXP do you have?')
desiredxp = raw_input('How much EXP do you want?')
if desiredxp > currentxp:
	print('You cannnot enter smaller value of desiredxp')

else:
	difference = int(desiredxp) - int(currentxp)
	monsterxp = int(lifepoints) * 0.4
	killcount = int(difference) / int(monsterxp)
	print 'You need to kill '+str(killcount)+' more monster with '+str(lifepoints)+' lifepoints.'
