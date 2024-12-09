#diccionario = {"c1":"hola","c2":"mucho gusto"}
#resultado = diccionario["c1"]
#print(resultado)

#diccionario = {"c1":"juan", "c2" :[1,2,3],"c3":{"s1":100,"s2":500}}
#print(diccionario.keys())
#print(diccionario.values())
#print(diccionario.items())

#mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
#print(mi_dict["puntos"]["points2"][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic.update({
    "edad": 36,
    "ocupacion": "Editora",
    "pais": "Colombia"
})
print(mi_dic)