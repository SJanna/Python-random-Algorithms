vis= input('Valor inicial: ')
vfs= input('Valor final: ')
vi=int(vis)
vf=int(vfs)
ListaNumCon7=[]
for i in range(vi+1, vf+1):
    istring=str(i)
    if '6' in istring:
        ListaNumCon7.append(i)
print(ListaNumCon7)
print('Hay',len(ListaNumCon7),'números mayores a',vi, ', y menores o iguales a', vf, 'con el dígito 6')
