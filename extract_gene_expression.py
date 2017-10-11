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
		fh=open(EXP_DIR)
		p=0
		cmd=""
		cmd2=""
		for line in fh.readlines():
			line=line.strip()
			vals=line.split()
			if(p==0):
				header=["start"]
				for vals_ in vals:
					header.append(vals_)
			elif(len(vals)>1):
				cmd=cmd+"'%s':[" % vals[0]
				for x in range(1,len(vals)):
					comma=""
					if(x!=(len(vals)-1)):
						comma=","
					cmd=cmd+"['%s','%s',%s]%s" % (vals[0]+"_"+header[x],vals[0]+"_"+header[x+1],str(round(float(vals[x]),2)),comma)
				cmd=cmd+"],"
				cmd2=cmd2+"<option>"+vals[0]+"</option>"
			p=p+1
		return(cmd,cmd2)
	return get_expression()

