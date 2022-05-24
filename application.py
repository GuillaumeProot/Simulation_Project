from matplotlib import pyplot as plt
import numpy as np
import os
import atexit
from generators import *
from kolmogorov_smirnov import kolmogorov_smirnov_uniform_test
from poker import get_pi_seq, poker_test
from gap import gap_test

def open_file():
    with open("pi.txt", "r") as pi:
        for line in pi:
            line = line.strip()
            if "." in line:
                line = line.split(".")[1]
            for c in line:
                yield int(c)
def cls():

    """ 
    fonction de nettoyage d ecran
    """

    os.system('cls' if os.name =='nt' else 'clear')

def main():
    pi_numbers = np.array(list(open_file()))
    print(f"Etude du caractère pseudo-aléatoire des décimales de pi par des tests vus au cours \n")
    choix = int(input("Choisissez l'action: \n"
                      "1. Information sur pi \n"
                      "2. Tests sur les décimales de pi \n"
                      "3. Tests sur les générateurs \n"
                      "4. Quitter \n"))

    #############################################################################################################
    #############################################################################################################

    if choix == 1:
        cls()
        print(f"pi = {pi_numbers[:1000000]} \n")
        pi_labels, pi_counts = np.unique(pi_numbers, return_counts=True)
        print(f"Les chiffres apparaissant dans les décimales :\n"
              f"{pi_labels}\n")
        print(f"Leur fréquences d\'apparition : \n"
              f"{pi_counts}")
        plt.figure()
        plt.bar(pi_labels, pi_counts, color='palegreen')
        plt.savefig('histo_exp.png')
        plt.show()
        print("\n \n \n \n \n")
        main()

    #############################################################################################################
    #############################################################################################################

    elif choix == 2:
        cls()
        choix_test = int(input("Choisissez le test: \n"
                               "1. Test de Poker sur Pi \n"
                               "2. Test de Gap sur Pi \n"
                               "3. Retour \n"))

        if choix_test == 1 :

            k = int(input("Entrez le nombre de paquets : "))
            poker_test(10, k)
            print("\n \n \n \n \n")
            main()
        elif choix_test == 2:
            a = float(input("Choisissez un a dans [0;1[ : "))
            b = float(input("Choisissez un b dans [0;1[ : "))
            gap_test(get_pi_seq(), a, b, True)
            main()
        else:
            cls()
            main()

    #############################################################################################################
    #############################################################################################################

    elif choix == 3:
        cls()
        pyth_numbers = []
        for _ in range(2000):
            pyth_numbers.append(random.uniform(0, 1))

        randomgen1 = Generator1(50)
        gen_numbers_1 = [randomgen1.random() for _ in range(2000)]

        print(gen_numbers_1)
        print("---------------------------------------")

        randomgen2 = Generator2()
        gen_numbers_2 = [randomgen2.random() for _ in range(2000)]

        print(gen_numbers_2)
        print("---------------------------------------")

        randomgen3 = Generator3()
        gen_numbers_3 = [randomgen3.random() for _ in range(2000)]

        print(gen_numbers_3)
        print("---------------------------------------")

        choix_test = int(input("Choisissez le test: \n"
                               "1. Test de kolmogorov-smirnov uniforme sur les générateurs \n"
                               "2. Test du Gap sur les générateurs \n"
                               "3. Retour \n"))
        if choix_test == 1:
            print(f"Test de Kolmogorov-Smirnov pour notre générateur : \n"
                  f"1er generateur --> {kolmogorov_smirnov_uniform_test(gen_numbers_1)} \n"
                  f"2ieme generateur --> {kolmogorov_smirnov_uniform_test(gen_numbers_2)} \n"
                  f"3ieme generateur --> {kolmogorov_smirnov_uniform_test(gen_numbers_3)} \n"
                  f"Python --> {kolmogorov_smirnov_uniform_test(pyth_numbers)}")

            plt.figure()
            plt.hist(gen_numbers_1, color='palegreen', histtype='barstacked')
            plt.hist(pyth_numbers, color='darkblue', histtype='step')
            plt.legend({'Premier générateur', 'Python'}, loc=4)
            plt.savefig('generator1.png')
            plt.show()

            plt.figure()
            plt.hist(gen_numbers_2, color='tomato', histtype='barstacked')
            plt.hist(pyth_numbers, color='darkblue', histtype='step')
            plt.legend({'deuxième générateur', 'Python'}, loc=4)
            plt.savefig('generator2.png')
            plt.show()

            plt.figure()
            plt.hist(gen_numbers_3, color='gold', histtype='barstacked')
            plt.hist(pyth_numbers, color='darkblue', histtype='step')
            plt.legend({'Troisième générateur', 'Python'}, loc=4)
            plt.savefig('generator3.png')
            plt.show()
            print("\n \n \n \n \n")
            main()

        elif choix_test == 2:
            pass
        elif choix_test == 3:
            cls()
            main()
    #############################################################################################################
    #############################################################################################################
    else:
        cls()
        print("###############################################")
        print("###############################################")
        print("##### #####  #####  ####   ####   #    #  #####")
        print("#     #   #  #   #  #   #  #   #   #  #   #    ")
        print("#  ## #   #  #   #  #   #  ####     ##    #####")
        print("#  #  #   #  #   #  #   #  #   #    ##    #    ")
        print("####  #####  #####  ####   ####     ##    #####")
        print("###############################################")
        print("###############################################")
        print("\n \n \n \n")
        quit()

if __name__ == '__main__':
    os.system('cls' if os.name =='nt' else 'clear')
    print("##################################")
    print("##################################")
    print("#    #  #####  #      #      #####")
    print("#    #  #      #      #      #   #")
    print("######  #####  #      #      #   #")
    print("#    #  #      #      #      #   #")
    print("#    #  #####  #####  #####  #####")
    print("##################################")
    print("##################################")
    main()
