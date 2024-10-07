class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        return f"El estudiante {self.nombre} está estudiando"

def input_with_validation(prompt, type_func=str):
    while True:
        user_input = input(prompt)
        if user_input:
            try:
                return type_func(user_input)
            except ValueError:
                print("Entrada no válida. Por favor, intente nuevamente.")
        else:
            print("Este campo no puede estar vacío. Por favor, intente nuevamente.")

while True:
    name = input_with_validation("Ingresa el nombre del estudiante: ")
    age = input_with_validation("Ingresa la edad del estudiante: ", int)
    course = input_with_validation("Ingresa el grado del estudiante: ", int)
    estudiante = Estudiante(name, age, course)

    print(f"El estudiante {estudiante.nombre} registrado con éxito.")

    # Añadir opción para registrar otro estudiante o salir
    continuar = input("¿Deseas registrar otro estudiante? (s/n): ")
    if continuar.lower() != 's':
        break

while True:
    study = input_with_validation("escribe 'estudiar' si deseas poner a estudiar a determinado estudiante")
    if study.lower() != 'estudiar':
        print("Intenta de nuevo")
    else:
        print(estudiante.estudiar())
        break
