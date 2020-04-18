<!-- On MP set up, I use apache2 to run the server and php7 as well as phpmyadmin to mange the Mysql DB
    Put this file in your /var/www/html/ directory on your MP
 -->
 <html>
    <body>
    <form action = "index.php" method = "post">
        <input type = "text" name="user" />
        <input type="password" name="password"/>
        <input type="submit" value="Log In" />
    </form>
    </body>
 </html>