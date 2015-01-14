import willie
import json

data_file = 'players.dat'
list = []

@willie.module.commands('addme')
def addme(bot, trigger):
	global list
	try:
		list = json.loads(open(data_file).read())
		open(data_file).close()
	except IOError as e:
		pass # we don't care if it doesn't exist
	name = trigger.nick
	if name in list:
		bot.say('%s You are already in line!' % (name))
	else:
		list.append(name)
		outfile = open(data_file, 'w')
		json.dump(list, outfile)
		outfile.close()
		bot.say('%s has been put in line!' % (name))
	#current = str(', '.join(list))
	#bot.say('Current list is: %s' % (current))
