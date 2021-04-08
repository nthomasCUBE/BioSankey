#!/usr/bin/python3

import csv
import extract_DEG_information
import extract_gene_expression
import extract_taxon_freq
import string
import ctypes
import sys

#   ------------------------------------------------
#                   BIOSANKEY
#
#   Last modification: 04 september 2020
#   03/09/20:   adding error message when microbiome input is not correctly formatted
#   06/09/20:	now Bacteria and Archae can be displayed, >1 nodes
#   ------------------------------------------------

def parse_html(EXPR_DIR, MIC_DIR, DEG_DIR, DOM_DIR, nmb_genes, THRESHOLD):


	fh=open("template/template_V3.txt")
	a=""
	for line in fh.readlines():
		a=a+line
	
	if(DEG_DIR!=None):
		a=a.replace("___BUTTON_DEG___","<button class=\"btn btn-default\" onclick=\"do_update('DEG')\">DEG categories</button>")
	else:
		a=a.replace("___BUTTON_DEG___","")
	if(EXPR_DIR!=None):
		a=a.replace("___BUTTON_GENES___","<button class=\"btn btn-default\" onclick=\"do_update('GENES')\">GENES</button>")
	else:
		a=a.replace("___BUTTON_GENES___","")
	if(MIC_DIR!=None):
		a=a.replace("___BUTTON_MICROBIOME___","<button class=\"btn btn-default\" onclick=\"microbiome_analysis('MICROBIOME')\">MICROBIOME</button>")
	else:
		a=a.replace("___BUTTON_MICROBIOME___","")

	map=""; my_opt2=""
	if(EXPR_DIR!=None):
		map,my_opt2=extract_gene_expression.run(EXPR_DIR)

	map2=""; map3="var map2={}"
	if(DEG_DIR!=None):
		map2,map3=extract_DEG_information.run(DEG_DIR,EXPR_DIR)

	domains={}; my_opt=""; my_dom=""
	if(DOM_DIR!=None):
		with open(DOM_DIR, 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
			i=0
			for vals in spamreader:
				if(len(vals)>1 and i>0):
					if(domains.get(vals[1])==None):
						domains[vals[1]]={}
					domains[vals[1]][vals[0]]=1
				i=i+1
		dk=list(domains.keys())
		dk.sort()
		for dk_ in dk:
			my_opt=my_opt+"<option>%s</option>" % dk_
			my_dom=my_dom+"'%s':'%s'," % (dk_,",".join(list(domains[dk_].keys())))
	tax_species=""
	my_org={}
	first_level={}
	map_add=""
	if(MIC_DIR!=None):
		my_otus={}; abund={}; nmb_cond=None
		with open(MIC_DIR, 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=';', quotechar='\"')
			i=0
			for vals in spamreader:
				i=i+1
				if(i>1 and len(vals)>1):
					org=vals[1].split(";")
					if(not(len(list(org))==6 or len(list(org))==7)):
						ctypes.windll.user32.MessageBoxW(0, "You need to provide the taxonomic profile seperated by ';' using six or seven taxonomic units. If only broader taxonomic units are known use (';;') (e.g. 'Bacteria;Pseudmonas;xx;xx;;;)", "Error",1)
						return;

					if(len(list(vals))>0):
						first_level[vals[1].split(";")[0]]=1
                                        
					for org_ in org:
						org_=org_.replace("\"","")
						if(my_org.get(org_)==None):
							my_org[org_]={}
						my_otus[vals[0]]=1
						my_org[org_][vals[0]]=1
						if(abund.get(vals[0])==None):
							abund[vals[0]]=[]
							for x in range(2,len(vals)):
								abund[vals[0]].append(vals[x])
							nmb_cond=len(vals)-2
		#if(len(list(first_level.keys()))!=1):
		#	ctypes.windll.user32.MessageBoxW(0, "Within the taxonomic pofile first entry has to be the same for all OTUs';' (e.g. 'Bacteria;xx;xx;xx;;;)", "Error",1)
		#	return

		cmd=cmd1
		for my_org_ in my_org:
			cmd=cmd+"'"+my_org_+"'"+":"+"'"+",".join(list(my_org[my_org_]))+"',"
		map_add=","
		for my_otus_ in my_otus:
			map_add=map_add+"'"+my_otus_+"':["
			for x in range(0,nmb_cond):
				map_add=map_add+"['%s','%s',%s]," % (my_otus_+"R"+str(x),my_otus_+"R"+str(x+1),abund[my_otus_][x].replace(",","."))
			map_add=map_add+"],"
		tax_species=cmd

	if(DEG_DIR!=None or MIC_DIR!=None):
		if(len(map_add)>0):
			a=a.replace("___EXPR_MAP___","var expr_map={"+map+"'up':["+map2+"]"+map_add+"}")
		else:
			a=a.replace("___EXPR_MAP___","var expr_map={"+map+"'up':["+map2+"]"+"}")
	else:
		a=a.replace("___EXPR_MAP___","var expr_map={"+map_add+"}")

	tax_species="var group_item_map={"+tax_species
	if(len(my_dom)>0):
		tax_species=tax_species+my_dom
	tax_species=tax_species+"}"
	if(len(tax_species)>0):
		a=a.replace("___TAXON_SPECIES_MAP___",tax_species)
	else:
		a=a.replace("___TAXON_SPECIES_MAP___","var ___TAXON_SPECIES_MAP___={}")

	a=a.replace("___MAP2___",map3)
	a=a.replace("___OPTIONS___",my_opt)
	a=a.replace("___OPTIONS2___",my_opt2)
	a=a.replace("___WIDTH___","800")
	a=a.replace("___HEIGHT___","800")
	a=a.replace("___MAX_GENES___",str(nmb_genes))

	if(MIC_DIR!=None):
		cmd=extract_taxon_freq.parse_taxon_freq(MIC_DIR,THRESHOLD)
		a=a.replace("____ENTRY____",cmd)
	else:
		a=a.replace("____ENTRY____","")
		
	fw=open("make_html.html","w"); fw.write(a); fw.close()
