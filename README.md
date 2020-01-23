# Contact Directory

Application to simulate a contact directory

## Table of contents

1. [Requirements](#requirements)
1. [Installation](#installation)
1. [Develop](#develop)
1. [Testing](#testing)
1. [Add data to Identification System](#add-data-to-identification-system)

## Requirements

- Python 3.7
- pip

## Installation

1. Clone repository:

    ```sh
    git clone git@github.com:tamayonauta/contact-directory.git
    ```

1. Install requirements:

    ```sh
    pip3 install -r app/requirements/production.txt
    ```

1. Start project:

    ```sh
    python3 app/main.py
    ```

## Develop

1. Clone repository:

    ```sh
    git clone git@github.com:tamayonauta/contact-directory.git
    ```

1. Create virtual environment:

    ```sh
    python3 -m venv <my_env_name>
    ```

1. Activate virtual environment

    ```sh
    source <my_env_name>/bin/activate
    ```

1. Install requirements:

    ```sh
    pip install -r app/requirements/local.txt
    ```

1. Start project:

    ```sh
    python app/main.py
    ```

## Testing

1. Run commands:

    ```sh
    python -m unittest discover app/tests
    python -m unittest
    ```

## Add data to Identification System

1. Edit file:

    ```sh
    vim app/external_systems/data.py
    ```

1. Add data to `PERSONAL_DATA` list with this structure:

    ```python
    {
        "id_type": "CC",  # "CC", "CE", "PP"
        "id_number": "1000000",
        "id_exp_date": "2001-01-11",  # "%Y-%m-%d"
        "full_name": "John Doe"
    }
    ```

1. Save file

## License

This project is licensed under the terms of the MIT license.
