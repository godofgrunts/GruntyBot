import willie
import json

data_file = 'players.dat'
list = []

@willie.module.commands('remove', 'r', 'delete')
def remove(bot, trigger):
	global list
	list = json.loads(open(data_file).read())
	name = trigger.group(2)
	if trigger.admin:
		open(data_file).close()
		if name in list:
			bot.say('%s is being removed from the list!' % (name))
			list.remove(name)
			outfile = open(data_file, 'w')
			json.dump(list, outfile)
			outfile.close()
		elif (name == None) and (list):
			first = list[0]
			bot.say('%s is being removed from the list!' % (first))
			list.remove(first)
			outfile = open(data_file, 'w')
			json.dump(list, outfile)
			outfile.close()
		else:
			bot.say('I did not find %s in the list.' % (name))
	else:
		nickname = str(trigger.nick)
		if nickname in list:
			bot.say('%s, you are removing yourself from the line!' % (nickname))
			list.remove(nickname)
			outfile = open(data_file, 'w')
			json.dump(list, outfile)
			outfile.close()
