#!/usr/bin/python3

#   ------------------------------------------------
#                   BIOSANKEY
#
#   Last modification: 16 february 2018
#
#   ------------------------------------------------

import csv
import extract_gene_expression
import sys

def run(EXP_DIR):
	def get_expression():
		header=None
		try:
			fh=open(EXP_DIR)
			p=0; cmd=""; cmd2=""
			with open(EXP_DIR, 'r') as csvfile:
				spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
				for vals in spamreader:
					if(p==0):
						header=["start"]
						for vals_ in vals:
							if(len(vals_)>0):
								header.append(vals_)
					elif(len(vals)>1):
						cmd=cmd+"'%s':[" % vals[0]
						for x in range(1,len(header)-1):
							comma=""
							if(x!=(len(header)-1)):
								comma=","
							cmd=cmd+"['%s','%s',%s]%s" % (vals[0]+"_"+header[x],vals[0]+"_"+header[x+1],str(round(float(vals[x].replace(",",".")),2)),comma)
						cmd=cmd+"],"
						cmd2=cmd2+"<option>"+vals[0]+"</option>"
					p=p+1
		except Exception:
			pass
		return(cmd,cmd2)
	return get_expression()

