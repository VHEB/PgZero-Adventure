# Setup do Projeto

Este guia descreve como clonar o repositório, criar um ambiente virtual em Python e instalar as dependências do projeto usando o arquivo `requirements.txt`.

---

## 1. **Clone do Repositório**

Primeiro, clone o repositório para sua máquina local:

```bash
# Substitua o link abaixo pelo link do repositório que você deseja clonar
git clone https://github.com/VHEB/PgZero-Adventure.git
```

Navegue até a pasta do projeto:

```bash
cd repositorio
```

---

## 2. **Crie um Ambiente Virtual**

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

## 3. **Instale as Dependências**

Com o ambiente virtual ativo, instale as dependências do projeto listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 4. **Verifique o Setup**

Certifique-se de que todas as dependências foram instaladas corretamente executando o comando:

```bash
pip list
```

---

## 5. **Inicie o Projeto**

Agora você está pronto para executar o projeto! Consulte a documentação ou os arquivos do repositório para instruções específicas sobre como rodar o código.

Se precisar de ajuda, sinta-se à vontade para perguntar!

