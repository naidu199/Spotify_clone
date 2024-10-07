<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<body>
	<?php
	$_SESSION['name']='naidu';
	$_SESSION['password']='123455';
	?>
</body>
</html>
<!-- <?php
// session_start();
?> -->
<!DOCTYPE html>
<html>
<body>
<?php
// Echo session variables that were set on previous page
echo "Company name is " . $_SESSION["name"] . ".<br>";
echo "Company ID is " . $_SESSION["password"] . ".";
?>
</body> </html>
?>
