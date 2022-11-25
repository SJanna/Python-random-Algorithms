#Mostrará la palabra que más se repite y cuántas veces lo hace usando
#el método .items(). (Two iteration variables)

handle=open('romeo.txt')

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word] = counts.get(word,0) +1

bigcount=None
bogword=None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
