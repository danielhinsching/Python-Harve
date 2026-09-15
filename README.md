# Curso de Python — Materiais das Aulas

Este repositório reúne os exercícios e exemplos usados em aula. Cada pasta `aula X`
corresponde a um encontro e contém os arquivos `.py` praticados naquele dia.

## Dinâmica dos materiais

- Aula 1 → pasta [`aula 1/`](aula%201/)
- Aula 2 → pasta [`aula 2/`](aula%202/)
- Aula 3 → pasta [`aula 3/`](aula%203/)

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
`plantas_desafio.py`, `IR.py`, `salada.py`, `revisao1.py`, `revisao2.py`
(esses dois últimos são enunciados de revisão ainda sem solução implementada).

### Aula 3 — Funções, Listas e Dicionários

Foco em organizar o código em funções reutilizáveis e em representar dados
reais com listas e dicionários.

- `def` — cria uma função, um bloco de código reutilizável que recebe
  parâmetros e pode devolver um valor com `return`.
- Dicionários (`{chave: valor}`) — associam uma chave a um valor, por exemplo
  um ano à seleção campeã daquele ano.
- Recursão — uma função chamando a si mesma para repetir uma ação sem usar
  `while` (usado no exercício da calculadora).

Exemplo (`aula 3/velocidade.py`):

```python
def velocidade_media(distancia, tempo):
    return distancia / tempo


distancia = float(input("Digite a distância percorrida (km): "))
tempo = float(input("Digite o tempo da viagem (horas): "))

print(f"A velocidade média foi de {velocidade_media(distancia, tempo)} km/h")
```

Exemplo com dicionário (`aula 3/times_camp.py`):

```python
campeoes = {1958: "Brasil", 1962: "Brasil", 2002: "Brasil", 2022: "Argentina"}

time_consultado = input("Digite o nome do time: ").strip()
vitorias = sum(1 for time in campeoes.values() if time.lower() == time_consultado.lower())

print(f"O {time_consultado} foi campeão {vitorias} vez(es).")
```

Arquivos da pasta:

| Arquivo | O que faz |
|---|---|
| `bootcamp.py` | Calculadora (+, -, \*, /) que repete o cálculo por recursão, sem usar `while`. |
| `filmes.py` | Recebe o ano de nascimento e retorna o filme vencedor do Oscar daquele ano (1950–2010). |
| `media_lista.py` | Calcula a média de uma lista fixa de números. |
| `paraguai.py` | Lista com os 17 estados (departamentos) do Paraguai. |
| `pin.py` | Jogo do "pin": conta até um limite substituindo os múltiplos de um número por "pin". |
| `times_camp.py` | Dicionário com os campeões da Copa do Mundo; conta quantas vezes um time consultado já venceu. |
| `velocidade.py` | Calcula a velocidade média a partir da distância e do tempo de uma viagem. |

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
