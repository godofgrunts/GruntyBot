import willie
import json

data_file = 'players.dat'
list = []

@willie.module.commands('line')
@willie.module.rate(30)
def addme(bot, trigger):
	global list
	try:
		list = json.loads(open(data_file).read())
		open(data_file).close()
	except IOError as e:
		pass # we don't care if it doesn't exist
	current = str(', '.join(list))
	bot.say('Current line is: %s' % (current))
