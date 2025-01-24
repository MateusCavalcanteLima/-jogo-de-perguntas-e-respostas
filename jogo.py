def jogo_perguntas():
    print("Bem-vindo ao jogo de perguntas e respostas!")
    print("Você terá 2 tentativas para cada pergunta.")
    print("Pontuação:")
    print("1ª pergunta: 30 pontos")
    print("2ª pergunta: 30 pontos")
    print("3ª pergunta: 40 pontos")
    print("Se errar na primeira tentativa, você perderá 10 pontos por questão.")
    print("Você terá uma chance extra para cada pergunta no final, valendo 15 pontos.")

    jogador1 = input("Nome do jogador 1: ").strip()
    jogador2 = input("Nome do jogador 2: ").strip()

    perguntas = {
        "Qual a linguagem que estamos usando?": "Python",
        "Qual é a maior floresta tropical do mundo?": "Amazonia",
        "Quem descobriu o Brasil?": "Indios"
    }

    def jogar(jogador):
        pontos = 0
        valores = [30, 30, 40]
        respostas_erradas = []

        for i, (pergunta, resposta_correta) in enumerate(perguntas.items()):
            tentativas = 0
            while tentativas < 2:
                resposta_jogador = input(f"{jogador}, {pergunta} ").strip().lower()
                if resposta_jogador == resposta_correta.strip().lower():
                    if tentativas == 0:
                        pontos += valores[i]
                        print("Resposta correta! Vamos para a próxima pergunta.")
                    else:
                        pontos += valores[i] - 10
                        print("Resposta correta! Vamos para a próxima pergunta.")
                    break
                else:
                    tentativas += 1
                    if tentativas < 2:
                        print("Resposta errada! Você tem mais 1 tentativa.")
                    else:
                        print(f"Resposta errada! A resposta correta é: {resposta_correta}")
                        respostas_erradas.append((pergunta, resposta_correta, valores[i]))

        if respostas_erradas:
            print(f"\n{jogador}, você terá uma chance extra para as perguntas que errou.")
            for pergunta, resposta_correta, valor in respostas_erradas:
                resposta_jogador = input(f"{jogador}, {pergunta} ").strip().lower()
                if resposta_jogador == resposta_correta.strip().lower():
                    pontos += 15
                    print("Resposta correta!")
                else:
                    print(f"Resposta errada novamente! A resposta correta é: {resposta_correta}")

        return pontos

    pontos_jogador1 = jogar(jogador1)
    pontos_jogador2 = jogar(jogador2)

    print(f"\nPontuação final:")
    print(f"{jogador1}: {pontos_jogador1} pontos")
    print(f"{jogador2}: {pontos_jogador2} pontos")

    if pontos_jogador1 > pontos_jogador2:
        print(f"{jogador1} venceu!")
    elif pontos_jogador2 > pontos_jogador1:
        print(f"{jogador2} venceu!")
    else:
        print("Empate!")

if __name__ == "__main__":
    jogo_perguntas()
