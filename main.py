import sys
from Moon.Astro import Base
import dis
import time

if __name__ == '__main__':
    base = Base()
    number_of_astronauts = sys.argv[1]  # reading first two args from command line
    number_of_pairs = sys.argv[2]
    for x in range(int(number_of_pairs)):  # reading specified number of pairs and inserting them to countries list
        pair_string = input()
        pair = pair_string.split(' ')
        pair[0] = int(pair[0])
        pair[1] = int(pair[1])
        base.insert_countryman(pair)

    start = time.time()
    combos = base.get_number_of_possible_combinations()
    print("Broj kombinacija: " + str(combos))
    print("Vreme izvrsavanja: " + str(time.time() - start))
    # print(dis.dis(base.get_number_of_possible_combinations))
