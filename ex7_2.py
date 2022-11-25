fname = input("Enter file name: ")
fh = open(fname)
count=0
Preprom=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
         continue
    findline=line.find(':')
    flinea=line[findline+1:]
    number=float(flinea)
    count=count+1
    Preprom=number+Preprom
print('Average spam confidence:',(Preprom/count))
