<?php
    session_start();
?>
<!-- On MP set up, I use apache2 to run the server and php7 as well as phpmyadmin to mange the Mysql DB
    Put this file in your /var/www/html/ directory on your MP
 -->
 <html>
    <body>
    <form action = "redirect_to_menu.php" method = "post">
        Username: <input type = "text" name="username" /><br>
        Password: <input type="password" name="password"/><br>
        <input type="submit" name = "submit" value="Log In" />
    </form>
    </body>
 </html>