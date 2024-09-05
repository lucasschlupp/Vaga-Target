num = int(input("Digite um número de no máximo TRÊS dígitos.\nVamos ver se ele se encontra na sequência de Fibonacci? "))

primeiro_num = 0
segundo_num = 1

fib = [0, 1]

for _ in range(15):
    terceiro_num = primeiro_num + segundo_num
    fib.append(terceiro_num)
    primeiro_num = segundo_num
    segundo_num = terceiro_num

print("Essa é a sequência de Fibonacci:")
print("_" * 20)
print(', '.join(map(str, fib)))
print("_" * 20)
if num in fib:
    print(f"Parabéns, você digitou o número {num}, que se encontra na sequência de Fibonacci!")
else:
    print(f"Que pena! Como podes ver, o número {num} não está na sequência de Fibonacci!")