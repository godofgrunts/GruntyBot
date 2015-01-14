import willie
import json


playlist = 'play.dat'
charlist = 'characters.dat'
list =[]

@willie.module.commands('play')
def play(bot, trigger):
	global list
	with open(charlist) as f:
		choices = [line.rstrip() for line in f]
	
	try:
		list = json.loads(open(playlist).read())
		open(playlist).close()
	except IOError as e:
		pass

	input = trigger.group(2)
	char = input.lower()
	
	if (char in choices):
		if (char in list):
			bot.say('%s is already in line!' % (char))
		else:
			list.append(char)
			outfile = open(playlist, 'w')
			json.dump(list, outfile)
			outfile.close()
			bot.say('%s has been put in line!' % (char))
	else:
		bot.say('I do not understand \"%s\", please see http://pastebin.com/DigyBFDy for a list of names I do understand' % (char))
