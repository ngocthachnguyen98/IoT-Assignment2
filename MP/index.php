<!-- On MP set up, I use apache2 to run the server and php7 as well as phpmyadmin to mange the Mysql DB
    Put this file in your /var/www/html/ directory on your MP
 -->
 <html>
    <body>
    <form action = "index.php" method = "post">
        Username: <input type = "text" name="username" /><br>
        Password: <input type="password" name="password"/><br>
        <input type="submit" name = "submit" value="Log In" />
        <?php
            $message="";
            if(isset($_POST['submit'])){
                $connect = mysqli_connect("35.189.9.144","root","iotassignment2","CarShare");
                $result = mysqli_query($connect, "SELECT * FROM Users WHERE username = '".$_POST["username"]."' and password = '".$_POST["password"]."'");
                $count = mysqli_num_rows($result);
                if ($count == 0){
                    $message = "Invalid Login Detail !";
                }
                else {
                    $message = "Logged in successfully !";
                }
            }
            if ($message!= ""){
                echo $message;
            }
        ?>
    </form>
    </body>
 </html>