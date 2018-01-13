import dota2api
apikey= #your api key here
api = dota2api.Initialise(apikey)
match = api.get_match_details(match_id=3638312745)
heroesList=api.get_heroes().get('heroes')
matchHeroes=[]
for i in range(0,10):
	hid=match.get('players')[i].get('hero_id')
	for hero in heroesList:
		if(hero.get('id')==hid):
			name=hero.get('name')
			break
	matchHeroes.append(name)


f = open("ehome.txt","r")  
lines = f.readlines()

dictList=[]

for i in range(len(lines)):
	line=lines[i]
	if(line.startswith('\tvalue')):
		lines[i+1]='\tendvalue'+lines[i+1][6:]
	if(line=='{\n'):
		dict={}
		continue
	if(line=='}\n'):
		dictList.append(dict)
		continue
	stringList=line.split(':')
	dict[stringList[0][1:len(stringList[0])]]=stringList[1][1:len(stringList[1])-1]

i=0
n=0
dict={}
for i in range(10):
	for j in range(10):
		dict[matchHeroes[i][14:]+' to '+matchHeroes[j][14:]]=0

while(i<len(dictList)):
	if(dictList[i].get('type')=='0' and dictList[i].get('is_target_illusion')=='0'):
		attacker=dictList[i].get('damage_source')
		death=dictList[i].get('target')
		n=0
		for name in matchHeroes:
			if(str(attacker).find(name[14:])!=-1):
				n=n+1
				attacker=name
			if(death==name):
				n=n+1
		if(n==2):
			dict[attacker[14:]+' to '+death[14:]]=dict[attacker[14:]+' to '+death[14:]]+int(dictList[i].get('value'))								
	i=i+1

for i in range(10):
	for j in range(10):
		if(i==j or dict.get(matchHeroes[i][14:]+' to '+matchHeroes[j][14:])==0):
			dict.pop(matchHeroes[i][14:]+' to '+matchHeroes[j][14:])

print(dict)




