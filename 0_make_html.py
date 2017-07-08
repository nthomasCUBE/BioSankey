import sys
import extract_gene_expression
import extract_DEG_information

a="""
<html>
<head>
<noscript>JavaScript is needed for BioSankey</noscript>
<style>
h1 {
    color: red;
        font-family: Arial;
        color: blue;
        font-size:28px;
}
h2 {
        color:        green;
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
        height: 80px;
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
<a href="javascript:location.reload(true)">Refresh this page</a>
<p>
<h2>Please insert variants/genes, which should be displayed</h2>
<textarea name="textarea1" id="textarea1" onfocus="this.value=''; "></textarea>
</textarea>
<button onclick="do_update()">Select</button>
</p>
<p>
<select id='my_select' name='my_select' onChange="do_update(this.selectedIndex);">
</select>
</p>
<script type="text/javascript" src="https://www.google.com/jsapi?autoload={'modules':[{'name':'visualization','version':'1.1','packages':['sankey']}]}"></script>
<button onclick="do_update('DEG')">DEG categories</button>
<button onclick="do_update('GENES')">GENES</button>
<div id="sankey_basic" style="width: 900px; height: 500px;"></div>
<script type="text/javascript">
        var data;
        var chart;

        function do_update2(input){
                var max_genes=10;
				___MAP___
				___MAP2___
                cur_vals=map2[input]
                var data = new google.visualization.DataTable();
                data.addColumn('string', 'From');
                data.addColumn('string', 'To');
                data.addColumn('number', 'Amount of genes');
                cur_vals = cur_vals.split(',');
                goi=[]
                for(var cur_val in cur_vals){
                         cur_val=cur_vals[cur_val];
                         goi.push(cur_val)
                }
                if(goi.length>max_genes){
                         var goiLength = goi.length;
                         var my_select = document.getElementById("my_select");
                         my_select.options.length = 0;
                         for (var i = 0; i < goiLength; i++) {
                                 if(i==0){
                                         data.addRows(map[goi[i]])
                                 }
                                 my_select.options[my_select.options.length] = new Option(goi[i], goi[i]);
                         }
                }else{
                         var goiLength = goi.length;
                         for (var i = 0; i < goiLength; i++) {
                                 data.addRows(map[goi[i]])
                         }
                }
                var options = {
                  width: 600,
                    sankey: {
                        node: {
                            interactivity: true
                        }
                    }
                };
                var chart = new google.visualization.Sankey(document.getElementById('sankey_basic'));
                chart.draw(data, options);
        }

        function do_update(input){

                /// ----------------------------------------------------
                ///
                ///        GLOBAL PARAMETER USED IN BIOSANKEY
                ///
                var max_genes=10;
                var items = [];
                var goi = [];
                var found_match=false;
                var i=0;
                var myobject = {};
				___MAP___
                var my_select = document.getElementById("my_select");
                var cur_vals=document.getElementById('textarea1').value;
                var gene_was_selected=false
                ///
                ///
                /// ----------------------------------------------------

                var data = new google.visualization.DataTable();
                data.addColumn('string', 'From');
                data.addColumn('string', 'To');
                if(input=="DEG"){
                        data.addColumn('number', 'Amount of genes');
                }else{
                        data.addColumn('number', 'Expression');
                }
                if(typeof(input)=="undefined"){
                }else{
                        cur_vals=my_select.value
                        if(input!="DEG" && input!="GENES"){
                           gene_was_selected=true
                        }
                }
                if(input=="DEG"){
                        for(var key in map){
                                opt=(key=="up")
                                if(opt==true){
                                        data.addRows(map[key])
                                }
                        }
                }else if(input=="GENES"){
                        for(var key in map){
                                opt=(key=="up")
                                if(opt==false){
                                        goi.push(key)
                                }
                        }
                        if(goi.length>max_genes){
                                var goiLength = goi.length;
                                var my_select = document.getElementById("my_select");
                                my_select.options.length = 0;
                                for (var i = 0; i < goiLength; i++) {
                                        if(i==0){
                                           data.addRows(map[goi[i]])
                                        }
                                        my_select.options[my_select.options.length] = new Option(goi[i], goi[i]);
                                }
                        }else{
                                var goiLength = goi.length;
                                for (var i = 0; i < goiLength; i++) {
                                        data.addRows(map[goi[i]])
                                }
                        }
                }
                if(typeof(input) == "undefined" || input=="undefined" || gene_was_selected==true){
                        cur_vals = cur_vals.split(',');
                        for(var cur_val in cur_vals){
                                cur_val=cur_vals[cur_val];
                                if(cur_val=="all"){
                                        for(var key in map){
                                                opt=(key=="up")
                                                if(val=="DEG"){
                                                        if(opt==true){
                                                         data.addRows(map[key])
                                                        }
                                                }else{
                                                        if(opt==false){
                                                                data.addRows(map[key])
                                                        }
                                                }
                                                found_match=true;
                                        }
                                }else{
                                         data.addRows(map[cur_val]);
                                         items.push(cur_val)
                                        found_match=true;
                                }
                        }
                }
                if(found_match==false && input!="DEG"){
                        for(var key in map){
                                for(var el in map[key]){
                                        var opt=(key=="up")
                                        if(typeof(input) == "undefined"){
                                               data.addRow(map[key][el])
                                        }else{
                                                if(key!="up"){
                                                        var n=map[key][el][0].search(input);
                                                        if(n>=0){
                                                              data.addRow(map[key][el])
                                                        }
                                                }
                                        }
                                }
                        }
                }
                if(my_select.value==""){
                        my_select.options.length = 0;
                        fLen = items.length;
                        for (var x = 0; x < fLen; x++) {
                                my_select.options[my_select.options.length] = new Option(items[x], items[x]);
                        }
                }
                var options = {
                  width: 600,
                    sankey: {
                        node: {
                            interactivity: true
                        }
                    }
                };
                var chart = new google.visualization.Sankey(document.getElementById('sankey_basic'));
                chart.draw(data, options);
                google.visualization.events.addListener(chart, 'select', function() {
                var sel = chart.getSelection();
                if (sel.length)
                 do_update2(sel[0].name);
                });
         }

         function drawChart() {
                var data = new google.visualization.DataTable();
                data.addColumn('string', 'From');
                data.addColumn('string', 'To');
                data.addColumn('number', 'Weight');
                var options = {
          width: 600,
            sankey: {
                node: {
                    interactivity: true
                }
            }
        };
        var chart = new google.visualization.Sankey(document.getElementById('sankey_basic'));
        chart.draw(data, options);
          google.visualization.events.addListener(chart, 'select', function() {
              var sel = chart.getSelection();
              if (sel.length)
                  alert('You selected node "' + sel[0].name + '"');
          });
      }
</script>
<hr>
<h2>Citation</h2>
Platzer, Polzin, Han and Nussbaumer. BioSankey: a tool to visualise and analyse microbial communities, gene expression and variants over time.
</body>
</html>


"""

