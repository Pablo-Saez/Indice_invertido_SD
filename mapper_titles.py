#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split("\t")

    if len(fields) == 6 and fields[3]=="actor":  # Filtrar solo registros de actores
        nconst = fields[2]
        #print(fields[0])
        movie_id = fields[0]  # Obtener lista de IDs de películas


        print(f"{nconst}\t{movie_id}")
    for x in fields[0]:
        if(x=='n'):
            actor_name = fields[1]
            nconst = fields[0]
            print(f"{nconst}\t{actor_name}")
            break
    