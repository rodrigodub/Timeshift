# function timeshift

def timeshift(tempo,s):
	inifim=tempo.rsplit(" --> ")
	listinicio= inifim[0].split(":")
	listfim= inifim[1].split(":")
	
	novoinicio=[listinicio[0],listinicio[1]
		,(str(float(listinicio[2].replace(",","."))+s)).replace(".",",")]
	novofim=[listfim[0],listfim[1]
		,(str(float(listfim[2].replace(",","."))+s)).replace(".",",")]
	
	print novoinicio[0]+":"+novoinicio[1]+":"+novoinicio[2]
		+" --> "
		+novofim[0]+":"+novofim[1]+":"+novofim[2]
