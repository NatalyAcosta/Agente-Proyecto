import random

#Se crea una clase maquinaMetales para establecer la funcionalidad de una maquina de Metales
class maquinaMetales():
    """
    Una clase que representa una maquina de metales.

    ...

    Attributes
    ----------
    costo : int
        El costo total de realizar el trabajo correspondiente.
        
    valor : int
        El valor inicial para crear las areas.
        
    diccionario_areas : dictionary
        Establece las areas en un diccionario.
        
    posicion_maquina_metales : str
        la posición en que se encuentra actualmente la máquina.
    
    Methods
    -------
    Informacion(): private
        Permite obtener la informacion del diccionario para su uso.
        
    identificarArea(): private
        identifica que areas se encuentran con metal.
        
    containZona(numero):
        Permite saber si una zona esta contenida en las areas con metal encontradas.
        
    redirigirPrimero(): private
        Redirige la maquina a la primera posicion de la lista de areas con metal encontrado.
        
    encenderMaquina():
        Enciende la maquina para ser utilizada.
    """
    def __init__(self):
        #Guarda el costo total de realizar el trabajo correspondiente
        self.costo=0
        #Guarda el valor inicial para crear las areas
        self.valor=1
        #Establece las areas en un diccionario
        self.diccionario_areas={}
        #Guardara la posición en que se encuentra actualmente la máquina 
        self.posicion_maquina_metales=''
    
    
    
    def __Informacion(self):
        
        """
        Obtiene la información con los sensores de la maquina busca metales.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        posicion_maquina_metales : int, required (<=20)
            Establece la posicion de la maquina de metales

        Returns
        -------
        None
        """
        
        
        #Establece 20 nodos para el agente
        locacionesEncontradas=20
        #Imprime el numero de locaciones encontradas
        print('La camara encontró '+ str(locacionesEncontradas)+' posiciones para buscar metales')
        while(True):
            #Metodo random para simular que un area esta con metal
            simularMetal=random.randint(0, 1)
            #Permitirá saber si ya termino el numero de locaciones
            if(self.valor<=locacionesEncontradas):
                
                areaEstado = simularMetal
                #Si el area esta con metal va a mostrarlo en pantalla
                if( areaEstado==1):
                    print('Se encontro metal en el area : '+str(self.valor))
                self.diccionario_areas[str(self.valor)] = [str(areaEstado),self.valor]
                self.valor+=1
            else:
                #detiene la ejecución
                break
        #Establecera la posición de la maquina de metales
        #Nota(debe tomarse en cuenta que no exceda de los 20)
        self.posicion_maquina_metales = input("Digite la zona en que se encuentra la Maquina: ")
    
    #Esta función sirve para identificar que areas se encuentran con metal
    def __identificarArea(self):
        """
        Crea una lista de las areas que se encuentran con Metal (sensores).

        Parameters
        ----------
        No requiere ningún parametro

        Returns
        -------
        Imprime las areas que se encuentran con Metal
        """
        #guardara las posiciones de areas con metal
        self.areasConMetalEncontradas=[]
        #recorrer el diccionario de areas
        for key in self.diccionario_areas:
            #si el area esta con metal se guardara
            if((self.diccionario_areas[key])[0]=='1'):
                self.areasConMetalEncontradas.append(key)
        
        
                
    
    #Este metodo te permitirá saber si una zona esta contenida en las areas con metal encontradas
    def containZona(self, numero):
        """
        Crea una lista de las areas que se encuentran con Metal.

        Parameters
        ----------
        numero : int
            Numero de area 

        Returns
        -------
        Imprime el area que hay metal (se compara con la de los sensores)
        """
        for x in self.areasConMetalEncontradas:
            if(str(numero)==str(x)):
                print('Encontro metal en la zona : '+str(x))
                return True
            
        return False
    
    #En este metodo se permitira mover la posicion al primer elemento del libro
    def __redirigirPrimero(self):
        """
        Redirige la maquina a la primera posicion que se encontro metales.

        Parameters
        ----------
        No se requiere de ningún parametro

        Returns
        -------
        Imprime el movimiento de la maquina busca metales
        """
        #si no hay areas vacias se terminara el programa
        if( not(not self.areasConMetalEncontradas)):
            
            #si la posicion de la maquina es la misma no se necesitara de movimientos extras
            if(self.posicion_maquina_metales==self.areasConMetalEncontradas[0]):
                
                pass
            else:
                #Se movera nuestra maquina a la posicion inicial de nuestro libro
                #la primera posicion de areasConMetalEncontradas es la posicion a la que queremos llegar
                for i in range(int(self.posicion_maquina_metales),int(self.areasConMetalEncontradas[0]),-1):
                    print('girando de zona '+str(i)+' a posicion '+str(i-1))
                    self.costo+=1
                #establecerá el movimiento de la maquina si la maquina se encuentra en la parte delantera
                for i in range(int(self.posicion_maquina_metales),int(self.areasConMetalEncontradas[0]),+1):
                    print('Arranca ...')
                    print('Girando ...')
                #la posicion actual es la primera posicion con metal
                self.posicion_maquina_metales=self.areasConMetalEncontradas[0]
                
    
    #En este metodo se establecera toda la logica de manera que usaremos los demás metodos
    def encenderMaquina(self):
        """
        Enciende la maquina buscadora de metales.

        Parameters
        ----------
        No se requiere pasar parametros

        Returns
        -------
        None
        """    
        self.__Informacion()
        self.__identificarArea()
        self.__redirigirPrimero()
        #si no hay areas vacias se terminara el programa
        if( not(not self.areasConMetalEncontradas)):
            #Se buscara las areas para limpiar con la maquina
            for i in range(int(self.posicion_maquina_metales) ,int(self.areasConMetalEncontradas[len(self.areasConMetalEncontradas)-1])+1,+1):
                #Comprobara si la maquina debe limpiar
                #si la zona es contenida en el array de areas con metal pues se movera y limpiara
                if(self.containZona(i)):
                    self.costo+=2
                    print('Arranca ...')
                    print('Girando...')
                else:
                    self.costo+=1
                    print('Arranca ...')
                    print('Girando...')
        
        print('Ya no se encontraron metales ')
        print('El costo seria '+str(self.costo))

limpiadorplatos= maquinaMetales()
limpiadorplatos.encenderMaquina()
help(maquinaMetales)
