#Funciones
def fibonacci(n):
    a=0
    f=0
    b=1
    
    i=1
    while(i<n):
        f=a+b
        a=b
        b=f
    print("El número ",a," en fibonacci: ",f)

def fibonaccis(n):
    a=0
    f=0
    b=1
    i=1
    while(i<n):
        f=a+b
        a=b
        b=f
        print(f)

def collatz(a):
    if((a*2)/100==0):
        result=a/2
        print("La secuencia de collatz de ",a,"es: ",result)
    else:
        result=(a*3)+1
        print("La secuencia de collatz de ",a,"es: ",result)   

#Parte del programa
print("Bienvenid@ \n1)Numero Fibonacci \n2)Serie Fibonacci \n3)Serie de Collatz ")
option=0
while True:
    option=0
    while ((option<=0)|(option>3)):
        option=int(input("\nQue opción desea calcular: "))
        if(option==1):
            num=int(input("Ingrese el numero a calcular su Fibonacci: "))
            resultado = fibonacci(num)
        elif(option==2):
            num=int(input("Ingrese el numero a calcular su Fibonacci: "))
            resultado= fibonaccis(num)
        elif(option==3):
            num=int(input("Ingrese el numero a calcular su Fibonacci: "))
            resultado=collatz(num)