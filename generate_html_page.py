#!/usr/bin/python

import sys

a="""
<html>
<head>
<style>
h1 {
    color: red;
	font-family: Arial;
	color: blue;
	font-size:28px;
}
h2 {
	color:	green;
	font-family: Arial;
	font-size:12px;
}
body {
    background-color: #111111ff;
}
p {
    border: 1px solid powderblue;
}
textarea#textarea1 {
	width: 600px;
	height: 120px;
	border: 3px solid #cccccc;
	padding: 5px;
	font-family: Tahoma, sans-serif;
	background-position: bottom right;
	background-repeat: no-repeat;
	font-size:15px;
}
</style>
</head>
<body>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<h1>BioSankey - Exploring variants and microbiomes along different timepoints</h1>
<p>
<h2>Please insert variants/genes, which should be displayed</h2>
<textarea name="textarea1" id="textarea1" onfocus="this.value=''; ">You can select either 'all' or 'A1', 'A5', or 'A9'.
If more genes should be visualized, please seperate them by a comma.</textarea>
</textarea>
<button onclick="do_update()">Select</button>
</p>

<div id="sankey_multiple" style="width: 900px; height: 300px;"></div>
<script type="text/javascript">
  google.charts.load("current", {packages:["sankey"]});
  google.charts.setOnLoadCallback(drawChart);
    var data;
	var chart;
	var map = {
	___XXX___
	}

    function do_update(){
 	data= new google.visualization.DataTable();
    data.addColumn('string', 'From');
    data.addColumn('string', 'To');
    data.addColumn('number', 'Weight');

	var cur_vals=document.getElementById('textarea1').value;
	cur_vals = cur_vals.split(',');
	for(var cur_val in cur_vals){
		cur_val=cur_vals[cur_val];
		if(cur_val=="all"){
			for(var key in map){
				data.addRows(map[key])
			}
		}else{
			data.addRows(map[cur_val]);
		}
	}

    var options = {
      width: 600,
    };
    chart = new google.visualization.Sankey(document.getElementById('sankey_multiple'));
    chart.draw(data, options);
   }

   function drawChart() {
	data= new google.visualization.DataTable();
   data.addColumn('string', 'From');
    data.addColumn('string', 'To');
    data.addColumn('number', 'Weight');
		data.addRows([])
    var options = {
      width: 600,
    };
    chart = new google.visualization.Sankey(document.getElementById('sankey_multiple'));
    chart.draw(data, options);
   }
</script>
<hr>
<h2>Citation</h2>
Platzer Alexander, ..... BioSankey - another useless tool...
</body>
</html>
"""

tmp="""
"A1": [['A1','B1',595],  ['B1','C1',1],['C1','D1',55],['D1','E1',3389]],
"A5": [['A5','B5',100], ['B5','C5',200], ['B5','C5',300],['C5','D5',400]],
"gene1": [['1h','3h',595], ['3h','6h',500], ['6h','10h',0.00000000000000000001],['10h','15h',55],['15h','20h',3389]],
"sulfure": [['XX','YY',595], ['YY','ZZ',500], ['ZZ','OO',55],['OO','PP',355]]
"""

a=a.replace("___XXX___",tmp)

fh=file("Use_case_2/extract_genes.txt")
p=0
for line in fh.readlines()[1:]:
	line=line.strip()
	vals=line.split()
	p=p+1
	cmd=""
	for x in range(1,len(vals)):
		cmd=cmd+"[%s,%s,%s]" % ("\"t"+str(x-1)+"_"+str(p)+"\"","\"t"+str(x)+"_"+str(p)+"\"",vals[x])
		if(x<(len(vals)-1)):
			cmd=cmd+","
	xx="\"%s\": [%s]" % (vals[0],cmd)
	xx=xx+","
	print(xx)

fw=file("0_make_html.html","w")
fw.write(a)
fw.close()


