import time
def mostrar_bienvenida():
	print('''
	                 SOPA DE LETRAS

         ''')
mostrar_bienvenida()


def temas():
	print ("""
		1) Jugar

		2) Salir de la Sopa de Letras
			""")
	opcion = input("Ingresa una opción: ")
			 
	if opcion != "1" and opcion != "2":
		print ("Opcion incorrecta, Ingrese una opcion valida")
		opcion = input("Ingresa una opción: ->  ")
		temas()
	elif opcion == "1":
		print("""
					  A) Buscar Verbos
					  B) Buscar Sustantivos
					  C) Buscar Adjetivos
					  """)
		op = input("Ingrese tipos de palabras que quiere buscar: ")
		if op == "a":
			def dificultad_Verbos():
				print("""
					NIVEL DE DIFICULTAD
					    1) Facil
					    2) Intermedio
					    3) Dificil
					  """)
				op= input("Elija el nivel de dificultad: ")

				if op != "1" and op != "2" and op != "3":
						print ("Opcion incorrecta, Ingrese una opcion valida")
						op= input("Elija el nivel de dificultad: ")
				print("")
				print("")		
				input("Presione Enter para empezar a jugar. ")
				
				if op == "1":
					print("""
			    		p  r  i  m  a  g  r  i  e  t  a  
			 	 	s  p  d  i  s  a  l  t  a  r  o  
				 	u  a  o  k  v  b  a  i  l  a  r  
				 	b  e  r  c  j  u  t  m  o  l  i  
				 	i  r  m  o  k  s  h  l  m  a  w  
				 	r  b  i  m  x  c  z  r  r  d  q  
				 	a  t  r  e  n  a  r  o  n  i  m  
				 	c  o  r  r  e  r  o  t  a  ñ  c  
				 	t  c  b  a  j  a  r  x  d  q  v  
				    	o  a  r  o  c  a  n  t  a  r  z  
				 	h  r  a  t  v  o  l  a  r  z  x  
				 	r  a  t  a  w  e  f  i  o  p  i  
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el verbo encontrado:  ")
						if preg == "comer":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "bailar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "cantar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "saltar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "correr":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "buscar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "nadar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "tocar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "volar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "dormir":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						else:
							print("La palabra no se encuentra en la sopa de letras, seguí intentando.")
						
						final = time.time()

						if final - inicio >= 300:
							print("")
							print("Se terminó el tiempo :(")
							break
					print("")
					print("Los Verbos encontrados fueron", aciertos)

				elif op == "2":
					print("""
			       		p  r  i  m  a  g  r  i  e  t  a
			 	 	s  p  r  i  s  a  l  t  a  r  o  
				 	u  a  o  k  v  b  a  i  l  a  r  
				 	b  e  m  c  j  u  t  m  o  l  i  
				 	i  r  p  o  k  s  h  l  m  a  w  
				 	r  b  e  m  x  c  z  r  r  d  q  
				 	a  t  r  e  n  a  r  o  n  i  m  
				 	c  o  r  r  e  r  o  t  a  ñ  c  
				 	t  c  b  a  j  a  r  x  d  q  v  
					o  a  r  o  c  a  n  t  a  r  z  
				 	h  r  a  t  v  o  l  a  r  z  x  
				 	r  a  t  a  w  e  f  i  o  p  i  
				""")

					inicio = time.time()
					aciertos= 0
					while True:
						preg = input("Ingrese el verbo que encontró:  ")
						if preg == "comer":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "bailar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "cantar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "saltar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "correr":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "buscar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "nadar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "tocar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "volar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "romper":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "subir":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "bajar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						else:
							print("La palabra no se encuentra en la sopa de letras, seguí intentando.")
						
						final = time.time()

						if final - inicio >= 200:
							print("")
							print("Se terminó el tiempo :(")
							break
					print("")
					print("Los Verbos encontrados fueron", aciertos)


				elif op == "3":
					print("""
			       		p  r  i  m  a  g  r  i  e  t  a 
			 	 	s  p  r  i  s  a  l  t  a  r  o  
				 	u  a  o  k  v  b  a  i  l  a  r  
				 	b  e  m  c  j  u  t  m  o  l  i  
				 	i  r  p  o  k  s  h  l  m  a  w  
				 	r  b  e  m  x  c  z  r  r  d  q  
				 	a  t  r  e  n  a  r  o  n  i  m  
				 	c  o  r  r  e  r  o  t  a  ñ  c  
				 	t  c  b  a  j  a  r  x  d  q  v  
				   	o  a  r  o  c  a  n  t  a  r  z  
				 	h  r  a  t  v  o  l  a  r  z  x  
				 	r  a  t  a  w  e  f  i  o  p  i  
				""")
					inicio = time.time()
					aciertos= 0
					while True:
						preg = input("Ingrese el verbo que encontró:  ")
						if preg == "comer":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "bailar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "cantar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "saltar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "correr":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "buscar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "nadar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "tocar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "volar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "romper":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "subir":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "bajar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						else:
							print("La palabra no se encuentra en la sopa de letras, seguí intentando.")
						
						final = time.time()

						if final - inicio >= 100:
							print("")
							print("Se termino el tiempo :(")
							break
					print("")
					print("Los Verbos encontrados fueron", aciertos)

			dificultad_Verbos()
			
		elif op == "b":
			def dificultad_Sustantivos():
				print("""
					Nivel de dificultad
					    1) Facil
					    2) Intermedio
					    3) Dificil
					  """)
				op= input("Indique el nivel de dificultad: ")

				if op != "1" and op != "2" and op != "3":
						print ("Opcion incorrecta, Ingrese una opcion valida")
						op= input("Indique el nivel de dificultad: ")
				print("")
				print("")		
				input("Presione Enter para empezar.")
				
				if op == "1":
					print("""

			      		c  r  i  m  a  g  r  o  s  i  p  
			 	 	a  a  r  i  p  a  l  w  a  r  l  
				 	m  a  s  k  v  m  a  i  l  a  a  
				 	p  e  m  a  r  b  o  l  o  l  t  
				 	o  r  p  o  k  a  h  b  m  a  o  
				 	a  b  e  m  x  c  z  a  r  d  q  
				 	t  r  e  m  e  r  a  n  n  i  m  
				 	e  o  p  e  l  o  c  c  l  ñ  c  
				 	p  c  b  a  j  a  e  o  e  s  a  
					r  a  r  o  c  a  ñ  t  a  r  z  
				 	a  r  a  t  y  o  u  a  r  z  x  
				 	s  i  l  l  a  e  m  i  o  p  i 
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Sustantivo que encontró:  ")
						if preg == "casa":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "arbol":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "pelota":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "muñeca":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "remera":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "plato":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "piso":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "carpeta":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "mesa":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "silla":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						else:
							print("No se encuentra ese Sustantivo en la sopa de letras, seguí intenando.")
						
						final = time.time()

						if final - inicio >= 300:
							print("")
							print("Se terminó el tiempo :(")
							break
					print("")
					print("Los Sustantivos encontrados fueron", aciertos)

				elif op == "2":
					print("""
			       		c  r  i  m  a  g  r  o  s  i  p  
			 	 	a  a  r  i  p  a  l  w  a  r  l  
				 	m  a  s  k  v  m  a  i  l  a  a  
				 	p  e  m  a  r  b  o  l  o  l  t  
				 	o  r  p  o  k  a  h  b  m  a  o  
				 	a  b  e  m  x  c  z  a  r  d  q  
				 	t  r  e  m  e  r  a  n  n  i  m  
				 	e  o  p  e  l  o  c  c  l  ñ  c  
				 	p  c  b  a  j  a  e  o  e  s  a  
				   	r  a  r  o  c  a  ñ  t  a  r  z  
				 	a  r  a  t  y  o  u  a  r  z  x  
				 	s  i  l  l  a  e  m  i  o  p  i  
			""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Sustantivo que encontró:  ")
						if preg == "casa":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "arbol":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "pelota":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "muñeca":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "remera":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "plato":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "piso":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "carpeta":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "mesa":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "silla":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "campo":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "banco":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						else:
							print("No se encuentra ese Sustantivo en la sopa de letras, seguí intentando.")
						
						final = time.time()

						if final - inicio >= 200:
							print("")
							print("Se terminó el tiempo.")
							break
					print("")
					print("Los Sustantivos encontrados fueron", aciertos)


				elif op == "3":
					print("""
			       		c  r  i  m  a  g  r  o  s  i  p  
			 	 	a  a  r  i  p  a  l  w  a  r  l  
				 	m  a  s  k  v  m  a  i  l  a  a  
				 	p  e  m  a  r  b  o  l  o  l  t  
				 	o  r  p  o  k  a  h  b  m  a  o  
				 	a  b  e  m  x  c  z  a  r  d  q  
				 	t  r  e  m  e  r  a  n  n  i  m  
				 	e  o  p  e  l  o  c  c  l  ñ  c  
				 	p  c  b  a  j  a  e  o  e  s  a  
				   	r  a  r  o  c  a  ñ  t  a  r  z  
				 	a  r  a  t  y  o  u  a  r  z  x  
				 	s  i  l  l  a  e  m  i  o  p  i  
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Sustantivo que encontro:  ")
						if preg == "casa":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "arbol":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "pelota":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "muñeca":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "remera":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "plato":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "piso":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "carpeta":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "mesa":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "silla":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "campo":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "banco":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						else:
							print("No se encuentra ese Sustantivo en la sopa de letras, seguí intentando.")
						
						final = time.time()

						if final - inicio >= 100:
							print("")
							print("Se terminó el tiempo :(")
							break
					print("")
					print("Los Sustantivos encontrados fueron", aciertos)


			dificultad_Sustantivos()
			
		elif op == "c":
			def dificultad_Adjetivos():
				print("""
					NIVEL DE DIFICULTAD
					    1) Facil
					    2) Intermedio
					    3) Dificil
					  """)
				op= input("Indique el nivel de dificultad: ")

				if op != "1" and op != "2" and op != "3":
						print ("Opcion incorrecta, Ingrese una opcion valida")
						op= input("Indique el nivel de dificultad: ")
				print("")
				print("")		
				input("Presione Enter para empezar, mucha suerte!")
				
				
				if op == "1":
					print("""
			       		b  r  i  m  a  g  r  a  n  d  e  
			 	 	r  p  e  l  a  d  o  t  a  r  f  
				 	i  e  o  k  v  b  a  m  l  a  l  
				 	l  q  m  c  c  u  t  m  o  l  a  
				 	l  u  p  o  o  a  m  a  b  l  e  
				 	a  e  e  m  l  c  z  r  r  d  o  
				 	n  ñ  r  e  o  p  r  o  n  i  m  
				 	t  a  n  c  r  e  f  t  a  ñ  c  
				 	e  c  p  v  a  l  i  e  n  t  e  
				   	o  a  r  o  d  u  n  m  a  r  z  
				 	h  r  a  t  o  d  o  a  r  z  x  
				 	f  l  a  c  o  o  f  a  l  t  o  
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Adjetivo que encontro:  ")
						if preg == "grande":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "alto":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "valiente":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "brillante":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "pequeña":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "ancho":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "peludo":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "pelado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "flaco":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "fino":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						else:
							print("La palabra no se encuentra en la sopa de letras, seguí intentando.")
						
						final = time.time()

						if final - inicio >= 300:
							print("")
							print("Se terminó el tiempo :(")
							break
					print("")
					print("Los Adjetivos encontrados fueron", aciertos)

				elif op == "2":
					print(""" 
			       		b  r  i  m  a  g  r  a  n  d  e  
			 	 	r  p  e  l  a  d  o  t  a  r  f  
				 	i  e  o  k  v  b  a  m  l  a  l  
				 	l  q  m  c  c  u  t  m  o  l  a  
				 	l  u  p  o  o  a  m  a  b  l  e  
				 	a  e  e  m  l  c  z  r  r  d  o  
				 	n  ñ  r  e  o  p  r  o  n  i  m  
				 	t  a  n  c  r  e  f  t  a  ñ  c  
				 	e  c  p  v  a  l  i  e  n  t  e  
				   	o  a  r  o  d  u  n  m  a  r  z  
				 	h  r  a  t  o  d  o  a  r  z  x  
				 	f  l  a  c  o  o  f  a  l  t  o  
					""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Adjetivo que encontro:  ")
						if preg == "grande":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "alto":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "valiente":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "brillante":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "pequeña":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "ancho":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "peludo":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "pelado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "flaco":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "fino":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "colorado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "amable":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						else:
							print("La palabra no se encuentra en la sopa de letras, seguí intentando.")
						
						final = time.time()

						if final - inicio >= 200:
							print("")
							print("Se terminó el tiempo")
							break
					print("")
					print("Los Adjetivos encontrados fueron", aciertos)


				elif op == "3":
					print("""
			       		b  r  i  m  a  g  r  a  n  d  e  
			 	 	r  p  e  l  a  d  o  t  a  r  f  
				 	i  e  o  k  v  b  a  m  l  a  l  
				 	l  q  m  c  c  u  t  m  o  l  a  
				 	l  u  p  o  o  a  m  a  b  l  e  
				 	a  e  e  m  l  c  z  r  r  d  o  
				 	n  ñ  r  e  o  p  r  o  n  i  m  
				 	t  a  n  c  r  e  f  t  a  ñ  c  
				 	e  c  p  v  a  l  i  e  n  t  e  
				   	o  a  r  o  d  u  n  m  a  r  z  
				 	h  r  a  t  o  d  o  a  r  z  x  
				 	f  l  a  c  o  o  f  a  l  t  o  
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Adjetivo que encontro:  ")
						if preg == "grande":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "alto":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "valiente":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "brillante":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "pequeña":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "ancho":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "peludo":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "pelado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "flaco":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "fino":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "colorado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						elif preg == "amable":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
						else:
							print("La palabra no se encuentra en la sopa de letras, seguí intentando.")
						
						final = time.time()

						if final - inicio >= 100:
							print("")
							print("Se terminó el tiempo.")
							break
					print("")
					print("Los Adjetivos encontrados fueron", aciertos)


			dificultad_Adjetivos()
		
		temas()	
		while op != "a" and op != "b" and op != "c":
			print ("Opción incorrecta, ingrese una opcion valida.")
			op = input("Ingrese una opción: ")


	elif  opcion == "2":
		print("Saliste de la Sopa de Letras")
					
		exit()

temas()