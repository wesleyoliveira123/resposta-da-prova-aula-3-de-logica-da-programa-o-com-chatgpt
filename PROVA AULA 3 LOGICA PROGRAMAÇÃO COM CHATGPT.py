import random
secret=random.randint(1,10)
palpites=3

while(palpites>0):
    num=int(input("digite um numero de 1 ao 10: "))
    palpites-=1
    if (num>secret):
        print(f"{num} é maior que numero secreto restam {palpites} palpites")
    elif (num<secret):
        print(f"{num} é menor que numero secreto, restam {palpites} palpites")

    else:
        print(f"acertou! {num} é o numero secreto.")
        break
else:
    print(f"acabaram as tentativas! nao desanime e boa sorte da proxima vez!")