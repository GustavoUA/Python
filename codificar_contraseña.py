#Generador de contraseñas
#lo convertimos a lista
def convertir(contraseña):
    list=[]
    for i in contraseña:
        list.append(i)

    
#codificamos por posicion
def codificacion(list):
    a = ";o"
    b = "/"
    c = "~ss"
    d = "=dsadas"
    e = "?qwer"
    f = "¿ddg"
    g = "Lbbb"
    h = "Ñbbc"
    i = "{dddg"
    j = "+hgg"
    k = "[khghj"
    l = "Ujkjk"
    m = "Zdf323"
    n = "Ysdsd"
    o = "13232"
    p = "Pddfdf"
    q = "Hdfd"
    r = "hghghy"
    s = "@yu55"
    t = "Vjh"
    u = "hjhh3"
    v = "gj2"
    w = "jkk5"
    x = "jkjk6"
    y = "lñl7"
    z = "9''12"
    
    #creamos una lista
    contraseña_cod=[]
    print(list)
    i = 0
    while i < len(list):
        if(list[i]=="a"):
            contraseña_cod.append(a)
        if(list[i]=="b"):
            contraseña_cod.append(b)
        if(list[i]=="c"):
            contraseña_cod.append(c)
        if(list[i]=="d"):
            contraseña_cod.append(d)
        if(list[i]=="e"):
            contraseña_cod.append(e)
        if(list[i]=="f"):
            contraseña_cod.append(f)
        if(list[i]=="g"):
            contraseña_cod.append(g)
        if(list[i]=="h"):
            contraseña_cod.append(h)
        if(list[i]=="i"):
            contraseña_cod.append(i)
        if(list[i]=="j"):
            contraseña_cod.append(j)
        if(list[i]=="k"):
            contraseña_cod.append(k)
        if(list[i]=="l"):
            contraseña_cod.append(l)
        if(list[i]=="m"):
            contraseña_cod.append(m)
        if(list[i]=="n"):
            contraseña_cod.append(n)
        if(list[i]=="o"):
            contraseña_cod.append(o)
        if(list[i]=="p"):
            contraseña_cod.append(p)
        if(list[i]=="q"):
            contraseña_cod.append(q)
        if(list[i]=="r"):
            contraseña_cod.append(r)
        if(list[i]=="s"):
            contraseña_cod.append(s)
        if(list[i]=="t"):
            contraseña_cod.append(t)
        if(list[i]=="u"):
            contraseña_cod.append(u)
        if(list[i]=="v"):
            contraseña_cod.append(v)
        if(list[i]=="w"):
            contraseña_cod.append(w)
        if(list[i]=="x"):
            contraseña_cod.append(x)
        if(list[i]=="y"):
            contraseña_cod.append(y)
        if(list[i]=="z"):
            contraseña_cod.append(z)
        i+=1
    
    #obtenemos el resultado de la codificacion 
    print("tu contraseña codificada es: ",contraseña_cod)
    
#introducimos por teclado la contraseña
contraseña = input("introduce una contraseña: ")

#Control de longitud y que contenga al menos un carácter especial
if(len(contraseña)!=10):
    print("Introduce una contraseña de 10 digitos")
    if("@" in contraseña):
        print("gracias")
    elif("%" in contraseña):
        print("gracias")
    elif("&" in contraseña):
        print("gracias")
    else:
        print("Error")
else:
    contraseña = contraseña.lower()
    convertir(contraseña)
