def jogo_perguntas():
    perguntas = {
        "Qual a linguagem que estamos usando?": "Python",
        "Qual é a maior floresta tropical do mundo?": "Amazonia",
        "Quem descobriu o Brasil?": "Índios"
    }

    for pergunta, resposta_correta in perguntas.items():
        tentativas = 0
        while tentativas < 2:
            resposta_jogador = input(pergunta + " ").strip().lower()
            if resposta_jogador == resposta_correta.strip().lower():
                print("Resposta correta! Vamos para a próxima pergunta.")
                break
            else:
                tentativas += 1
                if tentativas < 2:
                    print("Resposta errada! Você tem mais 1 tentativa.")
                else:
                    print(f"Resposta errada! A resposta correta é: {resposta_correta}")

if __name__ == "__main__":
    jogo_perguntas()
