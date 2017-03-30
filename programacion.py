print( "PRIMER PUNTO" ) 
radio =(int(input ("ingrese el valor para radio " ))) 
altura=(int(input ("ingrese el valor para altura " )))
pi= 3.1416
volumen =pi*radio**2*altura
print(volumen)
#----------------------------------------------------
print("SEGUNDO PUNTO ")


cm3=(int(input ("ingrese el valor para metros cubicos" )))
litros= cm3*0.001
print(litros) 
#-----------------------------------------------------
print("TERCER PUNTO ")

#los tiepos que usted puede ingresar son: 
#LL=lluvia T= tormenta S=soleado N=nublado

presente = input("ingrese el tiempo que hace hoy ")
futuro = " t "
if presente == "ll" or presente =="t":
    print(" lleve sombrilla")
elif presente=="s" or presente=="n" :
    print( "no lleve sombrilla")
#----------------------------------------------------------
print("CUARTO PUNTO ")
e =(int(input("ingrese la edad")))
pt = input("tiene problemas estuculares")
su = input("estudia") 
g = input("indique su genero")
n = input ("Es Colombiano")

if e>= 18:
    if pt ==('no'):
        if su =="si":
            if g ==" hombre":
                if n== "si":
                    print("presta servicio militar")
else:
    print("no presenta servicio militar")
            #se hace con elif anidados 