vals=sys.argv[1:]
expr_f=False
deg_f=False
for vals_ in vals:
	if(vals_.find("expr=")!=-1):
		EXP_DIR=vals_.split("expr=")[1]
		expr_f=True
	elif(vals_.find("deg=")!=-1):
		DEG_DIR=vals_.split("deg=")[1]
		deg_f=True

if(expr_f==False and deg_f==False):
	print "ERROR\texpression file and deg dir file missing"
	print "USAGE: python 0_make_html.py expr=Use_case_1/extract_genes.txt deg=Use_case_1/DEG_information"
	sys.exit()
elif(expr_f==False):
	print "ERROR\texpression file missing"
        print "USAGE: python 0_make_html.py expr=Use_case_1/extract_genes.txt deg=Use_case_1/DEG_information"
	sys.exit()
elif(deg_f==False):
	print "ERROR\tdeg dir missing"
        print "USAGE: python 0_make_html.py expr=Use_case_1/extract_genes.txt deg=Use_case_1/DEG_information"
	sys.exit()

map=extract_gene_expression.run(EXP_DIR)
map2,map3=extract_DEG_information.run(DEG_DIR,EXP_DIR)

a=a.replace("___MAP___","var map={"+map+"'up':["+map2+"]"+"}")
a=a.replace("___MAP2___",map3)
print(a)

