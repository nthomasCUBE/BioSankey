#!/usr/bin/python3

#   ------------------------------------------------
#                   BIOSANKEY
#
#   Last modification: 16 february 2018
#
#   ------------------------------------------------

import csv
import sys

def parse_taxon_freq(c_f, threshold):
	levels={}
	freq={}
	prev={}

	na_cnt={}

	with open(c_f, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';', quotechar='\"')
		for vals in spamreader:
			if(len(vals)>1):
				cl=vals[1].split(";")
				for x in range(1,len(cl)):
					cs=0

					for y in range(2,len(vals)):
						c_v=float(vals[y].replace(",","."))
						cs=cs+c_v
					if(cs>threshold):
						if(cl[x]=="NA"):
							cl[x]=cl[x-1]+"_"+cl[x]
						if(freq.get(cl[x])==None):
							freq[cl[x]]=0
						if(levels.get(x)==None):
							levels[x]={}
						levels[x][cl[x]]=1
						prev[cl[x]]=cl[x-1]
						for y in range(2,len(vals)):
							c_v=float(vals[y].replace(",","."))
							freq[cl[x]]=freq[cl[x]]+c_v
	lv=list(levels.keys())
	lv.sort()
	cmd="data.addRows(["
	for lv_ in lv:
		gg=(levels[lv_].keys())
		for gg_ in gg:
			if(int(freq[gg_])>=0 and prev[gg_]!=gg_ ):
				cmd=cmd+"['%s','%s',%i]," % (prev[gg_],gg_,int(freq[gg_]))
	cmd=cmd+"]);"
	return(cmd)





