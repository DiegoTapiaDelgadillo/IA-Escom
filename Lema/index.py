import stanza

# Descargar el modelo de idioma (stanza.download('es'))
#stanza.download('es')

# Inicializar el procesador de texto de Stanza para español
nlp = stanza.Pipeline('es', processors='tokenize,lemma')

# Nombre del archivo de entrada y salida
nombre_archivo_entrada = 'nota.txt'
nombre_archivo_salida = 'lema.txt'

# Inicializar un arreglo para almacenar las palabras del archivo de entrada
palabras = []

# Abrir el archivo de entrada en modo lectura
with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo_entrada:
    # Leer el contenido del archivo línea por línea
    for linea in archivo_entrada:
        # Dividir cada línea en palabras usando el espacio como separador
        palabras_linea = linea.split()
        # Guardar en el arreglo 'palabras' con las palabras de la línea actual
        palabras.extend(palabras_linea)

# Inicializar una lista para almacenar los lemas
lemas = []

# Procesar cada palabra para obtener su lema y guardar los lemas en un arreglo
for palabra in palabras:
    doc = nlp(palabra)
    lema = [word.lemma for sent in doc.sentences for word in sent.words]
    lemas.append(' '.join(lema))

# Escribir los lemas en el archivo de salida
with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
    #Escribe en el archivo "archivo_salida" las palabras lematizadas
    for palabraLemas in lemas:
        archivo_salida.write('Lema: ' + palabraLemas + '\n')

#Imprime en que ruta se guardo el archivo de salida    
print(f"Lemas guardados en '{nombre_archivo_salida}'.")
