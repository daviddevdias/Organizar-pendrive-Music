# Organizador de músicas para pendrive

Script que intercala músicas de diferentes artistas e copia os arquivos numerados para uma pasta de destino.

## 📌 Funcionalidades

- Alterna blocos de músicas entre artistas.
- Permite definir o tamanho do bloco e a ordem dos artistas.
- Aceita MP3, WAV, FLAC, M4A e OGG.
- Preserva os arquivos de origem.

## Tecnologias

Python 3, pathlib e shutil. Não exige pacotes externos.

## 🚀 Como executar

Configure `PASTA_ORIGEM`, `PASTA_DESTINO` e `TAMANHO_BLOCO` em `organizar_pendrive.py`. A origem deve conter pastas de artistas e o tamanho do bloco deve ser maior que zero.

```bash
git clone https://github.com/daviddevdias/Organizar-pendrive-Music.git
cd Organizar-pendrive-Music
python organizar_pendrive.py
```

Use um destino separado da origem e sem arquivos de mesmo nome. A ordem de reprodução depende do aparelho utilizado.
