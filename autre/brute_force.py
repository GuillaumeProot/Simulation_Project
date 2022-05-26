import matplotlib.pyplot as plt
from itertools import combinations as comb

def lecture():
	file = open('pi.txt', "r")
	lines = file.readlines()
	file.close()
	return lines

def create_tab(lines):
	tableau = [0,0,0,0,0,0,0,0,0,0]
	lines = lines[1:]
	for line in lines:
		for caract in line[:len(line)-1]:
			tableau[int(caract)] += 1
	return tableau

def create_sequence(lines):
	seq = []
	lines = lines[1:]
	for line in lines:
		for caract in line[:len(line)-1]:
			seq.append(int(caract))
	return seq

def print_tab(tableau):
	compteur = 0
	for elt in tableau:
		print(str(compteur)+" = "+str(elt), ", ", end="")
		compteur += 1

def histogramme(tableau):
	plt.plot(tableau)
	plt.show()


 
def statistic(ab, a):
    sumab, suma = sum(ab), sum(a)
    return ( suma / len(a) -
             (sumab -suma) / (len(ab) - len(a)) )
 
def permutationTest(a, b):
    ab = a + b
    Tobs = statistic(ab, a)
    under = 0
    for count, perm in enumerate(comb(ab, len(a)), 1):
        if statistic(ab, perm) <= Tobs:
            under += 1
    return under * 100. / count


lines = lecture()
#tab = create_tab(lines)
seq = create_sequence(lines)
treatmentGroup = seq[:len(seq)//2]
controlGroup   = seq[len(seq)//2:]
under = permutationTest(treatmentGroup, controlGroup)
print("under=%.2f%%, over=%.2f%%" % (under, 100. - under))




#print_tab(tab)
#histogramme(tab)