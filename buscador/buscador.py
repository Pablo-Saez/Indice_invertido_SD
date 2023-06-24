import psycopg2

# Datos de conexión a la base de datos
conexion_info = {
    'host': 'localhost',
    'port': 5432,
    'database': 'peliculas_hadoop',
    'user': 'postgres',
    'password': 'contraseña'
}

def buscar_actores():
    # Establecer la conexión a la base de datos PostgreSQL
    conexion = psycopg2.connect(**conexion_info)

    while True:
        # Solicitar al usuario el nombre del actor a buscar
        nombre_actor = input("Ingrese el nombre del actor (o 'salir' para salir): ")

        if nombre_actor.lower() == 'salir':
            break

        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Realizar la consulta a la tabla actores por los IDs del nombre del actor
        consulta = "SELECT nombre_actor, peliculas FROM actores WHERE nombre_actor = %s"
        cursor.execute(consulta, (nombre_actor,))

        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()

        if len(resultados) > 0:
            print("Resultados:")
            for resultado in resultados:
                nombre_actor, peliculas = resultado
                print(f"{nombre_actor}\t{peliculas}")
        else:
            print(f"No se encontraron resultados para el actor {nombre_actor}.")

        # Cerrar el cursor
        cursor.close()

    # Cerrar la conexión a la base de datos
    conexion.close()

# Ejecutar la función de búsqueda de actores
buscar_actores()
