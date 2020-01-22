from datetime import date
from datetime import datetime

from contacts.contact import Person
from contacts.directory import Directory


def run():
    print("DIRECTORIO DE CONTACTOS")
    directory = Directory()

    while True:
        command = str(input(
            "\nSeleccione una opción:\n\n" +
            "[a] Agregar nuevo contacto\n" +
            "[b] Mostrar contactos\n" +
            "[x] Salir\n"
        ))

        if command == "a":
            try:
                id_type = get_id_type()
                id_number = get_id_number()
                id_exp_date = get_id_exp_date()
                full_name = get_full_name()
                email = get_email()
                phone_number = get_phone_number()

                result = directory.add(
                    id_type=id_type,
                    id_number=id_number,
                    id_exp_date=id_exp_date,
                    full_name=full_name,
                    email=email,
                    phone_number=phone_number
                )

                if result:
                    print("Operación exitosa")
                else:
                    print("El contacto no se puede agregar al directorio")
            except ValueError as err:
                print(err)
                continue
        elif command == "b":
            directory.show()
        elif command == "x":
            break
        else:
            print("Opción incorrecta")


def get_id_type():
    id_type = str(input(
        "Seleccione tipo de identificación:\n\n" +
        "[cc] Cédula\n" +
        "[ce] Cédula de extranjeria\n" +
        "[pp] Pasaporte\n"
    ))
    index = Person.ID_TYPES.index(id_type.upper())

    return Person.ID_TYPES[index]


def get_id_number():
    return str(input("Ingrese número de documento:\n"))


def get_id_exp_date():
    id_exp_date = str(input(
        "Ingrese fecha de expedición de documento (YYYY-MM-DD):\n"
    ))

    return datetime.strptime(id_exp_date, Person.DATE_FORMAT)


def get_full_name():
    return str(input("Ingrese nombre completo:\n"))


def get_email():
    return str(input("Ingrese correo:\n"))


def get_phone_number():
    return str(input("Ingrese número de teléfono:\n"))


if __name__ == "__main__":
    run()
