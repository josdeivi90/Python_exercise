def misplit(string2):
    if(string2 == ""):
        return []
    elif(string2.starwith(" ")):
        string2 = string2.strip()
        misplit(string2)
    return(string2.split(" "))

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))