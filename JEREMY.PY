import os
class ficha :
    def init(self):
        pass

    def menu(self,opciones):
        
        print("-MENU DE FICHA- ")
        for opcion in opciones:
            print(opcion)

        opc=input("digite el numero de ficha [1...{}]: ".format(len(opciones)))
        return opc

help=ficha()
Lista=["1. Pila","2. Cola","3. Lista","4. Salir"]

opcion =" "

while opcion != "4":
    
    os.system("cls")
    
    if opcion=="1":
        class Menu :
            def init(self):
                pass
        
            def menu(self,opciones):
                

                print("-menu de pila-  ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite el numero de ficha [1...{}]: ".format(len(opciones)))
                return opc
                
            milis=[]
                # for x in milis:
                # milis_edd = print(milis)
            print("-menu pilas-  ")
            print("elementos requeridos: ")
            cant=int(input())
            os.system("cls")
            i=0
            if cant <8:
                    print("su lista es vacia")
                    
            while i<cant:
                        print("Ingresar")
                        nom=input()
                        milis.append(nom)
                        i+=1
                        
                        print("su pila esta vacia")
                        # lista2=["si","no"]
                        # lista2=input("desea agg otro nombre si o no : ")


                        # if lista2 == "si":
                        #     nom2=input("agg otro nombre : ")
                        #     milis.append(nom2)

                        #     print(f"el segundo nombre que se agg fue {nom2}")

                        # else:
                        #     print("ok")
                        
                        
                        os.system("cls")
                        print(milis)
                    
            else:
                    print("su lista esta llena")

            print("lista: ",milis)

            na=milis.pop(-1)
            print("El elemento en salir: ",na)

            print(milis)

        print("--------------------------------------------------------- ")
        print()
        
    elif opcion=="2":
        class ficha :
            def init(self):
                pass
        
            def menu(self,opciones):
                
                print("-menu cola-  ")
                for opcion in opciones:
                    print(opcion)

                opc=input("Digitar el numero de ficha [1...{}]: ".format(len(opciones)))
                return opc             
            milis=[]
                # for x in milis:
                # milis_edd = print(milis)
            print("-menu cola- ")
            print("elementos deseados?: ")
            cant=int(input())
            os.system("cls")
            i=0
            if cant <8:
                    print("su lista esta vacia")
                    
            while i<cant:
                        print("Ingrese")
                        nom=input()
                        milis.append(nom)
                        i+=1
                        
                        print("su pila esta vacia")
                                    
                        os.system("cls")
                        print(milis)
                    
            else:
                 print("su lista esta llena")

            print("su lista es",milis)

            na=milis.pop(0)
            print("El elementos por presentar es: ",na)
            
            print(milis)

        print("---------------------------------------------------------   ")
        print()
    elif opcion=="3":
        class ficha :
            def init(self):
                pass

            def menu(self,opciones):
            
                print("-menu lista-  ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite el numero de ficha [1...{}]: ".format(len(opciones)))
                return opc                 
            milis=[]
                # for x in milis:
                # milis_edd = print(milis)
            print("-menu lista-  ")
            print("elementos deseados?: ")
            cant=int(input())
            os.system("cls")
            i=0
            if cant <8:
                    print("su lista esta vacia")
                
            while i<cant:
                        print("Ingresar")
                        nom=input()
                        milis.append(nom)
                        i+=1
                        
                        print("su lista esta vacia")
                        os.system("cls")
                        print(milis)
                    
            else:
                    print("su lista esta llena")

            sacar=input("elemento que desee presentar : ")
                    
            os.system("cls")
            for x in range(len(milis)-1,-1,-1):
                        if milis[x]== sacar:
                            print(milis.pop(x))
            print(milis)

            sa=input("en que posicion desee que este su elemento : ")
            
            print("Posicion : ",milis.index(sa))
    else:
            print()
    opcion=help.menu(Lista)
print("GRACIAS VUELVA PRONTO MUAK")