def CreateLine(scheduleline):
	Format='SPORTNGIN'
	temp=StartEndTime(scheduleline[2])
	starttime=temp[0]
	endtime=temp[1]
	Start_Date_time = scheduleline[1] +i ' ' +  starttime
	End_Date_Time = scheduleline[1] + ' ' + endtime
	Title = "SCVHA Practice - "+ str(scheduleline[4]) + ' '+ str(scheduleline[5])
	Description = "SCVHA Practice - "  + str(scheduleline[4]) + ' ' +  str(scheduleline[5])
	Location = str(scheduleline[3])
	Location_URL=''
	All_Day_Event = str(0) 
	Event_Type = "Practice"
	Tags=''
	Team1_ID=''
	Team1_Is_Home=''
	Team2_Name=''
	Event_ID=''

	header = Format,Start_Date_time,End_Date_Time,Title,Description,Location,Location_URL,All_Day_Event,Event_Type,Tags,Team1_ID,Team1_Is_Home,Team2_Name,Event_ID
	out = '' 
	for e in header:
		out = str(out) + str(e) + ','
	print out	
	return out


def StartEndTime(origtime):
	#Still need to midiy this to return 24h time 
	import re

	timetemp = origtime.split("-")

	m=re.search('[aApP][Mm]',timetemp[1])

	ampm=m.group(0)

	timetemp[0] = timetemp[0] + ampm
	
	return timetemp


f = open('orig.csv','r')
out = open('out.csv','w')

header ="""Format,Start_Date_time,End_Date_Time,Title,Description,Location,Location_URL,All_Day_Event,Event_Type,Tags,Team1_ID,Team1_Is_Home,Team2_Name,Event_ID"""

out.write(header) 
out.write('\n')

for line in f.read().splitlines(True):
	scheduleline = []
	for word in line.split(','):
		scheduleline.append(word.rstrip('\n'))
	temp = CreateLine(scheduleline)
	out.write(temp)	
	out.write('\n')

f.close()
out.close()

