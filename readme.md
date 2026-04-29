# Projeto - Persistência de Dados com Python

## Descrição

Este projeto tem como objetivo demonstrar, de forma prática, conceitos fundamentais de persistência de dados em Python, incluindo:

* Ordenação de arrays
* Implementação de algoritmos de ordenação (Bubble Sort e Selection Sort)
* Leitura de arquivos externos
* Escrita de dados em arquivos
* Comparação de performance entre algoritmos

---

## Requisitos

* Python 3 instalado (no Linux/WSL utilize `python3`)

---

## Como executar

1. Abra o projeto no VS Code
2. Abra o terminal na pasta do projeto

### Microatividades

Execute os arquivos abaixo:

```bash
python3 array.sort.py
python3 bubble.sort.py
python3 selection.sort.py
python3 ler.txt.py
python3 escrever.txt.py
```

---

### Trabalho final

Execute:

```bash
python3 kdd.py
```

---

## Arquivos gerados

Após a execução, serão criados:

* `texto.txt`: arquivo com dados escritos pelo script
* `resultado.txt`: palavras ordenadas a partir do arquivo de entrada

---

## Observações

* O arquivo `loremipsum.txt` é utilizado como base para leitura de dados
* O script `kdd.py` realiza a comparação de desempenho entre:

  * Bubble Sort
  * Selection Sort
  * Método nativo do Python (`sort`)

---

## Execução com Docker

Este projeto também pode ser executado utilizando Docker, garantindo um ambiente isolado e padronizado.

### Pré-requisitos

* Docker instalado
* Docker Compose instalado

### Como executar com Docker

No terminal, navegue até a pasta do projeto:

```bash
cd Trabalho-Python
```

Execute o comando:

```bash
docker compose up --build
```

### O que esse comando faz

* Constrói a imagem do projeto
* Cria e inicia o container
* Executa os scripts automaticamente

### Parar o container

```bash
docker compose down
```

### Observação sobre o uso do Docker

O uso do Docker neste projeto é opcional e foi adotado como uma prática adicional para padronização do ambiente de desenvolvimento.

Todos os scripts também podem ser executados normalmente sem Docker, utilizando apenas Python 3.

---

## Objetivo acadêmico

Aplicar conceitos de manipulação de arquivos e algoritmos de ordenação, analisando na prática a eficiência entre diferentes abordagens.
