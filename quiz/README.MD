1. Создайте виртуальное окружение Python:

    ```bash
    python3 -m venv venv
    ```

2. Активируйте виртуальное окружение:

    - На Windows:

    ```bash
    venv\Scripts\activate
    ```

    - На macOS и Linux:

    ```bash
    source venv/bin/activate
    ```

3. Установите все зависимости проекта с помощью следующей команды:

    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции базы данных:

    ```bash
    python manage.py migrate
    ```

5. Запустите проект с помощью команды:

    ```bash
    python manage.py runserver
    ```
