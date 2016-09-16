# ver en repl.it: https://repl.it/X3G/3975

# Metodo para ubicar en actual en la posicion "pos" (enviada por parametro)
def pos_actual(self, pos):
		
	if (pos > self.__n):
		return

	nodo = self.__primero
	p = 0
	while (nodo != None):
		if (p == pos):
			self.__actual = nodo
			self.__pos = p
			return
		p = p + 1
		nodo = nodo.sig
