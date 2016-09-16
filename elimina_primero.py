# ver en repl.it: https://repl.it/X3G/3977

# Metodo para eliminar el primer elemento de la lista
	def elimina_primero(self):
		
		if (self.__primero == None):
			return
		h = self.__primero
		self.__primero = h.sig
		if (self.__actual == h):

		
			self.__actual = h.sig

			
		elif (self.__ultimo == h):
			
			self.__ultimo = h.sig
			
		self.__n = self.__n - 1
		self.__pos = self.__pos - 1
		del h
