tem_sementes = input("A planta possui sementes? (S - N): ")

if tem_sementes == "N":
      tem_vasos_condutores = input("A planta possui vasos condutores? (S - N): ")
      if tem_vasos_condutores == "N":
            print("Briófitas")
      else:
            print("Pteridófitas")
else:
      tem_frutos = input("A planta possui frutos?(S - N): ")
      if tem_frutos == "N":
            print("Gimnospermas")
      else:
            print("Angiospermas")