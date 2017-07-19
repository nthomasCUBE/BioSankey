#!/usr/bin/python

#
#	This script groups genes into up-regulated, down-regulated and into LC (low-change)
#	which is then used to provide a global overview of the DEGs
#

import os
import sys
import string

def run(DEG_DIR, EXP_DIR):

	unit=["h","m","d","w"]
	def get_expr():
	        fh=file(EXP_DIR)
		p=0
		mm={}
		for line in fh.readlines():
			line=line.strip()
			vals=line.split()
			if(p==0):
				header=vals
			else:
				for x in range(2,len(vals)):
					if(mm.get(vals[0])==None):
						mm[vals[0]]={}
					mm[vals[0]][header[x]]=str(round(float(vals[x]),2))
			p=p+1
		return(mm)

	my_expr=get_expr()
	def get_all_deg():
		MAIN=DEG_DIR
		files=os.listdir(MAIN)
		freq={}
		all={}
		my_files={}
		for files_ in files:
			my_files[files_.split("_")[0]]=1
			c_f=os.path.join(MAIN,files_)
			fh=file(c_f)
			for line in fh.readlines():
				line=line.strip()
				vals=line.split()
				cur_gene=vals[0]
				all[cur_gene]=1
		all=all.keys()
		fk=my_files.keys()
		fk.sort()
		fk2={}
		for fk_ in fk:
			fk_short=fk_
			for unit_ in unit:
				fk_short=fk_short.replace(unit_,"")
			fk2[int(fk_short)]=fk_
		return(all),(fk2)

	def DEG(r_id):
		fh=file("%s/%s" % (DEG_DIR,r_id))
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

	(all,files)=get_all_deg()
	tpsort=files.keys()
	tpsort.sort()
	
	map={}
	for tpsort_ in tpsort:
		uid1="%s_up" % files[tpsort_]
		uid2="%s_down" % files[tpsort_]
		uid3="%s_LC" % files[tpsort_]
		map[uid1]=DEG(uid1+".dat")
		map[uid2]=DEG(uid2+".dat")
		map[uid3]=get_diff(all,map[uid1],map[uid2])
	
	def get_deg():
		cmd2=""
		for map_ in map:
			if(len(cmd2)==0):
				comma=""
			else:
				comma=","
		        cmd2=cmd2+comma+"'"+map_+"'"+":"+"'"+string.join(map[map_],",")+"'"
		cmd2="var map2={"+cmd2+"}"
		cmd=""
		opt=["up","down","LC"]
		for opt_ in opt:
			for x in range(0,len(tpsort)-1):
				A=calc_intersect(map[files[tpsort[x]]+"_"+opt_],map[files[tpsort[x+1]]+"_up"])
				cmd=cmd+"[%s,%s,%i]" % ("'"+files[tpsort[x]]+"_"+opt_+"'","'"+files[tpsort[x+1]]+"_up'",len(A))

	                        A=calc_intersect(map[files[tpsort[x]]+"_"+opt_],map[files[tpsort[x+1]]+"_down"])
	                        cmd=cmd+"[%s,%s,%i]" % ("'"+files[tpsort[x]]+"_"+opt_+"'","'"+files[tpsort[x+1]]+"_down'",len(A))

	                        A=calc_intersect(map[files[tpsort[x]]+"_"+opt_],map[files[tpsort[x+1]]+"_LC"])
	                        cmd=cmd+"[%s,%s,%i]" % ("'"+files[tpsort[x]]+"_"+opt_+"'","'"+files[tpsort[x+1]]+"_LC'",len(A))

		cmd=cmd.replace(",,",",").replace("][","],[")
		return cmd,cmd2
	return get_deg()
#get_deg()

