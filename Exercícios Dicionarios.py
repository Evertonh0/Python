# Crie um dicionário chamado aluno que armazene o nome, idade e nota final de um estudante. Depois, imprima cada informação em uma linha separada, no formato:

aluno = {
    'nome': str(input('Digite aqui um nome ao dicionario: ')),  # Não esquecer as virgulas
    'idade': int(input('Digite aqui a idade ao dicionario: ')),
    'nota_final': float(input('Digite aqui a nota final: ')),
    }
print(type(aluno['nome']))
print(type(aluno['idade']))
print(type(aluno['nota_final']))

print(f'Nome: {aluno['nome']}')
print(f'Idade: {aluno['idade']}')
print(f'Nota Final: {aluno['nota_final']}')
print('Fim do programa')
    
