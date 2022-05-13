import random

print('PASSWORD RANDOM GENERATOR')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*().,-?0123456789'
lowercase = chars[0:26]
uppercase = chars[26:52]
specialcharacters = chars[52:66]
numbers = chars[66:76]

quantidade = input('QUANTIDADE DE SENHAS PARA GERAR: \n')
if quantidade.isdigit() == False:
    exit()
quantidade = int(quantidade)

tamanho = input('\nNÚMERO DE CARACTERES: \n')
if tamanho.isdigit() == False:
    exit()
tamanho= int(tamanho)

lower = input('\nCONTER LETRAS MINÚSCULAS?(s/n) \n')
if lower == 'n':
    chars = chars.replace(lowercase[:], '')

upper = input('\nCONTER LETRAS MAIÚSCULAS?(s/n) \n')
if upper == 'n':
    chars = chars.replace(uppercase[:], '')

special = input('\nCONTER CARACTERES ESPECIAIS(s/n) \n')
if special == 'n':
    chars = chars.replace(specialcharacters[:], '')

num = input('\nCONTER NÚMEROS?(s/n) \n')
if num == 'n':
    chars = chars.replace(numbers[:], '')

if (lower == 'n') and (upper == 'n') and (special == 'n') and (num == 'n'):
    print('ENTÃO NÃO VAI TER SENHA.')
    exit()

def password_genetor(amount, length, character):
    print("SUAS SENHAS: \n")
    for passwrd in range(amount):
        passwords = ''
        for v in range(length):
            passwords +=random.choice(character)
        print(passwords)

password_genetor(quantidade, tamanho, chars)
input('')
