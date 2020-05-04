<?php
    if(isset($_POST['submit'])){
        $connect = mysqli_connect("35.189.9.144","root","iotassignment2","CarShare");
        $result = mysqli_query($connect, "SELECT * FROM Users WHERE username = '".$_POST["username"]."' and password = '".$_POST["password"]."'");
        $count = mysqli_num_rows($result);
        if ($count != 0) {
            header('Location:https://youtube.com');
            $_SESSION['username'] = $_POST['username'];
            exit;
        }
    }
?>