
//var bars_in_chart = 10;

$(document).ready(function(){

  $(".chart_and_buttons").hide(); // hide buttons initially

  // load the visualization API and the core chart package.
  google.charts.load('current', {'packages':['corechart']});
  
  // set a callback to run when the Google Visualization API is loaded.
  google.charts.setOnLoadCallback(function(){
  drawChart(all_lines,0);
  $(".chart_and_buttons").fadeIn(1000);
  });

  // create and populate a data table,
  // instantiate the chart, pass in the data and
  // draw it:
  function drawChart(all_lines_arr, start_at_index) {

  start_at_index_int = parseInt(start_at_index);
  var brands_to_be_shown_number = all_lines_arr.length
  var last_possible_index_int = brands_to_be_shown_number - 1;

  // if start index is out of bound, don't draw new chart
  if ((start_at_index_int > last_possible_index_int) || 
      (start_at_index_int <0)) {
      return;
  }

  // create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Brand');
  data.addColumn('number', 'Items');

  // showing part of the data
  var slice_at = start_at_index_int + bars_in_chart;
  data.addRows(all_lines.slice(start_at_index_int, slice_at));

  // set chart options
  var options = {'title': 'Chart of Top Brands: Items per Brand in Descending Order', 
                 'width':700,
                 'height':350,
                 'chartArea': {'width': '60%', 'height': '70%'},
                 'legend': {'position': 'bottom'}
                };

  // instantiate and draw chart, passing in some options.
  var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
  chart.draw(data, options);

  // update next/prev buttons
  $("#prev-btn").attr("start", start_at_index - bars_in_chart);
  $("#nxt-btn").attr("start", start_at_index + bars_in_chart);
              
  }

  $("#prev-btn").click(function(){
  drawChart(all_lines, parseInt($(this).attr("start")));
  });  

  $("#nxt-btn").click(function(){
  drawChart(all_lines, parseInt($(this).attr("start")));
  });  

});
