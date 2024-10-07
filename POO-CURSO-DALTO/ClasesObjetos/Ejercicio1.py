class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre= nombre
        self.edad= edad
        self.grado= grado

    def estudiar(self):
        print(f'El estudiante {self.nombre} está estudiando')
        
firstName = input("Ingresa el nombre del estudiante: ")
edadEstudiante = input("Ingresa la edad del estudiante: ")
gradoEstudiante = input("Ingresa el grado del estudiante: ")

estudiate1 = Estudiante(firstName, edadEstudiante, gradoEstudiante)
print(f'''Nombre= {estudiate1.nombre}\nEdad= {estudiate1.edad}\nGrado={estudiate1.grado}''')

preguntaEstudia = input("Escribe la palabra 'estudia' si quieres imprimir el metodo: ").lower
if preguntaEstudia== 'estudia':
    estudiate1.estudiar()