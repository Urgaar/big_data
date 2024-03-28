#!/usr/bin/env python

import sys

# Mapper pour trouver le nombre de tags par film et par utilisateur
def mapper_default_config():
    for line in sys.stdin:
        try:
            # Splitter la ligne en userID, movieID, tagID, timestamp
            userID, movieID, tagID, timestamp = line.strip().split(',')
            # Émettre la clé 'movieID' avec valeur 1 pour chaque tag
            yield movieID, 1
            # Émettre la clé 'userID' avec valeur 1 pour chaque utilisateur
            yield userID, 1
        except Exception:
            pass

if __name__ == "__main__":
    mapper_default_config()
