def jogo_perguntas():
    perguntas = {
        "Qual a linguagem que estamos usando?": "Python",
        "Qual é a maior floresta tropical do mundo?": "Amazônia",
        "Quem descobriu o brasil?": "Indios"
    }

    for pergunta, resposta_correta in perguntas.items():
        tentativas = 0
        while tentativas < 2:
            resposta_jogador = input(pergunta + " ").lower()
            if resposta_jogador == resposta_correta.lower():
                print("Resposta correta!")
                break
            else:
                print("Resposta errada!")
                tentativas += 1
                if tentativas == 2:
                    print(f"A resposta correta é: {resposta_correta}")

if __name__ == "__main__":
    jogo_perguntas()
