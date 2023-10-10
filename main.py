song = """The itsy bitsy spider climbed up the water spout
Down came the rain and washed the spider out
Out came the sun and dried up all the rain
And the itsy bitsy spider climbed up the spout again"""
def generate_token(song):

#Obtener el hash de la cancion
    hash = 0
    for char in song:
        hash += ord(char)

#Generar el token a partir del hash obtenido
    token = ""
    while hash > 0:
        token += chr(hash % 256)
        hash //= 256

    return token
bitsy_token = generate_token(song)    
print(bitsy_token)
