#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys

current_actor = None
movies = set()

for line in sys.stdin:
    print("linea: "+ line)
    line = line.strip()
    actor_name, movie_id = line.split("\t")

    if current_actor is None:
        current_actor = actor_name

    if actor_name != current_actor:
        # Imprimir el resultado del actor anterior
        print(f"{current_actor}\t{','.join(movies)}")

        # Reiniciar variables para el nuevo actor
        current_actor = actor_name
        movies = set()

    movies.add(movie_id)

# Imprimir el resultado del último actor
if current_actor is not None:
    print(f"{current_actor}\t{','.join(movies)}")