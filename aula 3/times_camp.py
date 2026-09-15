campeoes = {
    1930: "Uruguai",
    1934: "Itália",
    1938: "Itália",
    1950: "Uruguai",
    1954: "Alemanha Ocidental",
    1958: "Brasil",
    1962: "Brasil",
    1966: "Inglaterra",
    1970: "Brasil",
    1974: "Alemanha Ocidental",
    1978: "Argentina",
    1982: "Itália",
    1986: "Argentina",
    1990: "Alemanha Ocidental",
    1994: "Brasil",
    1998: "França",
    2002: "Brasil",
    2006: "Itália",
    2010: "Espanha",
    2014: "Alemanha",
    2018: "França",
    2022: "Argentina",
    2026: "Espanha",
}

times = list(campeoes.values())

time_consultado = input("Digite o nome do time que deseja consultar: ").strip()

vitorias = sum(1 for time in times if time.lower() == time_consultado.lower())

if vitorias > 0:
    print(f"O {time_consultado} foi campeão mundial {vitorias} vez(es).")
else:
    print(f"O {time_consultado} nunca foi campeão mundial.")
