import re

# regex para email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


# função para verificar o email de acordo com o regex
def verifica_email(msg):
    email = input(msg)
    while not re.fullmatch(regex, email):
        email = input("Email Inválido! Coloque seu email novamente: ")
    return email


# verifica se o input é um número
def verifica_numero(msg):
    num = input(msg)
    if not num.isnumeric():
        print("Deve ser um numero!")
        num = verifica_numero(msg)
    return int(num)


# recebe a lista e busca o elemento digitado
def meu_in(lista, buscar):
    for elem in lista:
        if elem == buscar:
            return True
    return False


# procura index do elemento
def meu_index(lista, buscar):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return i
    return False


# força a opção do usuário
def forca_opcao(msg, lista_opcoes):
    msg_erro = ' '.join(lista_opcoes)
    msg_erro = f"Somente essas opcoes:\n{msg_erro}"
    opcao = input(msg)
    while not meu_in(lista_opcoes, opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao


def senha_len(msg):
    senha = input(msg)
    while len(senha) < 5:
        print("A senha deve ter 5 ou mais caractéres")
        senha = input("Digite sua senha: ")
    return senha


print(""
      "|------------------------------------------------------------------------------------------------------------------------------------------------------|\n"
      "|                                                                                                                                                      |\n"
      "|                                                                                                                                        .-+*####=.    |\n"
      "|                                                                                                                                 ..+%@%%@@@@@@@@@+    |\n"
      "|                                                                                                                             .=#%%%%@@@%*=:.#@@@%.    |\n"
      "|                                                                                                                         ..*%%%%%@%%=     .%@@@%:     |\n"
      "|                                                                                                                       .*%%%%%%%+.       *@@@@%.      |\n"
      "|                ...-+%%%%%%%%%%%*           .....       .:-      ..*%%.            -%=    ...        .=%%%          .:%%%%%%%-        .*%%@@%+        |\n"
      "|            .+%%%%%%%%%#*+=-::..      .:*%%%%%%%%%:   .*%%%    .*%%%%%.  .-=      =%#    +%%:      -%%%%%*         :%%%%%%+.        .*@@%%@*.         |\n"
      "|           -%%%%%%.           .+-.  .%%%%%#:   *%%%  -%%%%=   %%%%%%%   =%%#     +%%.  .%%#.    .*%%%%%%*        .%%%%%%=         -%%%@@%+            |\n"
      "|             =%%#.       :*%%%%%%%. --*%%.   :#%%*  #%%*%# .*%%*-%%%.  *%%%:    *%%.  =%%+.   .*%%%:-%%#        :%%%%%*.     .:+%%@%%%#:              |\n"
      "|            -%%%-*%%%# .%%%%:..%%%:  +%%.  *%%%#. .%%%.%%=-%%%.:%%%. .%%%%:   .%%%. .#%%=.   *%%%.. %%%.       .%%%%%=. #%%%%%%%%%%*..                |\n"
      "|           -%%%%%%*=:.*%%%:   :%%%. +%%=*%%%#-   .%%#.=%%*%%+..%%%. .#%%%:   :%%#. :%%%-   -%%%:   *%%-        *%%%%#.  =*###*+-.                     |\n"
      "|          -%%%:.     *%%#.   .%%%: =%%%%%#..    .%%*. #%%%%.  #%%:  +%%%:   =%%*. -%%%=   #%%: -%#.%%#.        %%%%%=                      +%*        |\n"
      "|         .%%%.      :%%%.   -%%%: :%%**%%%%-.   -%*  .%%%*   *%%=  :%%%=  .#%%-  -%%%+    .     =%%%%-         %%%%%%.                  -%%@#.        |\n"
      "|         #%%.       +%%.  -%%%%.  %%*. .:%%%%#: ..   :%%=    %%*   =%%%. +%%#.  :%%%* .:+#%%%#. .%%%%.         #%%%%%%.             .*%%@@%:          |\n"
      "|        +%%.        :%%%%%%%#:   :%%.      :*%%%#-.         *%%:   =%%%#%%#:    #%%%%%%%%#*=-.  .%%%+          :%%%%%%%%=:....:-+%%%@%%%%:            |\n"
      "|        #%:          ..-=-..      :.          ..--.         *%=    .=%%%-.      .#%%#-.          =%%:           :%%%%%%%%%%%%%%%%%%%%%+.              |\n"
      "|                                                             .                                                    =%%%%%%%%%%%%%%%#=.                 |\n"
      "|                                                                                                                    .-*%%%%%%#=:.                     |\n"
      "|                                                                                                                                                      |\n"
      "|------------------------------------------------------------------------------------------------------------------------------------------------------|\n")

sim_nao = ['s', 'n']
moedas = 1500
# Cadastro
print("Faça seu cadastro!")
email = verifica_email("Diga seu email: ")
endereco = input("Digite seu endereço: ")
nome = input("Diga seu nome: ")
senha = senha_len("Digite sua senha: ")

# caso a senha tiver menos de 5 caractéres, entra en um loop

print("Você foi cadastrado")
i = 0
while True:
    print('Login')
    nome_login = input("Diga seu nome: ")
    senha_login = input("Digite sua senha: ")
    if nome_login == nome or senha_login == senha:
        break
    while nome_login != nome or senha_login != senha:
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

# Tipos de telas no código
telas = ['H', 'A', 'B', 'C', 'M', 'E']
escolha = forca_opcao("Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ",
                      telas)
print('\n')
while escolha != 'E':
    while escolha == 'H':
        print(
            "                                                                    Home                                                                               \n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print(
            "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵\n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print(
            "                                                                                                                                                       ")
        print(
            f"Bem vindo(a) {nome}! A Fórmula E é mais do que apenas uma série de corridas - é uma batalha pelo futuro. Nossos carros radicais - todos movidos a \n"
            "eletricidade - pavimentam o caminho para os carros de rua do amanhã, com a série atuando como uma plataforma competitiva para testar e desenvolver o \n"
            "que há de mais moderno em tecnologia elétrica.")
        print('\n')

        escolha = forca_opcao(
            "Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
        print('\n')
    while escolha == 'A':
        print(
            "                                                                 AroundCity                                                                            ")
        print(
            "                                                             LET'S GET TOGETHER                                                                        \n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print(
            "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵\n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")

        print(
            "AroundcCity é uma campanha feita pela formula-e onde foca em patrocinio ou investimento em tudo que está relacionado a sustentabilidade em torno da\n"
            " cidade de São Paulo, ou outras cidades, como Parques e empresas que tem envolvimento grande com sustentabilidade(FIAP, etc)!\n")

        print(
            "                                                             Confira os eventos                                                                        \n")
        eventos = ['Corrida', 'Piquenique', 'Palestra', 'N']
        # Força a opção do usuário de acordo com a lista eventos
        escolha_evento = forca_opcao(
            "                          Corrida de Rua                            Piquenique                      Palestra sobre sustentabilidade                    \n"
            "                          12/08/24 - 4PM                          06/10/24 - 4PM                            10/12/24 - 4PM                             \n"
            "                      Local: Parque Iburapuera                Local: Parque Iburapuera                        Local: FIAP                              \n"
            "                    Venha com sua melhor roupa e             Conheça novas pessoas e se              Expanda seu networking e conheça                  \n"
            "                           corra com nós                    delicie com nosso piquinique!               mais sobre sustentabilidade                    \n"
            "                          Digite Corrida                        Digite Piquenique                            Digite Palestra                           \n"
            "                         para se inscrever                      para se inscrever                           para se inscrever                          \n"
            "                                                                                                                                                       \n"
            "                                              Caso não queira participar de nenhuma dos eventos digite N                                               \n",
            eventos)

        if escolha_evento == 'Corrida' or escolha_evento == 'Piquenique' or escolha_evento == 'Palestra':
            print(
                f"Você acaba de se inscrever na {escolha_evento}! Enviaremos mais informações sobre pelo email {email}")
        else:
            print("Esperamos você na próxima, novos eventos virão em breve!")

        escolha = forca_opcao(
            "Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
        print('\n')
    while escolha == 'B':
        print(
            "                                                                 Bicicletas                                                                            \n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print(
            "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵\n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")

        print(
            "                                                                 Bicicletas                                                                            \n")
        print(
            "                                                        😎 Navegue na eletricidade 😎                                                                  \n")

        # Força a opção do usuário de acordo com a lista sim_nao
        ver_bicicletas = forca_opcao("Deseja ver as bicicletas que oferecemos? (s/n)", sim_nao)

        # Setando o valores, descrição e nomes das bicicletas
        bicicletas = ['Bike Ultra Max', 'Bike Max', 'Bike-e', 'N']
        valores = [40, 20, 10]
        descricao = ['é uma ótima escolha para passear com amigos de uma maneira super confortável, tendo'
                     ' 4 assentos para se juntarem e pedalarem juntos', 'é uma ótima escolha para passear com'
                                                                        ' um amigo para viver uma aventura inesquecível, tendo 2 assentos para se juntarem'
                                                                        ' e pedalarem juntos',
                     'é uma escolha muito interessante para se aventurar pela cidade'
                     'e descobrir novos lugares pela cidade, a bike contem apenas um assento']
        while ver_bicicletas == 's':
            print(f'Temos essas opções: \n'
                  f'1 - {bicicletas[0]} - Premium\n'
                  f'2 - {bicicletas[1]} - Mediana\n'
                  f'3 - {bicicletas[2]} - Comum\n')
            bicicleta_escolhida = forca_opcao("Qual bicicleta você gostaria de conhecer mais sobre? Digite seus "
                                              "respectivos nomes ou N para encerrar: ", bicicletas)

            if bicicleta_escolhida == 'N':
                break
            # pega o index da bicicleta escolhida de acordo com as bicicletas
            index_bike = meu_index(bicicletas, bicicleta_escolhida)

            print(
                f"A bicicleta {bicicletas[index_bike]} {descricao[index_bike]}! Tudo isso sai por apenas {valores[index_bike]} por hora")

        escolha_progresso = forca_opcao("Deseja ver seu progresso atual? (s/n)", sim_nao)
        kilometros_rodados = 3

        moedas_bike = kilometros_rodados * 5
        moedas += moedas_bike
        # Mostra progresso do usuário de acordo com os kilometros rodados na bicicleta
        if escolha_progresso == 's':
            print(f'Atualmemte você tem {kilometros_rodados}Km rodados e {moedas} moedas')
        escolha = forca_opcao(
            "Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
        print('\n')
    while escolha == 'C':
        print(
            "                                                                  Community                                                                            \n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print(
            "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵\n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        tipos_chat = ['Chat 1', 'Chat 2', 'Chat 3', 'Chat 4', 'N']
        # Setando conversas
        conversa = [
            'Rodrigo: Opa, aea mn!\nRodrigo: Você viu aquele novo anúncio da mahindra??\nPatrick: Eu vi! Tá mtt da hora',
            'Amanda: Bom dia!!!!! Hoje vai ter o evento piquenique! Estou muito ansiosa pra ir!!!!!\n'
            'Roberto: Eu também! Estou levand minha torta preferida de maça!\n'
            'Pedro: Uhuu!!\n',
            'Alexia: Vocês viram a última corrida??\n'
            'Alexia: Foi insana\n',
            'Rob: Aquele jogo de basquete foi muito legal ontem\n'
            'Amanda: Eu não vi! :/\n'
            'Amanda: Em que canal que passou',
            'Conversa inexistente']
        print(
            "                                                             Chat das Equipes                                                                        \n")
        escolha_chat = forca_opcao("Aqui temos 4 tipos de chats!\n"
                                   "O 1º para pessoas interessadas nos eventos da Mahindra em geral - Digite Chat 1\n"
                                   "O 2º para pessoas interessadas na formula-e - Digite Chat 2\n"
                                   "O 3º para pessoas interessadas na última corrida - Digite Chat 3\n"
                                   "O 4º para pessoas interessadas sobre outros assuntos - Digite Chat 4\n"
                                   "Não quero conversar - Digite N\n", tipos_chat)

        while escolha_chat == 'Chat 1' or escolha_chat == 'Chat 2' or escolha_chat == 'Chat 3' or escolha_chat == 'Chat 4':
            chat_index = meu_index(tipos_chat, escolha_chat)
            print(f"{conversa[chat_index]}\n")
            escolha_chat = forca_opcao("Deseja mudar de Chat??!\n"
                                       "O 1º para pessoas interessadas nos eventos da Mahindra em geral - Digite Chat 1\n"
                                       "O 2º para pessoas interessadas na formula-e - Digite Chat 2\n"
                                       "O 3º para pessoas interessadas na última corrida - Digite Chat 3\n"
                                       "O 4º para pessoas interessadas sobre outros assuntos - Digite Chat 4\n"
                                       "Não quero conversar - Digite N\n", tipos_chat)
            moedas += 3
            print(f"Você ganhou mais 3 moedas por conversar, agora você tem {moedas}")
        print(
            "                                                                 QUIZES                                                                            \n")

        escolha_quizes = forca_opcao("Você deseja fazer os quizes? (s/n)", sim_nao)
        alternativas = ['A', 'B', 'C', 'D']
        quiz = ['1', '2']
        pontuacao = 0
        if escolha_quizes == 's':
            tipo_quiz = forca_opcao("Temos dois tipos de quiz:\n "
                                    "Digite 1 - VOCÊ CONHECE MESMO A FORMULA-E?\n"
                                    "Digite 2 - VOCÊ CONHECE OS CORREDORES?(Em breve)\n", quiz)
            if tipo_quiz == '1':
                print("VOCÊ CONHECE MESMO A FORMULA-E?")
                um_formula = forca_opcao(
                    "Qual é a principal característica que diferencia a Fórmula E das outras categorias de automobilismo?\n"
                    "A) Corridas Noturnas\n"
                    "B) Carros elétricos\n"
                    "C) Corridas em circuitos ovais\n"
                    "D) Uso de pneus slick\n", alternativas)
                if um_formula == "B":
                    pontuacao += 1
                dois_formula = forca_opcao(
                    "Em que ano a Fórmula E realizou sua primeira temporada?\n"
                    "A) 2012\n"
                    "B) 2014\n"
                    "C) 2016\n"
                    "D) 2018\n", alternativas)
                if dois_formula == "B":
                    pontuacao += 1
                tres_formula = forca_opcao(
                    "Qual cidade sediou a primeira corrida da história da Fórmula E?\n"
                    "A) Paris\n"
                    "B) Nova York\n"
                    "C) Pequim\n"
                    "D) Roma\n", alternativas)
                if tres_formula == "C":
                    pontuacao += 1
                quartro_formula = forca_opcao(
                    "Qual é o nome do atual presidente da Fórmula E?\n"
                    "A) Alejandro Agag\n"
                    "B) Jean Todt\n"
                    "C) Alberto Longo\n"
                    "D) Michael Andretti\n", alternativas)
                if quartro_formula == "A":
                    pontuacao += 1
                quinto_formula = forca_opcao(
                    "Qual equipe venceu o Campeonato de Construtores na temporada 2022-2023 da Fórmula E?\n"
                    "A) Mercedes-EQ Formula E Team\n"
                    "B) DS Techeetah\n"
                    "C) Jaguar TCS Racing\n"
                    "D) Porsche Formula E Team\n", alternativas)
                if quinto_formula == "A":
                    pontuacao += 1

                moedas_ganhas = pontuacao * 7
                moedas += moedas_ganhas
                print(f"Você acertou {pontuacao}/5 e ganhou {moedas_ganhas} moedas, ou seja, você tem {moedas} moedas")
            if tipo_quiz == '2':
                print("Em breve traremos novos quizes e curiosidades!")

        escolha = forca_opcao(
            "Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
        print('\n')
    while escolha == 'M':
        print(
            "                                                                   Moedas                                                                             \n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print(
            "🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print(
            '                                                                                                                                                     \n'
            '           .:-=++++++=:.                         .:-=++++++=:.                        .:-=++++++=:.                        .:-=++++++=:.             \n'
            '        .-::::=+********+-                    .-::::=+********+-                   .-::::=+********+-                   .-::::=+********+-           \n'
            '      .:-:.:-+*************=.               .:-:.:-+*************=.              .:-:.:-+*************=.              .:-:.:-+*************=.        \n'
            '     .--::-++****+++++++++***-             .--::-++****+++++++++***-            .--::-++****+++++++++***-            .--::-++****+++++++++***-       \n'
            '    :-====+++******++*+----++*=.          :-====+++******++*+----++*=.         :-====+++******++*+----++*=.         :-====+++******++*+----++*=.     \n'
            '   .-=--=+=+***:..::---=+----+*+.        .-=--=+=+***:..::---=+----+*+.       .-=--=+=+***:..::---=+----+*+.       .-=--=+=+***:..::---=+----+*+.    \n'
            '   :-=--=--+*+.     .::::==---+++.       :-=--=--+*+.     .::::==---+++.      :-=--=--+*+.     .::::==---+++.      :-=--=--+*+.     .::::==---+++.   \n'
            '  ::-----:+*+-        .:-:-+---+++.     ::-----:+*+-        .:-:-+---+++.    ::-----:+*+-        .:-:-+---+++.    ::-----:+*+-        .:-:-+---+++.  \n'
            '  ::-----:+*+          .:-:-=--=++=     ::-----:+*+          .:-:-=--=++=    ::-----:+*+          .:-:-=--=++=    ::-----:+*+          .:-:-=--=++=  \n'
            ' .::-----:+*+           .:=--+--=+*-   .::-----:+*+           .:=--+--=+*-   ::-----:+*+           .:=--+--=+*-  .::-----:+*+           .:=--+--=+*- \n'
            ' .::-----:+*+            .:=-==-=+++.  .::-----:+*+            .:=-==-=+++.. ::-----:+*+            .:=-==-=+++. .::-----:+*+            .:=-==-=+++.\n'
            ' .::----==+*+             :-=-+-==+*:  .::----==+*+             :-=-+-==+*:. ::----==+*+             :-=-+-==+*: .::----==+*+             :-=-+-==+*:\n'
            '  :-=---==+++             ::=-=====+-   :-=---==+++             ::=-=====+-  :-=---==+++             ::=-=====+-  :-=---==+++             ::=-=====+-\n'
            '  :-=---===+*=            .::-==-:-+=   :-=---===+*=            .::-==-:-+=  :-=---===+*=            .::-==-:-+=  :-=---===+*=            .::-==-:-+=\n'
            '  .:=----==+++.            ::-==-:-++   .:=----==+++.            ::-==-:-++  .:=----==+++.            ::-==-:-++  .:=----==+++.            ::-==-:-++\n'
            '   :=-----=++*=            ::====:=+=    :=-----=++*=            ::====:=+=   :=-----=++*=            ::====:=+=   :=-----=++*=            ::====:=+=\n'
            '   .:=-----=++*-          .:==+==-+*=    .:=-----=++*-          .:==+==-+*=   .:=-----=++*-          .:==+==-+*=   .:=-----=++*-          .:==+==-+*=\n'
            '    :-------=++*=         ::=-+-+++*-     :-------=++*=         ::=-+-+++*-    :-------=++*=         ::=-+-+++*-    :-------=++*=         ::=-+-+++*-\n'
            '     :--------++*+.      .:--*:=++*+.      :--------++*+.      .:--*:=++*+.     :--------++*+.      .:--*:=++*+.     :--------++*+.      .:--*:=++*+.\n'
            '      :--------=+*++:   .:-*+:=+***=        :--------=+*++:   .:-*+:=+***=       :--------=+*++:   .:-*+:=+***=       :--------=+*++:   .:-*+:=+***= \n'
            '       :---------+*****++*#*+*****+          :---------+*****++*#*+*****+         :---------+*****++*#*+*****+         :---------+*****++*#*+*****+  \n'
            '        .:-:------=+************++.           .:-:------=+************++.          .:-:------=+************++.          .:-:------=+************++.  \n'
            '         .::::------=++********+=              .::::------=++********+=             .::::------=++********+=             .::::------=++********+=    \n'
            '           .:::::------==++++++.                 .:::::------==++++++.                .:::::------==++++++.                .:::::------==++++++.     \n'
            '              .:--:-::----==-                       .:--:-::----==-                      .:--:-::----==-                      .:--:-::----==-        \n'
            '                   ..::..                                ..::..                               ..::..                               ..::..            \n'
            '                                                                                                                                                     \n')
        print(
            "-----------------------------------------------------------------------------------------------------------------------------------------------------\n")

        print(f"     Suas Moedas: {moedas} Moedas")
        print("        Ganhe mais moedas     \n"
              "     - Andando de bicicleta   \n"
              " - Interagindo na comunidadde \n"
              "        - Fazendo quizes      \n")

        objetos = ['Broche', 'Bike', 'Copo', 'Desconto']
        objetos_valores = [1000, 2000, 6000, 6500]
        while True:
            escolha_gastar = forca_opcao("Deseja trocar suas moedas por recompensas? (s/n) ", sim_nao)
            if escolha_gastar == 's':
                print("                       Loja\n"
                      "Broche Personalizado - 1000 moedas (Digite Broche)\n"
                      "1KM Bike Elétrica - 2000 moedas (Digite Bike)\n"
                      "Copo Staley - 6000 moedas (Diite Copo)\n"
                      "20% de desonto no ingresso formula-e - 6500 (Diite Desconto)\n")
                escolha_objeto = forca_opcao("Qual você gostaria de comprar? \n", objetos)

                index_objeto = meu_index(objetos, escolha_objeto)
                valor = objetos_valores[index_objeto]

                if valor > moedas:
                    print("Você não moedas o suficiente para comprar")
                else:
                    moedas -= valor
                    print(f"Você comprou {escolha_objeto} por {valor} moedas! Você tem {moedas} moedas agora!")
                    print(f"Seu pedido será enviado para o endereço - {endereco} em 5 dias úteis\n")
            else:
                break

        escolha = forca_opcao(
            "Home - H | AroundCity - A | Bicicletas - B | Community - C | Moedas - M | Encerrar sessão - E: ", telas)
        print('\n')

print('Obrigado por visitar nosso site! Volte sempre!')
