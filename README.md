# README

## Título do Projeto: Sistema de Interação com Usuário

Este projeto é um sistema interativo baseado em Python que lida com a dinâmica do site da formula-e que meu grupo criou para Challenge, tendo navegação por diferentes seções e interações com o usuário. O projeto utiliza expressões regulares para validação de email e fornece várias utilidades para validação de entrada do usuário e navegação.

### Pré-requisitos

- Python 3.11.9
- Compreensão básica de programação em Python

### Estrutura do Projeto

As principais funcionalidades fornecidas por este projeto são:

1. **Validação de Email**
2. **Validação de Número**
3. **Autenticação de Usuário**
4. **Navegação de Menu**
5. **Seções Interativas**

### Visão Geral do Código

#### Importar Bibliotecas Necessárias

```python
import re
```

#### Expressão Regular para Validação de Email

Um padrão de expressão regular é definido para validar endereços de email.

```python
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
```

#### Funções

1. **Verificação de Email**

    Esta função solicita ao usuário que insira um email e o valida em relação ao padrão da expressão regular.

    ```python
    def verifica_email(msg):
        email = input(msg)
        while not re.fullmatch(regex, email):
            email = input("Email Inválido! Coloque seu email novamente: ")
        return email
    ```

2. **Verificação de Número**

    Esta função assegura que a entrada seja um valor numérico.

    ```python
    def verifica_numero(msg):
        num = input(msg)
        if not num.isnumeric():
            print("Deve ser um número!")
            num = verifica_numero(msg)
        return int(num)
    ```

3. **Pesquisa de Elemento na Lista**

    Esta função verifica se um elemento está em uma lista.

    ```python
    def meu_in(lista, buscar):
        for elem in lista:
            if elem == buscar:
                return True
        return False
    ```

4. **Pesquisa do Índice de Elemento na Lista**

    Esta função encontra o índice de um elemento em uma lista.

    ```python
    def meu_index(lista, buscar):
        for i in range(len(lista)):
            if lista[i] == buscar:
                return i
        return False
    ```

5. **Forçar Opção de Usuário**

    Esta função assegura que o usuário selecione uma opção de uma lista predefinida.

    ```python
    def forca_opcao(msg, lista_opcoes):
        msg_erro = ' '.join(lista_opcoes)
        msg_erro = f"Somente essas opções:\n{msg_erro}"
        opcao = input(msg)
        while não meu_in(lista_opcoes, opcao):
            print(msg_erro)
            opcao = input(msg)
        return opcao
    ```

6. **Verificação de Comprimento de Senha**

    Esta função assegura que a senha tenha um comprimento mínimo.

    ```python
    def senha_len(msg):
        senha = input(msg)
        while len(senha) < 5:
            print("A senha deve ter 5 ou mais caracteres")
            senha = input("Digite sua senha: ")
        return senha
    ```

#### Script Principal

1. **Imprimir Arte de Boas-Vindas**

    Exibe uma mensagem de boas-vindas em ASCII art.

    ```python
    print("ASCII art here")
    ```

2. **Cadastro de Usuário**

    Solicita ao usuário detalhes de cadastro.

    ```python
    sim_nao = ['s', 'n']
    moedas = 0
    print("Faça seu cadastro!")
    email = verifica_email("Diga seu email: ")
    nome = input("Diga seu nome: ")
    senha = senha_len("Digite sua senha: ")
    print("Você foi cadastrado")
    ```

3. **Login de Usuário**

    Lida com o login do usuário com um máximo de 3 tentativas antes de oferecer a opção de resetar a senha.

    ```python
    i = 0
    while True:
        print('Login')
        nome_login = input("Diga seu nome: ")
        senha_login = input("Digite sua senha: ")
        if nome_login == nome ou senha_login == senha:
            break
        while nome_login != nome ou senha_login != senha:
            if i < 3:
                print("User ou senha incorretos")
                nome_login = input("Diga seu nome novamente: ")
                senha_login = input("Digite sua senha novamente: ")
                i += 1
            else:
                resetar = forca_opcao('Deseja resetar sua senha?', sim_nao)
                if resetar == 's':
                    print('O reset de sua senha foi enviado por email!')
                    print("Email")
                    senha = senha_len("Qual sua nova senha?")
                    break
    ```

4. **Navegação de Menu**

    Fornece um menu para navegar por diferentes seções do aplicativo.

    ```python
    telas = ['H', 'A', 'B', 'C', 'M', 'E']
    escolha = forca_opcao("Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
    ```

5. **Manipuladores de Seção**

    Cada seção do menu tem um manipulador dedicado para interações com o usuário.

    ```python
    while escolha != 'E':
        while escolha == 'H':
            # Código da seção Home
            escolha = forca_opcao("Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
        while escolha == 'A':
            # Código da seção AroundCity
            escolha = forca_opcao("Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
        while escolha == 'B':
            # Código da seção Bicicletas
            escolha = forca_opcao("Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
        while escolha == 'C':
            # Código da seção Community
            escolha = forca_opcao("Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
        while escolha == 'M':
            # Código da seção Moedas
            escolha = forca_opcao("Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
    ```

### Como Executar

1. Certifique-se de ter o Python instalado no seu sistema.
2. Copie o código para um arquivo Python (por exemplo, `sistema_interacao_usuario.py`).
3. Abra um terminal ou prompt de comando e navegue até o diretório que contém o arquivo.
4. Execute o script usando o comando:

    ```sh
    python sistema_interacao_usuario.py
    ```

### Funcionalidades

- **Validação de Email e Número**: Garante que as entradas do usuário sejam válidas.
- **Autenticação de Usuário**: Lida com o cadastro e login do usuário, com funcionalidade de redefinição de senha.
- **Navegação de Menu**: Fornece um menu interativo para navegar por diferentes seções.
- **Seções Interativas**: Inclui seções para home, eventos na cidade, aluguel de bicicletas, chat comunitário e um sistema de moedas.
