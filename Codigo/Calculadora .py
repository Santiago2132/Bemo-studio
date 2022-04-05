#Funciones 
def suma (a,b):
    result=a+b
    print("La suma de ",a," y ",b," es: ",result)
def resta (a,b):
    result=a-b
    print("La resta de ",a," y ",b," es: ",result)
def multiplicación (a,b):
    result=a*b
    print("La multipliación de ",a," y ",b," es: ",result)
def division(a,b):
    result=a/b
    print("La division de ",a," y ",b," es: ",result)

"""("Bienvenido :D \n╔═══╗ ♪\n║███║ ♫\n║ (●) ♫\n╚═══╝♪♪")"""
#Programa 
print("Bienvenido :D \n╔═══╗\n║███║\n║ 1 ║\n╚═══╝")
while True:
    print("Opciones \n1)Suma de dos numeros \n2)Resta de dos numeros \n3)Multipliación de dos numeros \n4)División de dos numeros \n(Cualquier otro numero o letra para apagar)")
    option=int(input("Ingrese la opción: "))
    if(option==1):
        num1=int(input("Ingrese un número: "))
        num2=int(input("Ingrese otro numero: "))
        suma(num1,num2)
    elif(option==2):
        num1=int(input("Ingrese un número: "))
        num2=int(input("Ingrese otro numero: "))
        resta(num1,num2)
    elif(option==3):
        num1=int(input("Ingrese un número: "))
        num2=int(input("Ingrese otro numero: "))
        multiplicación(num1,num2)
    elif(option==4):
        num1=int(input("Ingrese un número: "))
        num2=int(input("Ingrese el número popr el cual se va a dividir: "))
        division(num1,num2)
    else:
        print("Good bye")
        break