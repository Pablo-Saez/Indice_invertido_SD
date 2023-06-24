import psycopg2

# Establecer la conexión a la base de datos PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    database="peliculas_hadoop",
    user="postgres",
    password="contraseña"
)

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Nombre del archivo de entrada
archivo_entrada = "../output/part-00000"

# Abrir el archivo y leer los datos
with open(archivo_entrada, "r") as archivo:
    for linea in archivo:
        # Dividir la línea en nombre del actor e IDs de las películas
        actor, peliculas = linea.strip().split("\t")
        
        # Insertar los datos en la base de datos
        consulta = "INSERT INTO actores (nombre_actor, peliculas) VALUES (%s, %s)"
        cursor.execute(consulta, (actor, peliculas))

# Confirmar los cambios y cerrar la conexión
conexion.commit()
cursor.close()
conexion.close()
