#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split("\t")

    if len(fields) == 6 :  # Filtrar solo registros de actores
        actor_name = fields[1]
        movie_ids = fields[5].split(",")  # Obtener lista de IDs de películas

        for movie_id in movie_ids:  
            print(f"{actor_name}\t{movie_id}")