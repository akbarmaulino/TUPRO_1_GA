import math
from random import randrange, uniform

class gen1:
    def __init__(self, nilaikromosom, nilaiFitnes, nilaixy):
        self.kromosom = nilaikromosom
        self.fitnes = nilaiFitnes
        self.nilai = nilaixy  

class gen2:
    def __init__(self, nilaikromosom, nilaiFitnes, nilaixy):
        self.kromosom = nilaikromosom
        self.fitnes = nilaiFitnes
        self.nilai = nilaixy  

def nilaiXY(kromosom):
    objek = []
    total_gen = 0
    rumus = 0
    tengah = len(kromosom)//2
    for i in range(tengah):
        rumus = rumus + 9*(10**-(i+1))
        total_gen = total_gen + (kromosom[i]*10**-(i+1))
    x = -1 + (3/rumus) * total_gen
    objek.append(x)

    total_gen = 0
    rumus = 0   
    for i in range(tengah, len(kromosom)):
      rumus = rumus + 9*(10**-(i+1))
      total_gen = total_gen + (kromosom[i]*10**-(i+1))
    y = -1 + (2/rumus) * total_gen
    objek.append(y)
    return objek

def functionKromosom(pjg_kromosom):
  kromosom = []
  for i in range(pjg_kromosom):
    kromosom.append(randrange(0,10))
  return kromosom

def functionFitnes(objek):
    fitnes = ((math.cos(objek[0])**2)*((math.sin(objek[1])**2)))+(objek[0]+objek[1])
    return fitnes


def ukuranPopulasi(pjg_populasi, pjg_kromosom):
  populasi = []
  for i in range(pjg_populasi):
    kromosom = functionKromosom(pjg_kromosom)
    objek = nilaiXY(kromosom)
    fitnes = functionFitnes(objek)
    populasi.append(gen1(kromosom,fitnes,objek))
  return populasi

def sorting(populasi):
    for i in range(len(populasi)):
        min_index = i
        for j in range(i+1, len(populasi)):
            if populasi[j].fitnes > populasi[min_index].fitnes:
                min_index = j
        populasi[i], populasi[min_index] = populasi[min_index], populasi[i]

def selectParent(populasi):
    popBaru = []
    for i in range(6):
        kromosom = populasi[i].kromosom.copy()
        fitnes = populasi[i].fitnes
        nilai = populasi[i].nilai.copy()
        popBaru.append(gen2(kromosom, fitnes, nilai))
    return popBaru

def crossover(popBaru):
    pc = 0.03
    if pc < (uniform(0,1)):
      i = 0
      while i<len(popBaru) - 1:
          for j in range(2):
              temp = popBaru[i].kromosom[j]
              popBaru[i].kromosom[j] = popBaru[i+1].kromosom[j]
              popBaru[i+1].kromosom[j] = temp
          popBaru[i].nilai =nilaiXY(popBaru[i].kromosom)
          popBaru[i].fitnes = functionFitnes(popBaru[i].nilai)
          popBaru[i+1].nilai =nilaiXY(popBaru[i+1].kromosom)
          popBaru[i+1].fitnes = functionFitnes(popBaru[i+1].nilai)
          i = i+2 

def mutasi(popBaru, pjg_kromosom):
    pm = 0.1
    if pm < (uniform(0,1)):
        for i in range(6) :
          j = randrange(0,len(popBaru))
          popBaru[j].kromosom[randrange(0, pjg_kromosom)] = randrange(0,10)
          popBaru[j].nilai =nilaiXY(popBaru[j].kromosom)
          popBaru[j].fitnes = functionFitnes(popBaru[j].nilai)

def steadyState(populasi, popBaru):
    akhir = len(populasi)-1
    for i in range(len(popBaru)):
      populasi[akhir] = popBaru[i]
      akhir -= 1
    sorting(populasi)

pjg_populasi = 100
pjg_kromosom = input("Masukan Panjang Kromosom : ")
pjg_kromosom = int(pjg_kromosom)
populasi = ukuranPopulasi(pjg_populasi, pjg_kromosom)
sorting(populasi)
z = 1
while z <= 200 and (populasi[0].nilai[0] != 2.0 or populasi[0].nilai[1] != 1.0):
    popBaru = selectParent(populasi)
    crossover(popBaru)
    mutasi(popBaru, pjg_kromosom)
    steadyState(populasi, popBaru)
    print("Generasi ke - ", z)
    print("Kromosom Terbaik : ", populasi[0].kromosom)
    print("Nilai terbaik : ", populasi[0].nilai)
    print("Nilai Fitnes : ", populasi[0].fitnes)
    z = z+1