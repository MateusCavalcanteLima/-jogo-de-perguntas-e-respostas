def jogo_perguntas():
    print("Bem-vindo ao jogo de perguntas e respostas!")
    print("Você terá 2 tentativas para cada pergunta.")
    print("Pontuação:")
    print("1ª pergunta: 30 pontos")
    print("2ª pergunta: 30 pontos")
    print("3ª pergunta: 40 pontos")
    print("Se errar na primeira tentativa, você perderá 5 pontos por questao.")

    jogar = input("Você quer jogar? (s/n): ").strip().lower()
    if jogar != 's':
        print("Até a próxima!")
        return

    perguntas = {
        "Qual a linguagem que estamos usando?": "Python",
        "Qual é a maior floresta tropical do mundo?": "Amazônia",
        "Quem descobriu o Brasil?": "Índios"
    }

    pontos = 0
    valores = [30, 30, 40]

    for i, (pergunta, resposta_correta) in enumerate(perguntas.items()):
        tentativas = 0
        while tentativas < 2:
            resposta_jogador = input(pergunta + " ").strip().lower()
            if resposta_jogador == resposta_correta.strip().lower():
                print("Resposta correta! Vamos para a próxima pergunta.")
                pontos += valores[i] - (5 if tentativas == 1 else 0)
                break
            else:
                tentativas += 1
                if tentativas < 2:
                    print("Resposta errada! Você tem mais 1 tentativa.")
                else:
                    print(f"Resposta errada! A resposta correta é: {resposta_correta}")

    print(f"Sua pontuação final é: {pontos} pontos.")

if __name__ == "__main__":
    jogo_perguntas()
