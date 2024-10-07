<?php
setcookie('name','naidu',time()+30*24*60*60);
?>
<!DOCTYPE html>
<html lang="en">

<body>
<?php
if(isset($_COOKIE["name"])){
	echo "Hi "  .$_COOKIE["name"];
}else{
echo "Welcome Guest User";
}
?>
</body>
</html>
