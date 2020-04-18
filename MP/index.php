<!-- On MP set up, I use apache2 to run the server and php7 as well as phpmyadmin to mange the Mysql DB
    Put this file in your /var/www/html/ directory on your MP
 -->
 <?php
    $message="";
    if(isset($_POST['submit'])){
        $connect = mysqli_connect("localhost","root","pynative@#29","carshare");
        $result = mysqli_query($connect, "SELECT * FROM Users WHERE username = '".$_POST["username"]."' and password = '".$_POST["password"]."'");
        $count = mysqli_num_rows($result);
        if ($count == 0){
            $message = "Invalid Login Detail !";
        }
        else {
            $message = "Logged in successfully !";
        }
    }
 ?>
 <html>
    <body>
    <form action = "index.php" method = "post">
        Username: <input type = "text" name="username" /><br>
        Password: <input type="password" name="password"/><br>
        <input type="submit" value="Log In" />
        <?php
            if ($message!= ""){
                echo $message;
            }
        ?>
    </form>
    </body>
 </html>