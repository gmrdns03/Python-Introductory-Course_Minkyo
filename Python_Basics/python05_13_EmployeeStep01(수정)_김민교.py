TName = ["구분","사원명","입사일","급여"]

empInfo = [
	['T160501',"캔디","2016-05-10"],
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]

empPayTable = [
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]
]

Rable = [ '계약직', '정규직']

print('%-6s %-3s %8s %7s'% (TName[0], TName[1], TName[2], TName[3]))
print('-'*42)


for i in range(len(empInfo)):
	if empInfo[i][0][0] =='T' or empInfo[i][0][0] =='t':
		print("{0} \t {1} \t {2} \t {3:,d}".format(Rable[0], empInfo[i][1], empInfo[i][2], (empPayTable[i][0]*empPayTable[i][1])))
	if empInfo[i][0][0] =='R' or empInfo[i][0][0] =='r':
		print("{0} \t {1} \t {2} \t {3:,d}".format(Rable[1], empInfo[i][1], empInfo[i][2], (empPayTable[i][0]*empPayTable[i][1])))
