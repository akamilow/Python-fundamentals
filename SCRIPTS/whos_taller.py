T = int(input())

lista = []

for i in range(T):
  t = input().split(" ")

  if t[0] > t[1]:
    lista.append("a")
  else:
    lista.append("b")

print(*lista)
    