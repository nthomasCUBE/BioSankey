# BioSankey
 
## What is BioSankey?

 BioSankey is a tool for generating Sankey plots from biological data either by using gene expression or microbical data. Sankey plots are suitable to show changes of counts or abundances over time (e.g. gene expression and abundances of microbial species). The plots are produced as an interactive Javascript HTML page and as static PDF plots. Multiple input formats are supported.
 
<p align="center">
 <img src="https://github.com/nthomasCUBE/BioSankey/blob/master/images/biosankey_11oct17.png" width="350"/>
</p>
 
 ## Prerequisites
 
 Python must be installed and a browser must be present, preferably a browser where JavaScript engine is particularly efficient.
 It was tested under Windows Python 3.6 and does not require additional dependencies except an internet connection to allow to integrate the Google API diagrams.
 
 ## Installation
 
 No particular installation is needed, just the files of this repository need to be downloaded.
 
 ## Application
 
 In order to generate a project-specific HTML, that allows to query data, either genes or DEG lists, it needs to run the python scripts

### GUI supported run

A user has to specific the needed files by choosing files from the Graphical User Inferface (starting biosankey.py).
There a user can upload expression information, domain information or microbial information.
 
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
 
 #### Picture export in high-quality
 In order to provide publication-ready images, we suggest to use PhantomJs, which allows to
 make a screenshot of the current webseite. [Link to PhantomJs](http://phantomjs.org/)
```
phantomjs-2.1.1-linux-i686/bin/phantomjs rasterize.js 'Use_case_combined.html' V1.png "100cm*80cm" 3
convert V1.png -trim V1x1.png
```
## Microbiome analysis

After the OTU Table has been added using the GUI and after clicking on the microbiome
Button, the BioSankey plot opens and the taxonomic groups are shown.

### Overall figure with total-counts per species summarizing all conditions together.

<p align="center">
 <img src="https://github.com/nthomasCUBE/BioSankey/blob/master/images/Figure1.png" width="1000"/>
</p>

### Detail view where each taxon shown over timepoints

<p align="center">
 <img src="https://github.com/nthomasCUBE/BioSankey/blob/master/images/Figure2.png" width="1000"/>
</p>

#### Excel to tab export

In order to export Excelt o tsv, we recommend to use [xlsx2tsv](https://gist.github.com/brendano/22764).


 ## Questions and problems
 
 If there are any issues and suggestions, please contact 
 Alexander Platzer ( alexander.platzer AT univie.ac.at ) or Thomas Nussbaumer ( thomas.nussbaumer AT univie.ac.at )
 
 ### Update (10/8/20)
 
 Now, we added 
```
 <script>
    google.charts.load('current', {packages: ['corechart','sankey']});
</script>
```
 to the existing code, so that BioSankey can still be used with Google Charts. Thanks for M. Mammel for observing this problem of changed
 loading of JS libraries.
 
 ### Update (03/9/20)
 
 For microbiome datasets, adding information when data is not correctly formatted
 
 ### Update (06/9/20)
 
Fixing height issue when displaying multiple OTUs.
 
 ## License
 https://creativecommons.org/licenses/by/4.0/
