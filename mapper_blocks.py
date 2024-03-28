#!/usr/bin/env python

import sys

# Mapper pour trouver le nombre de fois que chaque tag a été utilisé pour taguer un film
def mapper_blocks():
    for line in sys.stdin:
        try:
            # Splitter la ligne en userID, movieID, tagID, timestamp
            userID, movieID, tagID, timestamp = line.strip().split(',')
            # Émettre la clé 'tagID' avec valeur 1 pour chaque tag
            yield tagID, 1
        except Exception:
            pass

if __name__ == "__main__":
    mapper_blocks()
