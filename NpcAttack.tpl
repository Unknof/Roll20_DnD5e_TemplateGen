<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Roll20 Npc Attack</title>
</head>
<h3>Welcome to the npc attack macro creator</h3>
<p>Please enter npc stats.</p>
<form action="/create" method = "get">
    <label for="mname">Monster name:</label>
    <input type="text" id="mname" name="mname"><br><br>
    <label for="descr">Attack description:</label>
    <input type="text" id="descr" name="descr"><br><br>
    <label for="attm">Attackroll modifier:</label>
    <input type="number" id="attm" name="attm"><br><br>
    <label for="critc">Crit at (default is 20):</label>
    <input type="number" id="critc" name="critc"><br><br>
    <label for="dmgr">Damageroll:</label>
    <input type="text" id="dmgr" name="dmgr"><br><br>
    <label for="dmgt">Damage type:</label>
    <input type="text" id="dmgt" name="dmgt"><br><br>
  <input type="submit" value="Submit">
</form>
<body>

</body>
</html>