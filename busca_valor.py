# ver en repl.it: https://repl.it/X3G/3976

# Metodo que busca si un valor existe en la lista 
def busca_valor (self, valor):
		
		nodo  = self.__primero
		
		while (nodo != None) :
			if (nodo.info == valor):
				return True 
			
			nodo = nodo.sig
			
			
		return False
