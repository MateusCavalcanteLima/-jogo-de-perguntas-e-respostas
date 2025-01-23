def jogo_perguntas():
    perguntas = {
        "Qual a linguagem que estamos usando?": "Python",
        "Qual é a maior floresta tropical do mundo?": "Amazonia",
        "Quem descobriu o brasil?": "Indios"
    }

    for pergunta, resposta_correta in perguntas.items():
        resposta_jogador = input(pergunta + " ").lower()
        if resposta_jogador == resposta_correta.lower():
            print("Resposta correta!")
        else:
            print(f"Resposta errada! A resposta correta é: {resposta_correta}")

if __name__ == "__main__":
    jogo_perguntas()
