
import sys, csv
import random
import copy
import numpy as np
from datetime import datetime , timedelta
import time

def SmallRandomFileCreator(FileIn,FileOut,pi):
    FIn=open(FileIn,"r")
    FOut=open(FileOut,"w")
    reader=csv.reader(FIn)
    writer=csv.writer(FOut)
    for row in reader:	
        r=random.random()
        if r<=pi:
            writer.writerow(row)


def CreateZoneList(File):
    FIn=open(File,"r")
    reader=csv.reader(FIn)
    next(reader, None)
    ZoneList=[]
    for row in reader:
        if int(row[4]) not in ZoneList:
            ZoneList.append(int(row[4]))
        if int(row[5]) not in ZoneList:
            ZoneList.append(int(row[5]))

    return ZoneList
a=CreateZoneList(sys.argv[1])
print(len(a))


def CreateEmptySquareMatrix(n):
    Matrix= np.zeros(shape=(n,n),dtype=float)   
    return Matrix

def WriteTextMatrix(matrix,outfile):

	for i in range(len(matrix)):
		row=[]
		for j in range(len(matrix)):
			row.append(matrix.item((i,j)))
		str_row=str(row)[1 : -1]
		print(str_row,file=outfile)


def GetDateTime(Str):
	return datetime.strptime(Str, "%Y-%m-%d %H:%M:%S")


def GetTime(Str):
    t=datetime.strptime(Str, "%H:%M:%S")
    return datetime.time(t)


def ValidTimeRow(row,start,end):
    dt=GetDateTime(row[0])
    T=datetime.time(dt)
    StartTime=GetTime(start)
    EndTime=GetTime(end)
    if T>StartTime and T<EndTime:
        return True

#Variable code: Duration = 2 , Fare = 6, tip = 7 Total(Fare+tip+tolls) = 8
#n is row m is column
def CreateZoneTimeMatrixToCSV(InFile,Outfile,StartTime,EndTime,ID):
	FIn=open(InFile,"r")
	reader=csv.reader(FIn)
	next(reader, None)
	ZoneList=CreateZoneList(InFile)
	MatrixFareTotal=CreateEmptySquareMatrix(len(ZoneList))
	MatrixCounter=CreateEmptySquareMatrix(len(ZoneList))
	MatrixDurationTotal=CreateEmptySquareMatrix(len(ZoneList))
	for row in reader:
		vr=ValidTimeRow(row,StartTime,EndTime)
		if vr == True:
			n=ZoneList.index(float(row[4]))
			m=ZoneList.index(float(row[5]))
			MatrixFareTotal[n][m] += float(row[8])
			MatrixCounter[n][m]+=1
			MatrixDurationTotal[n][m]+= float(row[2]) 
	MatrixAveFare=np.divide(MatrixFareTotal,MatrixCounter,out=np.zeros_like(MatrixFareTotal),where=MatrixCounter!=0)
	MatrixAveDuration=np.divide(MatrixDurationTotal,MatrixCounter,out=np.zeros_like(MatrixDurationTotal),where=MatrixCounter!=0)
	FOut=open(Outfile,"w")
	str_row=str(ZoneList)[1 : -1]
	print("+\t", str_row,file=FOut)
	row = ">\t%s\t%s\t%s\tAverage Fare" % (ID, StartTime, EndTime)
	print(row,file=FOut)
	WriteTextMatrix(MatrixAveFare,FOut)
	row = ">\t%s\t%s\t%s\tAverage Duration" % (ID, StartTime, EndTime)
	print(row,file=FOut)
	WriteTextMatrix(MatrixAveDuration,FOut)
	row = ">\t%s\t%s\t%s\tCounter" % (ID, StartTime, EndTime)
	print(row, file=FOut)
	WriteTextMatrix(MatrixCounter,FOut) 
	FOut.close()
	return FOut

	

	


	


#CreateZoneTimeMatrixToCSV(sys.argv[1],"test2.txt","10:00:00","11:00:00","000")
#CreateZoneTimeMatrixToCSV(sys.argv[1],"test1.csv","11:00:00","12:00:00","001")
#CreateZoneTimeMatrixToCSV(sys.argv[1],"test2.csv","12:00:00","13:00:00","002")

CreateZoneTimeMatrixToCSV(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])


def LoadMatrixfromtxt(file):
	M=np.loadtxt(file,delimiter=',')
	print(M)
	return M

#LoadMatrixfromtxt("Output.txt")