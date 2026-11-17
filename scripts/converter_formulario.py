import csv
from pathlib import Path
from collections import Counter

ARQUIVO_ENTRADA = Path("dados/respostas_formulario.csv")
ARQUIVO_SAIDA = Path("dados/respostas_classificadas.csv")

# Classificacao individual das perguntas 1 a 5, na ordem dos participantes.
CLASSIFICACOES = [
    ["fora_dominio", "wifi", "fora_dominio", "senha", None],
    ["sistemas", "sistemas", "fora_dominio", "senha", "wifi"],
    ["suporte", "sistemas", "sistemas", "autenticacao", "wifi"],
    ["senha", "wifi", "fora_dominio", "email", "wifi"],
    ["suporte", "sistemas", "fora_dominio", "senha", "wifi"],
    ["ava", "sistemas", "suporte", "senha", "wifi"],
    ["suporte", "google_drive", "fora_dominio", "email", "wifi"],
    ["sistemas", "email", "sistemas", "email", "wifi"],
]

def main():
    with ARQUIVO_ENTRADA.open("r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.reader(arquivo)
        linhas = list(leitor)

    if len(linhas) != 9:
        raise ValueError(
            f"Esperados 8 participantes, encontrados {len(linhas) - 1}. "
            "Revise as classificacoes antes de continuar."
        )

    if len(linhas[0]) != 12:
        raise ValueError("O formulario nao possui as 11 perguntas esperadas.")

    respostas = []

    for participante, linha in enumerate(linhas[1:]):
        if len(linha) != 12:
            continue

        for pergunta in range(1, 12):
            texto = linha[pergunta].strip()

            if not texto:
                continue

            if pergunta <= 5:
                intencao = CLASSIFICACOES[participante][pergunta - 1]
            elif pergunta <= 8:
                intencao = "chitchat"
            else:
                intencao = "fora_dominio"

            if intencao is None:
                continue

            if texto.lower() == "como":
                continue

            respostas.append({
                "texto": texto,
                "intencao": intencao,
                "origem": "coletado"
            })

    with ARQUIVO_SAIDA.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=["texto", "intencao", "origem"]
        )
        escritor.writeheader()
        escritor.writerows(respostas)

    contagem = Counter(r["intencao"] for r in respostas)

    print(f"\nArquivo criado: {ARQUIVO_SAIDA}")
    print(f"Total de respostas aproveitadas: {len(respostas)}")
    print("\nQuantidade por intencao:")

    for intencao, quantidade in sorted(contagem.items()):
        print(f"{intencao}: {quantidade}")

    print(f"\nRespostas descartadas: {88 - len(respostas)}")

if __name__ == "__main__":
    main()
