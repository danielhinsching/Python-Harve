tem_sementes = input("O vegetal tem sementes?(S - N) ")
tem_flores = input("O vegetal tem flores?(S - N) ")
depende_de_agua = input("O vegetal depende de água para reprodução?(S - N)")
tem_frutos = input("O vegetal tem frutos?(S - N) ")
tem_vasos_condutores = input("O vegetal tem vasos condutores?(S - N)")

if tem_sementes == "não" and tem_flores == "não" and depende_de_agua == "sim" and tem_frutos == "não" and tem_vasos_condutores == "não":
      print("Briófitas")
else:
      if tem_sementes == "não" and tem_flores == "não" and depende_de_agua == "sim" and tem_frutos == "não" and tem_vasos_condutores == "sim":
            print("Pteridófitas")
      else:
            if tem_sementes == "sim" and tem_flores == "não" and depende_de_agua == "não" and tem_frutos == "não" and tem_vasos_condutores == "sim":
                  print("Gimnospermas")
            else:
                  if tem_sementes == "sim" and tem_flores == "sim" and depende_de_agua == "não" and tem_frutos == "sim" and tem_vasos_condutores == "sim":
                        print("Angiospermas")
                  else:
                        print("Não foi possível identificar o grupo vegetal com as respostas informadas")