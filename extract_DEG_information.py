#!/usr/bin/python

import os
import sys

unit=["h","m","d","w"]

def get_all_deg():
	MAIN="DEG_information"
	files=os.listdir(MAIN)
	freq={}
	all={}
	for files_ in files:
		c_f=os.path.join(MAIN,files_)
		fh=file(c_f)
		for line in fh.readlines():
			line=line.strip()
			vals=line.split()
			cur_gene=vals[0]
			all[cur_gene]=1
	all=all.keys()
	return(all)

def DEG(r_id):
	fh=file("DEG_information/%s" % r_id)
	deg={}
	for line in fh.readlines():
		line=line.strip()
		vals=line.split()
		deg[vals[0]]=1
	return(deg.keys())

def get_diff(A,B,C):
	col=[]
	for A_ in A:
		if(not(A_ in B) and not(A_ in C)):
			col.append(A_)
	return col

def calc_intersect(A,B):
	col=[]
	for A_ in A:
		if(A_ in B):
			col.append(A_)
	return col
#
# ---------------------------------------------------------------------
#

all=get_all_deg()

map={}
map["2h_up"]=DEG("2h_up.dat")
map["2h_down"]=DEG("2h_down.dat")
map["2h_LC"]=get_diff(all,map["2h_up"],map["2h_down"])

print "2h_up",len(map["2h_up"])
print "2h_down",len(map["2h_down"])
print "2h_LC",len(map["2h_LC"])

#sys.exit()

map["6h_up"]=DEG("6h_up.dat")
map["6h_down"]=DEG("6h_down.dat")
map["6h_LC"]=get_diff(all,map["6h_up"],map["6h_down"])

map["16h_up"]=DEG("16h_up.dat")
map["16h_down"]=DEG("16h_down.dat")
map["16h_LC"]=get_diff(all,map["16h_up"],map["16h_down"])

map["24h_up"]=DEG("24h_up.dat")
map["24h_down"]=DEG("24h_down.dat")
map["24h_LC"]=get_diff(all,map["24h_up"],map["24h_down"])

#  ------------------------------------------------------

cmd=""

opt=["up","down","LC"]
for opt_ in opt:
	A=calc_intersect(map["2h_"+opt_],map["6h_up"])
	cmd=cmd+"[%s,%s,%i]" % ("'2h_"+opt_+"'","'6h_up'",len(A))+","
        A=calc_intersect(map["2h_"+opt_],map["6h_down"])
	cmd=cmd+"[%s,%s,%i]" % ("'2h_"+opt_+"'","'6h_down'",len(A))+","
        A=calc_intersect(map["2h_"+opt_],map["6h_LC"])
	cmd=cmd+"[%s,%s,%i]" % ("'2h_"+opt_+"'","'6h_LC'",len(A))+","

        A=calc_intersect(map["6h_"+opt_],map["16h_up"])
        cmd=cmd+"[%s,%s,%i]" % ("'6h_"+opt_+"'","'16h_up'",len(A))+","
        A=calc_intersect(map["6h_"+opt_],map["16h_down"])
        cmd=cmd+"[%s,%s,%i]" % ("'6h_"+opt_+"'","'16h_down'",len(A))+","
        A=calc_intersect(map["6h_"+opt_],map["16h_LC"])
        cmd=cmd+"[%s,%s,%i]" % ("'6h_"+opt_+"'","'16h_LC'",len(A))+","

        A=calc_intersect(map["16h_"+opt_],map["24h_up"])
        cmd=cmd+"[%s,%s,%i]" % ("'16h_"+opt_+"'","'24h_up'",len(A))+","
        A=calc_intersect(map["16h_"+opt_],map["24h_down"])
        cmd=cmd+"[%s,%s,%i]" % ("'16h_"+opt_+"'","'24h_down'",len(A))+","
        A=calc_intersect(map["16h_"+opt_],map["24h_LC"])
        cmd=cmd+"[%s,%s,%i]" % ("'16h_"+opt_+"'","'24h_LC'",len(A))+","

# ------------------------------------------------------

cmd="'up': [%s]]" % cmd
print cmd

cmd=cmd.replace("[","\n")
print cmd


#
# ---------------------------------------------------------------------
#

