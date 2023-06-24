#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys
i = 0
movies_dict = {}  # Diccionario para almacenar el primer output: id del actor y id de la película
actors_dict = {}  # Diccionario para almacenar el segundo output: id del actor y nombre del actor

for line in sys.stdin:
    line = line.strip()
    fields = line.split("\t")

    if len(fields) == 2:  # Primer output: id del actor y id de la película
        if fields[1][0]=='t':
            
            actor_id, movie_id = fields
            if actor_id not in movies_dict:
                movies_dict[actor_id] = []
            movies_dict[actor_id].append(movie_id)
                
        else:  # Segundo output: id del actor y nombre del actor
            
            i = i+1
            actor_id, actor_name = fields[0], fields[1]
            actors_dict[actor_id] = actor_name

# # Recorrer el diccionario de películas y mostrar el nombre del actor asociado a cada película
for actor_id, movie_ids in movies_dict.items():
    actor_name = actors_dict.get(actor_id)
    
    if actor_name != None:

        movies = ','.join(movie_ids)
        print(f"{actor_name}\t{movies}")
    else:
        continue
# for clave, valor in movies_dict.items():
#     print(clave, valor)

# print("------")

# for clave, valor in actors_dict.items():
#     print(clave, valor)