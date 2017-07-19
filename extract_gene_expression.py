#!/usr/bin/python

#
#	This script allows to generate the input necessary to
#	generate the Google Sankey Plot
#

import extract_gene_expression
import sys

def run(EXP_DIR):
	def get_expression():
		header=None
		fh=file(EXP_DIR)
		p=0
		cmd=""
		for line in fh.readlines():
			line=line.strip()
			vals=line.split()
			if(p==0):
				header=vals
			elif(len(vals)>1):
				cmd=cmd+"'%s':[" % vals[0]
				for x in range(2,len(vals)-1):
					comma=""
					if(x!=(len(vals)-2)):
						comma=","
					cmd=cmd+"['%s','%s',%s]%s" % (vals[0]+"_"+header[x],vals[0]+"_"+header[x+1],str(round(float(vals[x]),2)),comma)
				cmd=cmd+"],"
			p=p+1
		return(cmd)
	return get_expression()

