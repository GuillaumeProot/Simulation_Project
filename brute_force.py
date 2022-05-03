import matplotlib.pyplot as plt

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

def print_tab(tableau):
	compteur = 0
	for elt in tableau:
		print(str(compteur)+" = "+str(elt), ", ", end="")
		compteur += 1

def histogramme(tableau):
	plt.plot(tableau)
	plt.show()


lines = lecture()
tab = create_tab(lines)
#print_tab(tab)
histogramme(tab)