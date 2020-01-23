from datetime import date
from datetime import datetime

from contacts.contact import Person
from contacts.directory import Directory
from resources.messages import (
    MSG_EXIT,
    MSG_TO_ADD_CONTACT,
    MSG_VALUE_INVALID,
    MSG_WELCOME
)
from resources.texts import (
    TEXT_GET_COMMAND,
    TEXT_GET_EMAIL,
    TEXT_GET_FULL_NAME,
    TEXT_GET_ID_EXP_DATE,
    TEXT_GET_ID_NUMBER,
    TEXT_GET_ID_TYPE,
    TEXT_GET_PHONE_NUMBER
)


def run():
    """
    Main function
    """

    print(MSG_WELCOME)
    directory = Directory()

    while True:
        command = str(input(TEXT_GET_COMMAND))

        if command == "a":
            print(MSG_TO_ADD_CONTACT)

            try:
                id_type = get_id_type()
                id_number = get_id_number()
                id_exp_date = get_id_exp_date()
                full_name = get_full_name()
                email = get_email()
                phone_number = get_phone_number()
            except ValueError as err:
                print(err)
                print(MSG_VALUE_INVALID)
            else:
                directory.add(
                    id_type=id_type,
                    id_number=id_number,
                    id_exp_date=id_exp_date,
                    full_name=full_name,
                    email=email,
                    phone_number=phone_number
                )
        elif command == "b":
            directory.show()
        elif command == "x":
            print(MSG_EXIT)
            break
        else:
            print(MSG_VALUE_INVALID)


def get_id_type():
    id_type = str(input(TEXT_GET_ID_TYPE))
    index = Person.ID_TYPES.index(id_type.upper())

    return Person.ID_TYPES[index]


def get_id_number():
    return str(input(TEXT_GET_ID_NUMBER))


def get_id_exp_date():
    id_exp_date = str(input(TEXT_GET_ID_EXP_DATE))

    return datetime.strptime(id_exp_date, Person.DATE_FORMAT)


def get_full_name():
    return str(input(TEXT_GET_FULL_NAME))


def get_email():
    return str(input(TEXT_GET_EMAIL))


def get_phone_number():
    return str(input(TEXT_GET_PHONE_NUMBER))


if __name__ == "__main__":
    run()
