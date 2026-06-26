import json
alunos = {
    "ana": 8.0,
    "pedro": 6.0
}
def add_alunos(alunos, aluno , nota ):
    alunos[aluno] = nota
    return f"Aluno {aluno.capitalize()}, adicionado com sucesso com a nota {nota}"
   
def remov_aluno(alunos,aluno):
    if aluno in alunos:
        del alunos[aluno]
        return f"Aluno: {aluno.capitalize()} , foi removido"
    else:
        return f"o aluno :{aluno.capitalize()} Nao existe"
    

def verificar_aprovado(alunos):
 aprovados = {}
 reprovados = {}
 recuperacao = {}
 for aluno , nota in alunos.items():
  if nota >= 7: 
   aprovados[aluno] = nota
  elif nota >=5 and nota <7 :
   recuperacao[aluno] = nota
  else:
   reprovados[aluno] = nota
 for aluno in aprovados:
  print (f"{aluno.capitalize()} : {aprovados[aluno]} , Aluno aprovado✔️")

 for aluno in recuperacao:
  print (f"{aluno.capitalize()} : {recuperacao[aluno]} , Aluno em Recuperção")

 for aluno in reprovados:
  print (f"{aluno.capitalize()} : {reprovados[aluno]} , Aluno Reprovado❌")

def alterar_notas(alunos):
 while True:
  print(f"""Lista dos Alunos 
        {alunos}""")
  try:
   aluno = str(input("Digite o Nome Do Aluno ou sair para volta ao menu\n"))
   if aluno == "sair":
     break
   if aluno not in alunos :
     nova_nota = float(input(f"Aluno: {aluno.capitalize()} , não encontrado , será adicionado , Digite a Nota\n"))
     alunos[aluno] = nova_nota
     print(f"Aluno {aluno.capitalize()} Foi Adicionado com sucesso com a Nota {nova_nota}")


   else:
     confirmacao = input(f"Nota antiga do aluno {aluno.capitalize()}: {alunos[aluno]} , Deseja alterar?")
     if confirmacao.lower() != "sim":
      continue
     nova_nota = float(input(f"Digite a nova nota do Aluno , {aluno.capitalize()}\n"))
     print(f"A nova nota do Aluno: {aluno.capitalize()}, Foi atualizada com sucesso, Nota: {nova_nota}")
     
   
     
   if nova_nota > 10 or nova_nota <0:
      print("Digite uma nota Valida entre 0 e 10")
      continue
   alunos[aluno] = nova_nota
  except ValueError as erro:
    print("Nota não e Valida, Digite uma nota valida")

def salvar_arquivo(alunos):
    with open ("arquivo.json" , "w") as arquivo:
      json.dump(alunos,arquivo)

def carregar_arquivo():
  try:
    with open("arquivo.json","r") as arquivo:
      return json.load(arquivo)
  except FileNotFoundError as erro:
    print("arquivo nao encontrado")
    return {}

def menu():
    print(
      """  Menu:
        1: Adicionar alunos
        2: Remover alunos
        3: Verificar Aprovação
        4: Media da turma
        5: Alterar Nota
        6: Salva Dados
        7: Carregar Dados
        8: Sair  """""
    )

def media_da_turma(alunos):
   if len(alunos) == 0:
      return "Não há nenhum aluno cadastrado"
   notas = sum(alunos.values()) / len(alunos)
   return f"A media da turma e {notas:.2f}"

def main(alunos):
    while True:
        menu()
        opcao = str(input("Digite uma opção\n"))
        if opcao == "1":
         aluno = input("Nome do aluno\n").lower()
         if aluno in alunos:
             print (f"Ô Aluno(a) {aluno.capitalize()} ja existi")
         else:
            nota = float(input(f"Qual a Nota do Aluno(a): {aluno.capitalize()}\n"))
            if nota <0 or nota >10:
              print("Digite uma nota entre 0 e 10")
            else:   
                print(add_alunos(alunos,aluno,nota))
        elif opcao == "2":
            aluno = input("Nome do aluno\n").lower()
            print(remov_aluno(alunos,aluno))
        elif opcao == "3":
            verificar_aprovado(alunos)
        elif opcao == "4":
            print(media_da_turma(alunos))
        elif opcao == "5":
           alterar_notas(alunos)
        elif opcao == "6":
           sim = input("Deseja salvar os dados? (sim/não)\n").lower()
           if sim == "sim":
                salvar_arquivo(alunos)
                print("Seus Dados Foram Salvos Com sucesso")
           else:
                print("Salvamento Cancelado")
        elif opcao == "7":
          alunos = carregar_arquivo()
          print("Seus dados foram carregados")
        elif opcao == "8":
          break
        else:
            print("Digite uma opção Valida")
    
main(alunos)
