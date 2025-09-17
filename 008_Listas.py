"""
Esto codigo es referente a la Leccion 10 del curso de Python
"""

print('Buen dia, usted esta ingresando al registro de usuarios\nIniciemos con el registro.\n')
nombre= input('Cual es su nombre? ')
edad= int(input('Cual es su edad? '))

usuarios = [] # Lista vacia

usuarios.append(nombre.capitalize()) # El metodo append agrega un elemento al final de la lista
usuarios.append(edad) # El metodo append agrega un elemento al final de la lista

fecha_nacimiento = input('Cual es tu fecha de nacimiento? (DD/MM/AAAA) ')
usuarios.insert(1, fecha_nacimiento) # El metodo insert agrega un elemento en la posicion que le indiquemos, en este caso en la posicion 1

registro = input('Cual es tu numero de registro? ')
usuarios.insert(2, registro) # El metodo insert agrega un elemento en la posicion que le indiquemos, en este caso en la posicion 2

usuarios[0] = 'Martha' # Podemos cambiar el valor de un elemento de la lista indicando su posicion

print('\nGracias por registrarte, estos son tus datos:\n')
print(f'Alumno {usuarios[0]}, con fecha de nacimiento {usuarios[1]}, con numero de registro {usuarios[2]} y con {usuarios[3]} años de edad.')

dato_a_cambiar = input('\nSi existe algun error en los datos ingresados, ingrese el dato que quiere cambiar escriba si : ')

print('\nEs posible que sea el nombre, ingrese nuevamente el nombre: ')
nuevo_nombre = input('Cual es su nombre? ') 
usuarios[0] = nuevo_nombre.capitalize() # Cambiamos el valor del elemento en la posicion 0

print('\nGracias por registrarte, estos son tus datos actualizados:\n')
print(f'Alumno {usuarios[0]}, con fecha de nacimiento {usuarios[1]}, con numero de registro {usuarios[2]} y con {usuarios[3]} años de edad.')

print('\nParece que ya no es necesario el tener su edad. Por lo que seara eliminado el dato de la lista.\n')
usuarios.pop() # El metodo pop elimina el ultimo elemento de la lista
print(f'Los datos que tenemos son: {usuarios}')

print('\nTampoco es necesario tener su fecha de nacimiento. Por lo que seara eliminado el dato de la lista.\n')
usuarios.pop(1) # El metodo pop elimina el elemento en la posicion que le indiquemos, en este caso en la posicion 1

print(f'Los datos que tenemos son: {usuarios}\n')

print('Parece que su usuario fue hackeado y se agregaron mas nombres a su usuario.\n')
usuarios.extend(['Ana', 'Luis', 'Carlos']) # El metodo extend agrega varios elementos al final de la lista
print(f'Los datos que tenemos son: {usuarios}\n')
usuarios.remove('Carlos') # El metodo remove elimina el elemento que le indiquemos, en este caso el elemento 'Carlos'
usuarios.remove('Ana') # El metodo remove elimina el elemento que le indiquemos, en este caso el elemento 'Ana'
usuarios.remove('Luis') # El metodo remove elimina el elemento que le indiquemos, en este caso el elemento 'Luis'

print('Ya se eliminaron los nombres que no correspondian a su usuario.\n')
print(f'Los datos que tenemos son: {usuarios}\n')

print('Ingrese su nombre nuevamente para corroborar que su nombre siga en la lista:\n')
nombre_comprobar = input('Cual es su nombre? ')
usuarios.index(nombre_comprobar.capitalize()) # El metodo index nos dice la posicion del elemento que le indiquemos, en este caso el nombre ingresado
print(f'Su nombre {nombre_comprobar.capitalize()} se encuentra en la posicion {usuarios.index(nombre_comprobar.capitalize())} de la lista.\n')

print('Ahora busquemos que no se repita su nombre en la lista.\n')
print(f'El nombre {nombre_comprobar.capitalize()} se repite {usuarios.count(nombre_comprobar.capitalize())} veces en la lista.\n') # El metodo count nos dice cuantas veces se repite el elemento que le indiquemos, en este caso el nombre ingresado

print('Finalmente ordenemos la lista Final.\n')
print(f'Lista final: {usuarios}\n')

print('Gracias por registrarte, que tengas un buen dia.\n')