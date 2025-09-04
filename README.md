# 🧮 Simulador de Algoritmos de Substituição de Páginas

## 📚 Visão Geral

Este repositório contém a implementação em **Python** de três algoritmos
clássicos de **substituição de páginas** utilizados em sistemas
operacionais:

- **FIFO (First-In, First-Out)**\
- **Ótimo (OTM)**\
- **LRU (Least Recently Used)**

O programa lê um arquivo de entrada contendo o número de quadros
disponíveis na memória e uma sequência de referências de páginas, e em
seguida simula os algoritmos, exibindo a quantidade de **faltas de
página** geradas por cada um.

---

## ⚙️ Estrutura do Projeto

    📂 projeto-substituicao-paginas
     ┣ 📜 main.py          # Código principal com os algoritmos
     ┣ 📜 input1.txt       # Arquivo de entrada exemplo 1
     ┣ 📜 Input2.txt       # Arquivo de entrada exemplo 2
     ┣ 📜 input3.txt       # Arquivo de entrada exemplo 3
     ┣ 📜 input4.txt       # Arquivo de entrada exemplo 4
     ┗ 📜 README.md        # Documentação do projeto

---

## 📥 Formato de Entrada

O programa lê os dados de um arquivo `.txt` no seguinte formato:

- **Primeira linha:** quantidade de quadros disponíveis na memória.\
- **Demais linhas:** sequência de referências de páginas (uma por
  linha).

### Exemplos:

#### 🔹 `input1.txt`

    4
    1
    2
    3
    4
    1
    2
    5
    1
    2
    3
    4
    5

#### 🔹 `Input2.txt`

    3
    1
    2
    3
    4
    2
    1
    5
    1
    2
    3

#### 🔹 `input3.txt`

    3
    1
    2
    5
    2
    3
    4
    7
    2
    7
    4
    5
    3
    5
    2

#### 🔹 `input4.txt`

    3
    1
    2
    3
    4
    5
    6

---

## 📤 Saída

A saída é impressa no terminal com o número total de **faltas de
página** para cada algoritmo:

    FIFO 9
    OTM 8
    LRU 10

---

## ▶️ Como Executar

1.  Clone este repositório:

```bash
git clone https://github.com/seu-usuario/projeto-substituicao-paginas.git
```

2.  Acesse a pasta do projeto:

```bash
cd projeto-substituicao-paginas
```

3.  Execute o programa (por padrão ele usa `input4.txt`):

```bash
python main.py
```

Se quiser usar outro arquivo de entrada, basta editar a variável
`nome_arquivo` dentro do `main.py`.

---

## 📌 Algoritmos Implementados

### 🔹 FIFO (First-In, First-Out)

- Substitui a página que está há mais tempo na memória.\
- Simples, mas pode gerar muitas faltas dependendo da sequência.

### 🔹 Ótimo (OTM)

- Substitui a página que **não será utilizada por mais tempo no
  futuro**.\
- Garante o **menor número possível de faltas de página**, mas requer
  conhecimento prévio da sequência.

### 🔹 LRU (Least Recently Used)

- Substitui a página **menos recentemente utilizada**.\
- É mais realista que o ótimo, mas exige controle do histórico de uso.

---

## 📝 Licença

Este projeto é de uso livre para fins educacionais.\
Sinta-se à vontade para contribuir e melhorar! 🎉
