import sys
import string
import extract_gene_expression
import extract_DEG_information
import extract_taxon_freq

#
#	Parses the input files that were provided by the user
#
def parse_html(EXP_DIR_, MIC_DIR_, DEG_DIR_, DOM_DIR_):
	fh=open("template/template_V2.txt")
	a=""
	for line in fh.readlines():
		a=a+line
	vals=sys.argv
	expr_f=False; deg_f=False; dom_f=False; mic_f=False
	EXP_DIR=None; MIC_DIR=None; DEG_DIR=None; DOM_DIR=None

	if(EXP_DIR_!=None):
		EXP_DIR=EXP_DIR_; expr_f=True
	if(MIC_DIR_!=None):
		MIC_DIR=MIC_DIR_; mic_f=True
	if(DOM_DIR_!=None):
		DOM_DIR=DOM_DIR_; dom_f=True
	if(DEG_DIR_!=None):
		DEG_DIR=DEG_DIR_; deg_f=True
	
	if(deg_f==True):
		a=a.replace("___BUTTON_DEG___","<button class=\"btn btn-default\" onclick=\"do_update('DEG')\">DEG categories</button>")
	else:
		a=a.replace("___BUTTON_DEG___","")
	if(expr_f==True):
		a=a.replace("___BUTTON_GENES___","<button class=\"btn btn-default\" onclick=\"do_update('GENES')\">GENES</button>")
	else:
		a=a.replace("___BUTTON_GENES___","")
	if(mic_f==True):
		a=a.replace("___BUTTON_MICROBIOME___","<button class=\"btn btn-default\" onclick=\"do_update4('MICROBIOME')\">MICROBIOME</button>")
	else:
		a=a.replace("___BUTTON_MICROBIOME___","")
	if(expr_f==False and mic_f==False):
			print("ERROR\texpression file missing")
			print("USAGE: python 0_make_html.py expr=Use_case_1/extract_genes.txt (deg=Use_case_1/DEG_information) dom=Use_case1/DOM_information.txt")
			print("")
			print(" expr... requires a text file containing  the expression information per gene")
			print(" deg...  the relative or absolute path to the deg in pairwise comparison of timepoint")
			print(" dom...  the domain information or functional annotation in general for genes that are integrated")
			sys.exit()
	if(EXP_DIR!=None):
		map,my_opt2=extract_gene_expression.run(EXP_DIR)
	if(deg_f==True):
			map2,map3=extract_DEG_information.run(DEG_DIR,EXP_DIR)
	else:
			map2=""
			map3="var map2={}"
	domains={}
	my_opt=""
	my_dom=""
	if(dom_f==True):
		fh=open(DOM_DIR)
		domasins={}
		for line in fh.readlines()[1:]:
			line=line.strip()
			vals=line.split()
			if(len(vals)>1):
				if(domains.get(vals[1])==None):
					domains[vals[1]]={}
				domains[vals[1]][vals[0]]=1
		dk=list(domains.keys())
		dk.sort()
		for dk_ in dk:
			my_opt=my_opt+"<option>%s</option>" % dk_
			my_dom=my_dom+"'%s':'%s'," % (dk_,",".join(list(domains[dk_].keys())))
	tax_species=""
	if(mic_f==True):
		pass
		fh=open(MIC_DIR)
		my_org={}
		for line in fh.readlines():
			line=line.strip()
			vals=line.split()
			org=vals[1].split(";")
			for org_ in org:
				if(my_org.get(org_)==None):
					my_org[org_]={}
				my_org[org_][vals[0]]=1
		cmd="var tax={"
		for my_org_ in my_org:
			cmd=cmd+"'"+my_org_+"'"+":"+"'"+",".join(list(my_org[my_org_]))+"',"
		cmd=cmd+"}"
		tax_species=cmd
	if(deg_f==True or mic_f==True):
		a=a.replace("___MAP___","var map={"+map+"'up':["+map2+"]"+"}")
	else:
			a=a.replace("___MAP___","var map={}")
	if(len(tax_species)>0):
		a=a.replace("___TAXON_SPECIES_MAP___",tax_species)
	else:
		a=a.replace("___TAXON_SPECIES_MAP___","var tax={}")
	a=a.replace("___MAP2___",map3)
	a=a.replace("___OPTIONS___",my_opt)
	a=a.replace("___OPTIONS2___",my_opt2)
	a=a.replace("___MAP3___","var map2={%s}" % my_dom)
	a=a.replace("___WIDTH___","800")
	a=a.replace("___HEIGHT___","800")
	if(mic_f==True):
		cmd=extract_taxon_freq.parse_taxon_freq(MIC_DIR)
		a=a.replace("____ENTRY____",cmd)
	else:
		a=a.replace("____ENTRY____","")
	fw=open("make_html.html","w")
	fw.write(a)
	fw.close()


#EXP_DIR_="C:/Users/nussbath/Google Drive/BIOSANKEY_RESUBMISSION/BioSankey-0.2/BioSankey-0.2/GUI_Use_case_1/Expression.txt"
#MIC_DIR_="C:/Users/nussbath/Google Drive/BIOSANKEY_RESUBMISSION/BioSankey-0.2/BioSankey-0.2/GUI_Use_case_1/Microbial.txt"
#DEG_DIR_="C:/Users/nussbath/Google Drive/BIOSANKEY_RESUBMISSION/BioSankey-0.2/BioSankey-0.2/GUI_Use_case_1/DEGs"
#DOM_DIR_="C:/Users/nussbath/Google Drive/BIOSANKEY_RESUBMISSION/BioSankey-0.2/BioSankey-0.2/GUI_Use_case_1/Domains.txt"
#parse_html(EXP_DIR_, MIC_DIR_, DEG_DIR_, DOM_DIR_)



