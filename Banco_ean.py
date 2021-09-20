titular=['Aldemar Cordoba', 'Brayan Torres']
usuario=   ['Aldemar'  , 'Brayan' ]
contraseña=    [2678       , 4343 ] 
numero_de_cuenta= [ 6578 , 4567 ]
account_tipo=  [ 'corriente', 'ahorros' ] 
dinero=[ '100 USD' , '3000 USD' ]
correo= ['aldemar@gmail.com'  , 'brayan@gmail.com']   
account=    ['cerrada' , 'cerrada' ] 
#EL USUARIO DE ADMINISTRADOR ES: ADMIN---COSNTRSEÑA:1234

while(True): 
    sesion = False
    sesion_administrador = False
    while(sesion==False and sesion_administrador==False):
        
        print("Eliga el numero del proceso que desee:")
        print("\n")
        print("1. Iniciar sesion")
        print("2. ¿Olvidaste la contraseña?")
        print("3. Iniciar como administrador(Administrar cuentas)")
    
        while(True):
            try:
                opcion=int(input())
                break
            except Exception as error:
                print("Debes digitar una opción valida")
                
        if opcion == 1:
            print("\n")
            print("Iniciar sesion")
            print("Ingrese su usuario: ")
            user=input()
            while(True):
                try:
                    password=int(input("Ingrese contraseña:"))
                    if password<0:
                        raise
                    break
                except Exception as error:
                    print("Debes digitar un numero entero")
            if user in usuario:
                indice=usuario.index(user)
                if contraseña[indice] == int(password):
                    account[indice] ='activa'
                    print("Usuario logueado")
                    sesion=True
                else:
                    print("contraseña invalida")
            else:
                print("El usuario no existe")
        elif opcion == 2:
            print("\n")
            print("RECUPERACIÓN DE CONTRASEÑA")
            print("Ingrese usuario:")
            user=input()
            if user in usuario:   
                print("¿Cual es su correo elctronico?")
                print("Ingrese su correo:")
                gmail=input()
                indice=usuario.index(user)
                if correo[indice] == gmail:
                    print("La contraseña debe ser numérica")
                    while(True):
                        try:
                            contraseña_1=int(input("Digite su nueva contraseña:"))
                            if contraseña_1<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero correcto")
                    while(True):
                        try:
                            contraseña_2=int(input("Digite la nueva contraseña otra vez:"))
                            if contraseña_2<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero correcto")
                    if contraseña_1 == contraseña_2:
                        contraseña[indice] = contraseña_1
                        print("Contraseña recuperada correctamente, puede iniciar sesión con su nueva contraseña.")
                    else:
                        print("Las contraseñas no coinciden, debe realizar el proceso de nuevamente.")
                else:
                    print("Respuesta incorrecta")
                
            else:
                print("El usuario ingresado no está en nuestra base de datos")
        elif opcion == 3:
            print("\n")
            print("INICIO DE SESIÓN ADMINISTRADOR DEL BANCO")
            print("Ingrese usuario:")
            user=str(input())
            if user == "admin":
                while(True):
                    try:
                        password=int(input("Ingrese contraseña:"))
                        if password<0:
                            raise
                        break
                    except Exception as error:
                        print("Debes digitar la contraseña correcta")
                    
                if  int(password) == 12345:
                    print("\n")
                    print("Bienvenido Administrador")
                    sesion_administrador=True
                else:
                    print("contraseña de usuario administrador es invalida")
            else:
                print("usuario administrador no existe")
        else:
            print("opcion invalida")
           
            
    if sesion==True:
        indice=usuario.index(user)
        print("\n")
        print("Bienvenido",titular[indice],"al banco EAN")

    while(sesion==True):
        print("\n")
        print("Está en su cuenta",account_tipo[indice],"N°",numero_de_cuenta[indice])
        print("\n")
        print("ELIGA ALGUNA TRANSACCION POR EL NUMERO:")
        print("1: Consultar saldo")
        print("2: Consignar dinero")
        print("3: Hacer retiro")
        print("4: Transferir dinero")
        print("5: Cerrar sesión")

        while(True):
            try:
                opcion=int(input())
                break
            except Exception as error:
                print("Debes digitar una opción valida")

        if opcion in [1,2,3,4,5]:
            if account[indice] =='activa':
                if  opcion==1:
                    print("Saldo en cuenta",account_tipo[indice]," N°",numero_de_cuenta[indice] ,":",dinero[indice] )
                elif  opcion==2:
                    while(True):
                        try:
                            valor_consignacion=float(input("Digite el valor a consignar:"))
                            if valor_consignacion<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero y que este sea mayor a 0")
                    if valor_consignacion > 0:
                        dinero[indice] = dinero[indice] + valor_consignacion
                        print("Consignación exitosa")
                        print("Valor consignado:",valor_consignacion )
                        print("Saldo en cuenta:",dinero[indice] )       
                    else:
                        print("Error en valor ingresado")
                        
                elif  opcion==3:
                    print("Digite el valor a retirar:")
                    while(True):
                        try:
                            valor_retiro=float(input("Digite el valor a retirar:"))
                            if valor_retiro<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero y que este sea mayor a 0")
                    if valor_retiro > dinero[indice]:
                        print("Fondos insuficientes")
                    else:
                        dinero[indice]=dinero[indice]-valor_retiro
                        print("Valor retiro:",valor_retiro )
                        print("Saldo en cuenta:",dinero[indice] )
                elif  opcion==4:
                    while(True):
                        try:
                            valor_trasferencia=float(input("Digite el valor de la trasferencia:"))
                            if valor_trasferencia<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero y que este sea mayor a 0")
                    account_tipo_final=str(input("Digite el tipo de cuenta de destino:")).lower()
                    while(True):
                        try:
                            numero_de_cuenta_final=int(input("Digite el numero de cuenta de destino:"))
                            if numero_de_cuenta_final<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero correcto")
                    if valor_trasferencia > dinero[indice]:
                        print("fondos insuficientes")
                    else:
                        if numero_de_cuenta_final in numero_de_cuenta:
                            indice_cta=numero_de_cuenta.index(numero_de_cuenta_final)
                            if account_tipo_final==account_tipo[indice_cta]:
                                dinero[indice]=dinero[indice]-valor_trasferencia
                                dinero[indice_cta]=dinero[indice_cta]+valor_trasferencia
                                print("trasferencia exitosa la cuenta",account_tipo[indice_cta]," N°",numero_de_cuenta_final )
                                print("valor trasferencia:",valor_trasferencia)
                                print("saldo en cuenta",numero_de_cuenta[indice] ,":",dinero[indice] )
                            else:
                                print("tipo de cuenta incorrecto")
                        else: 
                            print("Numero de cuenta no existe")
                elif  opcion==5:        
                    if account[indice] =='activa':
                        account[indice] ='cerrada'
                        print("sesion cerrada")
                    else:
                        print("sesion ya está cerrada")
                    sesion=False
                else:
                    print("opcion invalida")   
            else:
                print("sesion no activa, tramite invalido")    
        else:
            print("Opción invalida")
            
    while(sesion_administrador==True):
        print("\n")
        print("ELIGA ALGUNA OPCION:")
        print("1: Crear cuenta")
        print("2: Eliminar cuenta")
        print("3: Consultar cuenta")
        print("4: Información todas las cuentas del banco")
        print("5: Aumentar interes diario a cuentas de ahorro")
        print("6: Cerrar sesión de administrador")
 
        while(True):
            try:
                opcion=int(input())
                break
            except Exception as error:
                print("Debes digitar una opción valida")

        if opcion in [1,2,3,4,5,6]:
            if  opcion==1:
                new_titular =   str(input("Ingrese nombre completo de la titular:"))
                new_user =   str(input("Ingrese nombre de usuario de la titular:"))
                if new_user in usuario:
                    print("El usuario ya existe, solo se permite un nombre de usuario por cuenta. Debe iniciar de nuevo el proceso.")
                else:
                     
                    while(True):
                        try:
                            contraseña_nuevo =  int(input("Ingrese contraseña numerica:"))
                            if contraseña_nuevo<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero correcto")
                    while(True):
                        try:
                            numero_de_cuenta_nuevo =  int(input("Ingrese numero de cuenta:"))
                            if numero_de_cuenta_nuevo<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero correcto")
                    if numero_de_cuenta_nuevo in numero_de_cuenta:
                        print("El numero de cuenta ya existe, es un numero unico independiente del tipo de cuenta. Debe iniciar de nuevo el proceso.")
                    else:                   
                        new_account = str(input("Ingrese tipo de cuenta (ahorros o corriente):")).lower()
                        if new_account == "corriente" or new_account == "ahorros":
                            
                            while(True):
                                try:
                                    dinero_nuevo = float(input("Ingrese saldo inicial de la cuenta:")) 
                                    if dinero_nuevo<0:
                                        raise
                                    break
                                except Exception as error:
                                    print("Debes digitar un numero y que este sea mayor a 0")
                            correo_nuevo = str(input("Ingresar correo electronico:"))
                            new_account = "cerrada"
                            
                            print("Los datos de la nueva cuenta fueron ingresados correctamente.")

                            titular.append(new_titular)
                            usuario.append(new_user)
                            contraseña.append(contraseña_nuevo)
                            numero_de_cuenta.append(numero_de_cuenta_nuevo)
                            account_tipo.append(new_account)
                            dinero.append(dinero_nuevo)
                            correo.append(correo_nuevo)
                            account.append(new_account)                         
                            
                            print("La cuenta se ha creado exitosamente.")                       
                        else:                    
                            print("Tipo de cuenta incorrecto. Debe iniciar de nuevo el proceso.")

            elif  opcion==2:
                
                while(True):
                    try:
                        numero_de_cuenta_eliminar =  int(input("Ingrese numero de cuenta a eliminar:"))
                        if numero_de_cuenta_eliminar<0:
                            raise
                        break
                    except Exception as error:
                        print("Debes digitar un numero correcto")
                if numero_de_cuenta_eliminar in numero_de_cuenta:
                    indice = numero_de_cuenta.index(numero_de_cuenta_eliminar)
                    titular.pop(indice)
                    usuario.pop(indice)
                    contraseña.pop(indice)
                    numero_de_cuenta.pop(indice)
                    account_tipo.pop(indice)
                    dinero.pop(indice)
                    correo.pop(indice)
                    account.pop(indice)  
                    print("La cuenta se ha eliminado exitosamente.") 
                else:    
                    print("El numero de cuenta no existe. Debe iniciar de nuevo el proceso.")
            elif  opcion==3:  
                print("\n")               
                while(True):
                    try:
                        numero_de_cuenta_consulta =  int(input("Digite el numero de cuenta a consultar:"))
                        if numero_de_cuenta_consulta<0:
                            raise
                        break
                    except Exception as error:
                        print("Debes digitar un numero correcto")
                if numero_de_cuenta_consulta in numero_de_cuenta:
                    indice_cta=numero_de_cuenta.index(numero_de_cuenta_consulta)
                    print("Estado cuenta consultada")
                    i = indice_cta
                    print("\n")
                    print("   Titular:",titular[i]) 
                    print("   Usuario:",usuario[i]) 
                    print("   Contraseña:",contraseña[i]) 
                    print("   Numero de cuenta:",numero_de_cuenta[i]) 
                    print("   Tipo de cuenta:",account_tipo[i]) 
                    print("   Dinero:",dinero[i]) 
                    print("   Correo:",correo[i]) 
                    print("   Estado sesion:",account[i]) 
                    print("\n")
                else: 
                    print("numero de cuenta consultada no existe")
                            
            elif  opcion==4:  
                print("\n")
                print("Estado cuentas banco")
                for i in list(range(0,len(titular))):
                    print("\n")
                    print(" Titular:",titular[i]) 
                    print(" Usuario:",usuario[i]) 
                    print(" Contraseña:",contraseña[i]) 
                    print(" Numero de cuenta:",numero_de_cuenta[i]) 
                    print(" Tipo de cuenta:",account_tipo[i]) 
                    print(" Dinero:",dinero[i]) 
                    print(" Correo:",correo[i]) 
                    print(" Estado sesion:",account[i]) 
                    print("\n")
            elif  opcion==5:  
                print("\n")
                print("Diariamente se realiza un aumento de interes del 0.003 (0.03%) a cada cuenta de ahorro.")

                while(True):
                    try:
                        numero_confirmacion =  int(input("Para confirma incremento de hoy digite 1, sino digite 2:"))
                        if 2<numero_confirmacion or numero_confirmacion<1:
                            raise
                        else:   
                            break
                    except Exception as error:
                        print("Dato ingresado incorrecto") 
                        
                if numero_confirmacion==1:  
                    for i in list(range(0,len(account_tipo))):
                        if account_tipo[i]=="ahorros":
                            dinero[i] = dinero[i]*(1+0.003)
                    print("Aumento por interes exitoso")
                if numero_confirmacion==2:
                    print("No se realiza aumento por interes")

                    
            elif  opcion==6:   
                sesion_administrador = False
                print("sesion administrador cerrada")

            else:
                print("Opción invalida")