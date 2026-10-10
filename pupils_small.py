import time

class Pupil:
    def __init__(self, Surname, Name, Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark


pupils = []


def print_class(pupils):
    for pupil in pupils:
        print(pupil.Surname, pupil.Name, "-", pupil.Mark)

    print()


def print_five(pupils):
    print("Mejores estudiantes:")

    for pupil in pupils:
        if pupil.Mark == 5:
            print(pupil.Surname, pupil.Name)

    print()


def find_average(pupils):
    if len(pupils) == 0:
        print("No hay estudiantes registrados.")
        return

    average = 0

    for pupil in pupils:
        average += pupil.Mark

    average /= len(pupils)

    print("Calificación promedio de la clase:", average)


start_time = time.time()


with open("pupils_large.txt", "r") as file:

    for line in file:

        data = line.split()

        if len(data) == 3:

            surname = data[0]
            name = data[1]
            mark = int(data[2])

            pupil = Pupil(surname, name, mark)
            pupils.append(pupil)

        elif len(data) == 2 and data[1][-1].isdigit():

            surname = data[0]
            name = data[1][:-1]
            mark = int(data[1][-1])

            pupil = Pupil(surname, name, mark)
            pupils.append(pupil)

        else:
            print("Línea no válida:", line.strip())


print_five(pupils)

find_average(pupils)

print("Cantidad de estudiantes:", len(pupils))

execution_time = time.time() - start_time

print("Tiempo de ejecución:", execution_time, "segundos")