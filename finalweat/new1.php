<html>
<form  method="post">
  <input type="submit" value="month" name="submit">
 <?php
  if( isset($_POST["submit"]))
  {
	  echo shell_exec("python C:\\xampp\\htdocs\\elate\\finalweat\\Mainbar.py"); 
	  
  echo "<img src=\"abc.png\" alt=\"Image\" class=\"img-responsive\">";
  } 
  
 ?>
 </form>
 </html>