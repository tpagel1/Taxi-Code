
import sys, csv
import random
import copy
import numpy as np
from datetime import datetime , timedelta
import time
import matplotlib.pyplot as plt
from CreateMatrixHash import CreateMasterData

def CreateZoneKey(file):
	FIn=open(file,"r")
	Data=FIn.readlines()
	DataList=[]
	for line in Data:
		SLine=line.split('\t')
		DataList.append(SLine)
	ZoneKey={}
	for line in DataList:
		if line[0] not in ZoneKey.keys():
			Ad1=line[2]
			Ad2=line[1]
			Key="%s, %s" % (Ad1, Ad2)
			ZoneKey[int(line[0])]=Key
	return ZoneKey

def GetSum(ID,Zone):
	i=MasterData['ZoneList'].index(Zone)
	matrix=MasterData[ID]['Counter']
	sum=(np.sum(matrix[i])/365)
	return sum

def GetID(num):
	ID="%03d" %num
	return ID

def FreqList(Zone):
	FreqbyTime=[]
	for num in range(48):
		ID=GetID(num)
		freq=GetSum(ID,Zone)
		FreqbyTime.append(freq)
	return FreqbyTime

def GetAreaName(zone):
	Area=ZoneKey[zone]
	return Area

def MakePlot(zone):
	FName="ZoneNumber-%05d" %zone
	Title=GetAreaName(zone)
	X=FreqList(zone)
	plt.plot(X)
	plt.ylabel('Frequency')
	plt.xlabel('Time')
	plt.title(Title)
	plt.savefig(FName)
	plt.close()

def MakeMasterPlot(list):
	for zone in list:
		X=FreqList(zone)
		plt.plot(X)
		plt.ylabel('Frequency')
		plt.xlabel('Time ID (48 30 minute periods)')
		plt.title('All Zones')
		plt.savefig('Master')

def CreateEmptySquareMatrix(n):
    Matrix= np.zeros(shape=(n,n),dtype=float)   
    return Matrix

MasterData=CreateMasterData("All.txt")
ZoneKey=CreateZoneKey("ZoneNames.txt")
print(ZoneKey)
print(MasterData)
#for zone in MasterData['ZoneList']:
	#MakePlot(zone)
#MakeMasterPlot(MasterData['ZoneList'])

matrix=(MasterData['000']['Counter']/365)
matrix2=MasterData['000']['Average Fare']
matrix3=CreateEmptySquareMatrix(len(matrix))

for i in range(len(matrix)):
	sum=np.sum(matrix[i])
	weight=np.divide(matrix[i],sum,out=np.zeros_like(matrix[i]),where=matrix[i]!=0)
	row=matrix2[i]*weight
	for y in range(len(matrix)):
		matrix3[i][y]+=(row[y])

Probability=CreateEmptySquareMatrix(len(matrix))
for x in range(len(matrix)):
	for y in range(len(matrix)):
		if matrix[x][y]<=1:
			Probability[x][y]+=float(matrix[x][y])
		else:
			Probability[x][y]+=1
print(matrix)
print(Probability)

matrix3=np.multiply(matrix3,Probability)

PayoffPUL=[]
for x in range(len(matrix3)):
	payoff=np.sum(matrix3[x])
	PayoffPUL.append(payoff)
#print(PayoffPUL)
#MakeMasterPlot(MasterData['ZoneList'])