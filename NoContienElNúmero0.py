vis= input('Valor inicial: ')
vfs= input('Valor final: ')
vi=int(vis)
vf=int(vfs)
ListaNumCon7=[]
for i in range(vi, vf+1):
    istring=str(i)
    if '0' in istring:
        pass
    else:
        ListaNumCon7.append(i)
print(ListaNumCon7)
print('Hay',len(ListaNumCon7),'números SIN el dígito 0')
