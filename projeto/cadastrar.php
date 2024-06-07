<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastre-se</title>
    <link rel="icon" type="image/png" href="logo.png">
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }

        .container {
            background-color: #fff;
            max-width: 600px; 
            margin: 0 auto;
            padding: 40px; 
            border-radius: 15px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
            
        }

        .logo {
            width: 150px; 
            height: auto;
            display: block;
            margin: 0 auto 20px; 
            max-width: 100%; 
 
        }

        input[type="text"],
        input[type="password"],
        input[type="email"],
        input[type="tel"] {
            font-size: 20px;
            border: 1px solid #ccc;
            border-radius: 8px; 
            padding: 15px; 
            margin-bottom: 24px;
            width: 100%;
            box-sizing: border-box;
        }

        input[type="radio"] {
            margin-right: 10px;
            font-size: 18px;
        }

        input[type="submit"] {
            font-size: 24px; 
            color: white;
            background-color: #0077a0;
            border: none;
            border-radius: 8px;
            padding: 15px 30px; 
            margin-top: 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #005580;
        }

        a {
            font-size: 20px; 
            color: #0077a0;
            text-decoration: none;
            display: block;
            margin-top: 20px; 
        }

       
        footer {
            background-color: #0077a0;
            color: white;
            padding: 15px; 
            width: 100%;
            position: fixed;
            bottom: 0;
        }

       
        fieldset {
            margin-bottom: 20px;
        }

       
        p {
            font-size: 20px; 
            margin-bottom: 10px; 
        }
    </style>

    <script>
        function formatarTelefone() {
            var telefoneInput = document.getElementById('telefone');
            var numeroTelefone = telefoneInput.value.replace(/\D/g, ''); 

            if (numeroTelefone.length >= 2) {
                telefoneInput.value = '(' + numeroTelefone.substring(0, 2);

                if (numeroTelefone.length > 2) {
                    telefoneInput.value += ') ' + numeroTelefone.substring(2, 7);

                    if (numeroTelefone.length > 7) {
                        telefoneInput.value += '-' + numeroTelefone.substring(7);
                    }
                }
            }
        }
    </script>
</head>
<body>
    <div class="container">
        <img class="logo" src="./imagens/logogs.png" alt="logo">
        <h2>Cadastro</h2>
        <form method="post" action="./cadastro-login/cadastro.php" onsubmit="mostrarCampoTexto()">
            <input type="text" name="nome" placeholder="Nome" required/><br>
            <input type="email" name="email" placeholder="Email" required/><br>
            <input type="password" name="senha" placeholder="Senha" required/><br>
            <input type="tel" name="telefone" id="telefone" placeholder="Telefone" pattern="\(\d{2}\)\s\d{4,5}-\d{4}" title="Digite um número de telefone válido" oninput="formatarTelefone()" required/><br>

            <input type="submit" value="Cadastrar" /><br>
        </form>

        <a href="index.php">Voltar à página inicial</a>
    </div>
</body>
</html>