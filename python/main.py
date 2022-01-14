TXTFILE = "player.csv"

fd = open(TXTFILE, "r")
data = fd.read()
fd.close()

lisData = data.split("\n")

for data in lisData:
	data2 = data.split("\t")
	print("{")
	print('	"playerName" : "' + data2[0] + '",')
	print('	"playerText" : "' + data2[1] + '",')
	print('	"TwitterLnk" : "' + data2[2] + '",')
	if (data2[3] == "ダイヤ"):
		print('	"MaxRanked" : "' + "d" + '"')
	elif (data2[3] == "マスター"):
		print('	"MaxRanked" : "' + "m" + '"')
	elif (data2[3] == "プレデター"):
		print('	"MaxRanked" : "' + "p" + '"')
	else:
		print('	"MaxRanked" : "' + "n" + '"')
	print("},")
