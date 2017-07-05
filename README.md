# BioSankey

In order to generate a project-specific HTML, that allows to query data, either genes or
DEG lists, it needs to run the python scripts

'python 0_make_html.py' 

Furthermore, it needs to prepare the data in form, that it can be converted into transistion as
shown in the Sankey Plot.

## Expression Data

In order to demonstrate our tool, we have used six timepoints from the xxxx containing expression information
at six different timepoints: 2h, 6h, 16h, 24h, 48h, and 72h.

gene 2h 6h 16h 24h 48h 72h
LOC85028 33.6640162906 224.864142649 104.933678522 196.823768568 110.577118386 73.6416283113
ADK 77.9486373526 97.1801439103 43.8822760402 19.4820590989 15.1056264096 11.3466875369
H2BFB 126.109542051 103.670436269 101.373106832 44.9252898223 106.830906619 245.550872708
RAB6KIFL 73.4032444381 51.2443216327 35.0796530692 46.8037989271 28.9281668082 14.046483472
ADK 74.9655792777 91.7676343874 53.7275841454 21.1775332833 24.921695745 21.5779033788
NMI 101.449831015 98.9180127105 121.623283413 243.502632445 144.036383344 131.323016935
UBE2C 96.2759479343 78.1783979501 40.4077778918 34.4460033771 21.8029852429 8.85008849816

## Differential gene expression analysis

In addition, in order to get an idea of the differentially expressed genes, we have prepared inputs
to alos integrate these information into the visualisation.
For this reason we require, that for the genes are grouped into up and down regulated and per timepoints.
This makes it possible to also group genes into LC (low .xxxxx).
Figure 1 in the publication demonstrate the plot.

It requires, that all timepoints of interest are contianing the genes and also that these genes are also within
the expression data lists.

e.g. genes that are upregulated at 16h and down-regulated would be summarized in the file: '16h_down.dat'

## Questions and problems

If there are any issues and suggestions, please contact Alexander Platzer or Thomas Nussbaumer using the following
email addresses: thomas.nussbaumer AT univie.ac.at and alexander.platzer AT univie.ac.at

