<html>
<title> Scentopedia </title>
<body>
<h1> Welcome to the World of Plants!! </h1>
<hr>

<!-- <form action="/playerSubmit.php">
  Player First Name:<br>
  <input type="text" name="firstname" ><br>
  Player Last Name:<br>
  <input type="text" name="lastname" ><br>
  Player Hand:<br>
  <input type="text" name="hand" ><br>
  Player Height:<br>
  <input type="text" name="height" ><br>

  <input type="submit" value="Submit">
</form> -->

<form action="/plants.php" method="get">
  <button type="submit">Explore All Plants</button><br>
</form>

<form action="/tournaments.php" method="get">
  <button type="submit">Explore All Tournaments</button><br>
</form>

<form action = "/individual_tournament.php" method="post" name="tournament">
  Tournament Name:<br>
  <input type="select" name="tourney_name" id="temp_id" value=""><br>
  <button type="submit" >Submit</button><br>
</form>



</body>
</html>
