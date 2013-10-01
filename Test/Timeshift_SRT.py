#################################
# Timeshift SRT Ver. 1.0
#
# Rodrigo Nobrega
# 24-Feb-2008
#################################


# function timeshift

def timeshift(tempo,s):
	inifim=tempo.rsplit(" --> ")
	listinicio= inifim[0].split(":")
	listfim= inifim[1].split(":")
	
	novoinicio=[listinicio[0],listinicio[1],(str(float(listinicio[2].replace(",","."))+s)).replace(".",",")]
	novofim=[listfim[0],listfim[1],(str(float(listfim[2].replace(",","."))+s)).replace(".",",")]
	
	if float(novoinicio[2].replace(",","."))>=60:
		novoinicio[2]=('00'+str(float(novoinicio[2].replace(",","."))-60).replace(".",","))[-6:]
		novoinicio[1]=('00'+str(int(novoinicio[1])+1))[-2:]
	
	if float(novoinicio[2].replace(",","."))<0:
		novoinicio[2]=('00'+str(60+float(novoinicio[2].replace(",","."))).replace(".",","))[-6:]
		novoinicio[1]=('00'+str(int(novoinicio[1])-1))[-2:]
	
	if int(novoinicio[1])>=60:
		novoinicio[1]=('00'+str(int(novoinicio[1])-60))[-2:]
		novoinicio[0]=('00'+str(int(novoinicio[0])+1))[-2:]

	if float(novofim[2].replace(",","."))>=60:
		novofim[2]=('00'+str(float(novofim[2].replace(",","."))-60).replace(".",","))[-6:]
		novofim[1]=('00'+str(int(novofim[1])+1))[-2:]
	
	if float(novofim[2].replace(",","."))<0:
		novofim[2]=('00'+str(60+float(novofim[2].replace(",","."))).replace(".",","))[-6:]
		novofim[1]=('00'+str(int(novofim[1])-1))[-2:]
	
	if int(novofim[1])>=60:
		novofim[1]=('00'+str(int(novofim[1])-60))[-2:]
		novofim[0]=('00'+str(int(novofim[0])+1))[-2:]
	
	return novoinicio[0]+":"+novoinicio[1]+":"+novoinicio[2]+" --> "+novofim[0]+":"+novofim[1]+":"+novofim[2]






# arquivo de entrada
entnome=raw_input('SRT File (Path\Name) ? ')
a=open(entnome,'r')

# arquivo de saida
sainome=raw_input('New SRT File (Path\Name) ? ')
b=open(sainome,'w')


# shift
shift=float(raw_input('Time to shift (in seconds) ?'))



# loop principal
for linha in a:

	# teste
	if linha.find(" --> ")==-1:
		b.write(linha)
	else:
		b.write(timeshift(linha,shift))
		b.write('\n')



# fecha arquivos
b.close()
a.close()
