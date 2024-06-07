<?php
// Inclui o arquivo de conexão com o banco de dados
require_once('conexao.php');

// Verifica se o formulário foi submetido
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Verifica se todos os campos foram preenchidos
    if (!empty($_POST['nome']) && !empty($_POST['email']) && !empty($_POST['senha']) && !empty($_POST['telefone'])) {
        // Prepara os dados do formulário para inserção no banco de dados
        $nome = $conexao->real_escape_string($_POST['nome']);
        $email = $conexao->real_escape_string($_POST['email']);
        $senha = $conexao->real_escape_string($_POST['senha']);
        $telefone = $conexao->real_escape_string($_POST['telefone']);

        // Insere os dados no banco de dados
        $sql = "INSERT INTO Cadastro (nome, email, senha, telefone) VALUES ('$nome', '$email', '$senha', '$telefone')";
        if ($conexao->query($sql) === TRUE) {
            // Redireciona o usuário para a página de login
            header('Location: login.php');
            exit(); // Termina o script após o redirecionamento
        } else {
            echo "Erro ao cadastrar: " . $conexao->error;
        }
    } else {
        echo "Por favor, preencha todos os campos.";
    }
}
?>