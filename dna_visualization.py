import random
import sys
import time


class DNAVisualization:
    def __init__(self):
        self.PAUSE = 0.15
        self.ROWS = [
            '         ##',
            '        #{}-{}#',
            '       #{}---{}#',
            '      #{}-----{}#',
            '     #{}------{}#',
            '    #{}------{}#',
            '    #{}-----{}#',
            '     #{}---{}#',
            '     #{}-{}#',
            '      ##',
            '     #{}-{}#',
            '     #{}---{}#',
            '    #{}-----{}#',
            '    #{}------{}#',
            '     #{}------{}#',
            '      #{}-----{}#',
            '       #{}---{}#',
            '        #{}-{}#'
        ]
        self.index = 0

    def run(self):
        print('DNA Visualization/Animation')
        print('Press Ctrl-C to quit...')
        time.sleep(2)

        try:
            while True:
                self.update_index()
                self.display_row()
                time.sleep(self.PAUSE)
        except KeyboardInterrupt:
            sys.exit()

    def update_index(self):
        self.index = (self.index + 1) % len(self.ROWS)

    def display_row(self):
        nucleotides = self.get_random_nucleotides(
        ) if self.index != 0 and self.index != 9 else (' ', ' ')
        row = self.ROWS[self.index].format(*nucleotides)
        print(row)

    def get_random_nucleotides(self):
        random_selection = random.randint(1, 4)
        nucleotide_pairs = [('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')]
        return nucleotide_pairs[random_selection - 1]


if __name__ == '__main__':
    dna_visualization = DNAVisualization()
    dna_visualization.run()
