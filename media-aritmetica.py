# Média aritmética a partir do recebimento de três notas.
# 0 <= média < 3	= Reprovado
# 3 <= média < 6	= Exame
# 6 <= média <= 10	= Aprovado
# SE media >= 3 E media < 6
    # ESCREVA “Exame”
    # nota_exame = 12 - media
    # ESCREVA “Você deve tirar a nota”, nota_exame, “para ser aprovado.”

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
nota_exame = 12 - media
if media >= 0 and media < 3:
  print('Você precisará tirar',nota_exame,'para ser aprovado.')
elif media >= 3 and media < 6:
  print('Você precisará tirar',nota_exame,'para ser aprovado.')
else:
  print('Você foi aprovado.')
