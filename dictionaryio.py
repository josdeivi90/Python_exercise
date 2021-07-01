dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

#diccionario['llave'] = "valor"

print(dict)
print(numerosTelefono['jefe'])
print(diccionarioVacio)
# pregunto llave
#KEY #pregunta por llaves
for key in dict.keys():
    print(key, "-> keys ->", dict[key])
    print(len(dict))

#VALUES
for french in dict.values():
    print("values ->",french)

#ITEMS 
for spanish, french in dict.items():
    print(spanish, "-> items ->", french)

#UPDATE para agregar llaves y valores
x = "el triplehptaproblema"
dict.update({"pato" : x})
print(dict)
#popitem elimina el ultimo item
dict.popitem()
