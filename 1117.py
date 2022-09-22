nota = 0
x=0
media=0
while nota!=2:
    x = float(input())
    if x>=0 and x<=10:
        media+=x/2
        nota+=1
    else:
        print('nota invalida')

print('media = %.2f'%(media))