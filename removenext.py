import willie
import json

data_file = 'play.dat'
list = []

@willie.module.commands('removenext', 'rn', 'deletenext')
def remove(bot, trigger):
	global list
	list = json.loads(open(data_file).read())
	check = not list
	name = trigger.group(2)
	if trigger.admin:
		open(data_file).close()
		if name in list:
			bot.say('%s is being removed from the list!' % (name))
			list.remove(name)
			outfile = open(data_file, 'w')
			json.dump(list, outfile)
			outfile.close()
		elif (name == None) and (check == False):
			first = list[0]
			bot.say('%s is being removed from the list!' % (first))
			list.remove(first)
			outfile = open(data_file, 'w')
			json.dump(list, outfile)
			outfile.close()
		else:
			if check:
				bot.say('No one to remove you dummy.')
			else:
				bot.say('I did not find %s in the list.' % (name))
	else:
		bot.say('Only Admins can remove characters from the list!')
		
