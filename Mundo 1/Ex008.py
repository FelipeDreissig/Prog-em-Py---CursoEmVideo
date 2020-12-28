### convertendo valores
met = float(input('Quantos metros você quer converter?'))

km = met*(1/1000)
hec = met*(1/100)
deca = met*(1/10)
met = met
dec = met*10
cent = met*100
mili = met*1000

print('Os {} metros são {} milímetros, {} centímetros,'
      '\n {} decímetros, {} decâmetros, {} hetômetros e {} kilometros '.format(met, mili, cent, dec, deca, hec, km))