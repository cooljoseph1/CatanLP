from .genome import Genome

def run_tournament(num_players):
    genomes = [Genome() for _ in range(num_players)]
    while len(genomes) > 1:
        for genome1, genome2 in zip(genomes[::2], genomes[1::2]):
            rankings = Genome.compare(genome1, genome2)
            if rankings[0] > rankings[1]:
                genomes.remove(genome2)
            else:
                genomes.remove(genome1)
            print(len(genomes), "players left")
    return genomes[0]
