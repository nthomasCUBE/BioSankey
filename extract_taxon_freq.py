import sys

def parse_taxon_freq(c_f):
	fh=open(c_f)
	levels={}
	freq={}
	prev={}
	for line in fh.readlines()[1:]:
		line=line.strip()
		vals=line.split()
		cl=vals[1].split(";")
		for x in range(1,len(cl)):
			if(freq.get(cl[x])==None):
				freq[cl[x]]=0
			if(levels.get(x)==None):
				levels[x]={}
			levels[x][cl[x]]=1
			prev[cl[x]]=cl[x-1]
			for y in range(2,len(vals)):
				freq[cl[x]]=freq[cl[x]]+float(vals[y])
	lv=list(levels.keys())
	lv.sort()
	cmd="data.addRows(["
	for lv_ in lv:
		gg=(levels[lv_].keys())
		for gg_ in gg:
			if(int(freq[gg_])>=25):
				cmd=cmd+"['%s','%s',%i]," % (prev[gg_],gg_,int(freq[gg_]))
	cmd=cmd+"]);"
	return(cmd)

#parse_taxon_freq("Use_case_4/UseCase4_HumanGut_sub_improved.txt")


