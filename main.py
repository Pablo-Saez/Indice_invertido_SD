import pandas as pd

def build_inverted_index(name_basics_file, title_principals_file):
    inverted_index = {}
    
    # Construir el índice invertido a partir de la tabla name.basics.tsv
    print("entro \n")
    name_basics_df = pd.read_csv(name_basics_file, delimiter='\t', nrows=1000)
    for _, row in name_basics_df.iterrows():
        primary_name = row['primaryName']
        known_for_titles = row['knownForTitles'].split(',') if row['knownForTitles'] != '\\N' else []
        
        for known_for_title in known_for_titles:
            if primary_name not in inverted_index:
                inverted_index[primary_name] = []
            inverted_index[primary_name].append(known_for_title)
    
    # Actualizar el índice invertido con información de la tabla title.principals.tsv
    # print("primera salida")
    # title_principals_df = pd.read_csv(title_principals_file, delimiter='\t', nrows=100)
    # for _, row in title_principals_df.iterrows():
    #     nconst = row['nconst']
    #     primary_name = row['primaryName']
    #     tconst = row['tconst']
        
    #     if primary_name in inverted_index:
    #         inverted_index[primary_name].append(tconst)
    
    return inverted_index



# Ejemplo de uso
name_basics_file = 'dataset/name.basics.tsv'
title_principals_file = 'dataset/title.principals.tsv'

index = build_inverted_index(name_basics_file, title_principals_file)

# Función de búsqueda
def search_name(name):
    if name in index:
        return index[name]
    else:
        return []

# Ejemplo de búsqueda
flag = 0

while flag==0:
    opcion = str(input('Ingrese nombre a buscar: '))
    if(opcion == 0):
        flag=1
    movies_participated = search_name(opcion)
    print(f"Las películas en las que {opcion} ha participado son:")
    for movie in movies_participated:
        print(movie)
    




#print(index)
