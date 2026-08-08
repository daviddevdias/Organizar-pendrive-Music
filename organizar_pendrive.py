#!/usr/bin/env python3
"""
Organizador de músicas para pendrive - modo RODÍZIO
------------------------------------------------------
Pega até 5 músicas de cada pasta de artista por vez, dá a volta em
todas as pastas, e repete. Quando uma pasta esgota as músicas, ela
sai do rodízio e as outras continuam até esgotar tudo.

Exemplo: se "eduardo" tem 73 músicas e "zeze" tem 10, o resultado
vai ser algo como:

    5 bruno e marrone | 5 eduardo | 5 zeze | 5 bruno e marrone |
    5 eduardo | 5 zeze | ... até zeze acabar (rodada com só 10) |
    ... continua só bruno e marrone / eduardo ... até tudo acabar.

Como usar:
1. Ajuste PASTA_ORIGEM e PASTA_DESTINO abaixo (exemplo já configurado
   pra estrutura "D:/musicas" que você mostrou).
2. Se quiser uma ORDEM específica de artistas, preencha a lista
   ORDEM_ARTISTAS com o nome EXATO das pastas, na ordem que quiser
   que toquem. Se deixar como None, usa ordem alfabética das pastas.
3. Rode: python organizar_pendrive.py
"""

import shutil
from pathlib import Path

# ===================== CONFIGURAÇÃO =====================

# Pasta onde estão as pastas de cada artista/banda
PASTA_ORIGEM = "D:/musicas"

# Pasta de destino (pode apontar direto pro pendrive)
PASTA_DESTINO = "D:/pendrive_organizado"

# Quantas músicas por "rodada" de cada artista
TAMANHO_BLOCO = 5

# Ordem dos artistas (nome tem que ser IGUAL ao nome da pasta).
# Deixe None pra usar ordem alfabética automática das pastas.
ORDEM_ARTISTAS = None
# Exemplo de uso manual:
# ORDEM_ARTISTAS = [
#     "bruno e marrone",
#     "eduardo",
#     "Zeze",
#     "raca negra",
# ]

# Extensões de áudio que serão consideradas música
EXTENSOES_VALIDAS = {".mp3", ".wav", ".flac", ".m4a", ".ogg"}

# ==========================================================


def listar_musicas(pasta: Path):
    """Lista os arquivos de música de uma pasta, em ordem alfabética."""
    if not pasta.exists():
        return []
    return sorted(
        f for f in pasta.iterdir()
        if f.is_file() and f.suffix.lower() in EXTENSOES_VALIDAS
    )


def organizar():
    origem = Path(PASTA_ORIGEM)
    destino = Path(PASTA_DESTINO)
    destino.mkdir(parents=True, exist_ok=True)

    if ORDEM_ARTISTAS:
        nomes_artistas = ORDEM_ARTISTAS
    else:
        nomes_artistas = sorted(
            p.name for p in origem.iterdir() if p.is_dir()
        )

    filas = {}
    for nome in nomes_artistas:
        musicas = listar_musicas(origem / nome)
        if musicas:
            filas[nome] = musicas
            print(f"Encontrado: {nome} ({len(musicas)} música(s))")
        else:
            print(f"[AVISO] pasta vazia ou não encontrada: {nome}")

    ativos = [n for n in nomes_artistas if n in filas]

    contador = 1
    total = 0
    rodada = 1

    while ativos:
        print(f"\n--- Rodada {rodada} ---")
        proxima_rodada = []

        for nome in ativos:
            bloco = filas[nome][:TAMANHO_BLOCO]
            filas[nome] = filas[nome][TAMANHO_BLOCO:]

            if not bloco:
                continue

            print(f"\n>> {nome} ({len(bloco)} música(s) nesta rodada)")
            for musica in bloco:
                prefixo = f"{contador:04d}"
                novo_nome = f"{prefixo} - {nome} - {musica.name}"
                shutil.copy2(musica, destino / novo_nome)
                print(f"   copiado: {novo_nome}")
                contador += 1
                total += 1

            if filas[nome]:
                proxima_rodada.append(nome)

        ativos = proxima_rodada
        rodada += 1

    print(f"\nConcluído! {total} música(s) copiada(s) para '{destino}'")


if __name__ == "__main__":
    organizar()