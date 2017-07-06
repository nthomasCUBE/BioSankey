# BioSankey

BioSankey is a tool for generating Sankey plots from biological data. Sankey plots are suitable to show changes of counts or abundances over time (e.g. gene expression and abundances of microbial species). The plots are produced as an interactive Javascript HTML page and as static PDF plots. Multiple input formats are supported.

## Prerequisites

Python must be installed and a browser must be present, preferably a browser where JavaScript engine is particularely efficient.

## Installation

No particular installation is needed, just the files of this repository downloaded.

## Application

In order to generate a project-specific HTML, that allows to query data, either genes or DEG lists, it needs to run the python scripts

'python 0_make_html.py'

Furthermore, it needs to prepare the data in form, that it can be converted into transition as shown in the Sankeys Plot.


### Demo data

For demonstration purposes, we used the data from
Morandi, Elena, et al. "Gene expression time-series analysis of camptothecin effects in U87-MG and DBTRG-05 glioblastoma cell lines." Molecular cancer 7.1 (2008): 66.
containing expression information at six different timepoints: 2h, 6h, 16h, 24h, 48h, and 72h.

#### Format of input data:
- Genes divided in up- and down-regulated
or
- Abundances of genes or other entities (microbial species of a certain taxon, metabolites, ...)

It requires, that all timepoints of interest containing the genes and are also contained in the expression data lists.
E.g. Genes, that are upregulated at 16h and down-regulated would be summarized in the file: '16h_down.dat'.


## Questions and problems

If there are any issues and suggestions, please contact 
Alexander Platzer ( alexander.platzer AT univie.ac.at ) or Thomas Nussbaumer ( thomas.nussbaumer AT univie.ac.at )

## License
https://creativecommons.org/licenses/by/4.0/

