import sys, csv
import random
import copy
import numpy as np
from datetime import datetime , timedelta
import time

def CreateMat(Data, Start, Size):
	Matrix= np.zeros(shape=(Size,Size),dtype=float)
	for i in range(Size):
		Matrix[i]=Data[i+Start]

	return Matrix

def CreateSet(ID,datalist,line):
	ID={}
	Matrix=[]
	if str(line[4]) not in ID.keys():
		ID["Start Time"]=line[2]
		ID["End Time"]=line[3]
		ID[str(line[4])]=[]
		index=datalist.index(line)
		length=len(datalist[index+1])
		start=index+1
		Matrix=CreateMat(datalist,start,length)
		ID[str(line[4])].append(Matrix)
	
	return ID

def AddtoSet(ID,datalist,line):
	if str(line[4]) not in ID.keys():
		ID[str(line[4])]=[]
		index=datalist.index(line)
		length=len(datalist[index+1])
		start=index+1
		Matrix=CreateMat(datalist,start,length)
		ID[str(line[4])].append(Matrix)
	
	return ID

def CreateMasterData(file):
	FIn=open(file,"r")
	Data=FIn.readlines()
	DataList=[]
	for line in Data:
		ALine=line.replace('\t',',')
		BLine=ALine.replace('\n','')
		SLine=BLine.split(',')
		DataList.append(SLine)
	MasterData={}
	for line in DataList: 
		if line[0].startswith('+'):
			if 'ZoneList' not in MasterData.keys():
				ZoneList=[]
				ZoneList.append(line)
				MasterData['ZoneList']=[ZoneList]
		if line[0].startswith('>'):
			if line[1] not in MasterData.keys():
				set=CreateSet(line[1],DataList,line)
				MasterData[line[1]]=set
			if line[1] in MasterData.keys():
				AddtoSet(MasterData[line[1]],DataList,line)

	return MasterData
	

Hash=CreateMasterData(sys.argv[1])
print(Hash)