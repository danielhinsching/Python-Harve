# Curso de Python — Materiais das Aulas

Este repositório reúne os exercícios e exemplos usados em aula. Cada pasta `aula X`
corresponde a um encontro e contém os arquivos `.py` praticados naquele dia.

## Dinâmica dos materiais

- Aula 1 → pasta [`aula 1/`](aula%201/)
- Aula 2 → pasta [`aula 2/`](aula%202/)

A cada nova aula, uma nova pasta `aula N` será adicionada com os arquivos daquele
conteúdo. Os arquivos dentro de cada pasta são independentes entre si — cada `.py`
resolve um exercício específico e pode ser executado sozinho.

### Aula 1 — Input e Output

Foco em ler dados do usuário e exibir resultados na tela.

- `input()` — pede uma informação digitada pelo usuário (sempre retorna texto/string).
- `print()` — exibe informações na tela.

Exemplo (`aula 1/infos.py`):

```python
nome = input("qual seu nome:")
estado = input("qual seu estado:")

print("meu nome é", nome, "e nasci no", estado)
```

Arquivos da pasta: `primeiro.py`, `segudo.py`, `teste.py`, `infos.py`, `lampadas.py`,
`idades2.py`, `combustivel.py`, `descontos.py`, `media_pond.py`, `parcela.py`,
`desafios.py`.

### Aula 2 — If, Else e Listas

Foco em tomar decisões no código (condicionais) e em armazenar/manipular
coleções de valores (listas).

- `if` / `else` — executam um bloco de código dependendo de uma condição ser
  verdadeira ou falsa.
- Listas (`[]`) — guardam vários valores em uma única variável, com métodos como
  `append()` (adicionar), `pop()` (remover) e o operador `in` (verificar se um
  item está na lista).

Exemplo simplificado (`aula 2/plantas.py`):

```python
tem_sementes = input("O vegetal tem sementes?(S - N) ")

if tem_sementes == "sim":
    print("Pode ser uma planta com sementes")
else:
    print("Não tem sementes")
```

Exemplo com lista (`aula 2/salada.py`):

```python
frutas = ["Banana", "Maçã", "Uva", "Manga"]

fruta = input("Digite uma fruta: ")
if fruta not in frutas:
    frutas.append(fruta)

print(frutas)
```

Arquivos da pasta: `temperatura.py`, `temperatura2.py`, `plantas.py`,
`plantas_desafio.py`, `IR.py`, `salada.py`.

## Como rodar um exercício

1. Abra o terminal na pasta do repositório.
2. Execute o arquivo desejado com Python:

   ```bash
   python "aula 1/infos.py"
   ```

3. Digite as respostas pedidas pelo `input()` e veja o resultado no terminal.

## Git básico

Git é a ferramenta usada para guardar o histórico de mudanças do código. Comandos
essenciais para acompanhar o repositório da aula:

| Comando | O que faz |
|---|---|
| `git clone <url>` | Baixa uma cópia do repositório para o seu computador (usar só uma vez). |
| `git status` | Mostra o que mudou desde o último salvamento (commit). |
| `git pull` | Baixa as atualizações mais recentes enviadas pelo professor/colegas. |
| `git add <arquivo>` | Marca um arquivo para ser incluído no próximo commit. Use `git add .` para marcar tudo que mudou. |
| `git commit -m "mensagem"` | Salva as mudanças marcadas, com uma mensagem explicando o que foi feito. |
| `git push` | Envia os commits salvos localmente para o repositório remoto (ex: GitHub). |
| `git log` | Mostra o histórico de commits já feitos. |

### Fluxo básico do dia a dia

```bash
git pull                       # 1. Atualizar com o que já existe no repositório
# ... editar/criar seus arquivos .py ...
git add .                      # 2. Selecionar as mudanças
git commit -m "resolvi o exercício da aula 2"   # 3. Salvar as mudanças com uma mensagem
git push                       # 4. Enviar para o repositório remoto
```

**Dica:** rode `git status` sempre que tiver dúvida sobre o que já foi salvo ou não.
