estados_paraguai = [
    "alto paraguay",
    "alto paraná",
    "amambay",
    "boquerón",
    "caaguazú",
    "caazapá",
    "canindeyú",
    "central",
    "concepción",
    "guairá",
    "itapúa",
    "cordillera",
    "misiones",
    "ñeembucú",
    "paraguarí",
    "presidente hayes",
    "san pedro"
]


print(estados_paraguai)
estados = input("qual estado")
estados = estados.lower()

if estados in estados_paraguai:
      print(estados, "está no paraguai")
else:
      print(estados, "não está no paraguai")