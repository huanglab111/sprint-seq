f=open('./mapped_genes.csv','w')
for i in range(20):
    f2=open('./mapped_genes_'+str(i)+'.csv','r')
    for line in f2:
        f.write(line)
    f2.close()
f.close()