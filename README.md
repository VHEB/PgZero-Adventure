<h1 align="center"> Adventure World </h1>


<p align="center">
  <a href="#-guia">Guia</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#book-bibliotecas">Bibliotecas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;
  <a href="#email-contato">Contato</a>&nbsp;&nbsp;&nbsp;
</p>


## 🚀 **Guia**

Este guia descreve como clonar o repositório, criar um ambiente virtual em Python e instalar as dependências do projeto usando o arquivo `requirements.txt`.

---

 1 - **Clone do Repositório**

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/VHEB/PgZero-Adventure.git
```

Navegue até a pasta do projeto.

---

## 2 - **Crie um Ambiente Virtual**

Crie e ative um ambiente virtual para isolar as dependências do projeto:

### **Windows**

1. Crie o ambiente virtual:
   ```bash
   python -m venv .venv
   ```

2. Ative o ambiente virtual:
   ```bash
   .venv\Scripts\activate
   ```

### **macOS/Linux**

1. Crie o ambiente virtual:
   ```bash
   python3 -m venv .venv
   ```

2. Ative o ambiente virtual:
   ```bash
   source .venv/bin/activate
   ```

Quando o ambiente virtual estiver ativo, você verá algo semelhante a `(venv)` no início da linha de comando.

---

## 3 - **Instale as Dependências**

Com o ambiente virtual ativo, instale as dependências do projeto listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 4 - **Verifique o Setup**

Certifique-se de que todas as dependências foram instaladas corretamente executando o comando:

```bash
pip list
```

---

## 5 - **Inicie o Projeto**

Agora você está pronto para executar o projeto!

Rode o código abaixo no terminal e divirta-se.
```bash
pgzrun main.py
```

## :book: **Bibliotecas**

Esse projeto foi desenvolvido com as seguintes bibliotecas:

- PgZero
- PyGame
- NumPy

## 💻 **Projeto**

Adventure World nasce em de um desafio de criar um game com `pgzero`. Ele é um game de plataforma em que o personagem pode andar, pular, coletar moedas e perde vida ao encostar no `enemy`, o `herói` vence ao coletar todas as moedas e perder quando sua vida chegar a ZERO. 

Esse projeto utilizou de conceitos de Loop, Condicionais de Decisão, Tratamento de Erros, Funções, Física, um pouco de criativida artística e muita muita LOGICA.

## :email: **Contato**

Se precisar de ajuda, sinta-se à vontade para perguntar!

Você também pode me encontrar no [LinkedIn](https://www.linkedin.com/in/vitor-heb/).


