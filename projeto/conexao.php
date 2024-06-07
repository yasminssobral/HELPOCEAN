<?php
$host = "localhost";
$user = "root";
$pass = "";
$banco = "HELPOCEAN";

$conexao = new mysqli($host, $user, $pass, $banco);

if ($conexao->connect_error) {
    die("Erro de conexão: " . $conexao->connect_error);
}
?>