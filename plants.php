<html>
<title> Scentopedia </title>
<head>
  <style>
  h1, a.header {
    padding-left: 1%;
  }
  p {
    padding-top: 1%;
    padding-left: 1%;
    padding-bottom: 1%;
  }
  div {
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 10px;
    margin-left: 10px;
  }
  tfoot input {
    width: 100%;
    padding: 3px;
    box-sizing: border-box;
  }
  </style>
</head>

<body>
<h1> Plants </h1>
<hr>
<a class="header" href="http://localhost:3333/index.php">Home</a>


<br><br>
<p><strong>Click the headers to sort the table. <br> Search entire table using the search bar above the table. Search individual columns with regex queries using the search bar below each header.</strong></p>

<?php
require 'vendor/autoload.php'; // include Composer's autoloader

// Connect to MongoDB client
$conn = new MongoDB\Client('mongodb://localhost');

// Connect to plants database
$db = $conn->plants;

// $collection = plants;

// If url specifies a certain player, filter for that player
// Else, use entire collection
/*
if (isset($_GET['plants'])) {
  $p_name = $_GET['pants'];
  $cursor = $collection->find(array('player_name' => $p_name));
} else {
  $cursor = $collection->find();
};

    


$cursor = $collection->find();
*/
$tuple_count = 0;

$collection = $db->plants;
$cursor = $collection->find();
?>

<div>
<table id="plants" border="1" class="display">
  <thead>
    <tr style="text-align: right;">
      <th>Name</th>
      <th>Scientific Name</th>
    </tr>
  </thead>

<tbody>

<?php
foreach ($cursor as $row) {
  $tuple_count++;
  echo "<p> This is name of the plant $row[Name]" ;
  echo "<tr>";
  echo "<td>".$row['Name']."</td>";
  echo "<td>".$row['Scientific Name']."</td>";
  
  echo "</tr>";
}
?>

</tbody>
<tfoot>
  <tr>
      <th>Name</th>
      <th>Scientific Name</th>
  </tr>
</tfoot>
</table>
</div>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<link rel="stylesheet"
href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css"></style>

<script type="text/javascript"
src="http://cdn.datatables.net/1.10.2/js/jquery.dataTables.min.js"></script>

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>

<script>
$(document).ready(function() {
  // Setup - add a text input to each footer cell
  $('#plants tfoot th').each( function () {
    var title = $(this).text();
    $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
  } );

  // DataTable
  var table = $('#plants').DataTable();

    // Apply the search
    table.columns().eq(0).each(function (colIdx) {
      $('input', table.column(colIdx).footer()).on('keyup change', function () {
        table.column (colIdx)
          .search (this.value.replace('/;/g', '&quot;|&quot;'), true, false)
          .draw ();
      } );
    } );

  // Position column search below column names
  $('#plants tfoot th').appendTo('#plants thead');
} );
</script>

</body>
</html>
