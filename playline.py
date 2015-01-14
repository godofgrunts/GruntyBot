import willie
import json

data_file = 'play.dat'
list = []

@willie.module.commands('next')
@willie.module.rate(30)
def next(bot, trigger):
	global list
	try:
		list = json.loads(open(data_file).read())
		open(data_file).close()
	except IOError as e:
		pass # we don't care if it doesn't exist
	current = str(', '.join(list))
	bot.say('Current line is: %s' % (current))
