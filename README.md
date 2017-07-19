# BioSankey
 
 BioSankey is a tool for generating Sankey plots from biological data either by using gene expression or microbical data. Sankey plots are suitable to show changes of counts or abundances over time (e.g. gene expression and abundances of microbial species). The plots are produced as an interactive Javascript HTML page and as static PDF plots. Multiple input formats are supported.
 
 ## Prerequisites
 
 Python must be installed and a browser must be present, preferably a browser where JavaScript engine is particularly efficient.
 
 ## Installation
 
 No particular installation is needed, just the files of this repository need to be downloaded.
 
 ## Application
 
 In order to generate a project-specific HTML, that allows to query data, either genes or DEG lists, it needs to run the python scripts

### Run1 - Timeseries data of camptothecin effect
```
'python 0_make_html.py expr=Use_case_1/extract_genes.txt deg=Use_case_1/DEG_information dom=Use_case_1/1_extract_domains.txt > Use_case_1.html'
```
### Run2 - Randomly generated OTUs clustering visualisation
```
'python 0_make_html.py expr=$tmp mic=$tmp > Use_case_2.html'
```

 Furthermore, it needs to prepare the data in form, that it can be converted into transition as shown in the Sankeys Plot.
 
 
 ### Demo data
 
 For demonstration purposes, we used the data from
 [Morandi, Elena, et al. "Gene expression timeseries analysis of camptothecin effects in U87MG and DBTRG05 glioblastoma cell lines." Molecular cancer 7.1 (2008): 66.](https://www.ncbi.nlm.nih.gov/pubmed/18694480)
 containing expression information at six different timepoints: 2h, 6h, 16h, 24h, 48h, and 72h. 
 
 We also added an use case (Use case 2) where we included OTU from [Caporaso JG, Lauber CL, Costello EK, Berg-Lyons D, Gonzalez A, Stombaugh J, Knights D, Gajer P, Ravel J, Fierer N, Gordon JI, and Knight R. 2011. Moving pictures of the human microbiome. Genome Biol 12:R50. 10.1186/gb-2011-12-5-r50](https://www.ncbi.nlm.nih.gov/pubmed/21624126)
 
 #### Format of input data:
  Genes divided in up and downregulated
 or
  abundances of genes or other entities (microbial species of a certain taxon, metabolites, ...)
 
 It requires, that all timepoints of interest containing the genes and are also contained in the expression data lists.
 E.g. genes, that are upregulated at 16h and downregulated would be summarized in the file: '16h_down.dat'.
 
 
 ## Questions and problems
 
 If there are any issues and suggestions, please contact 
 Alexander Platzer ( alexander.platzer AT univie.ac.at ) or Thomas Nussbaumer ( thomas.nussbaumer AT univie.ac.at )
 
 
 ## License
 https://creativecommons.org/licenses/by/4.0/
