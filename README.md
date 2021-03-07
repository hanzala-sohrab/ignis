# ignis

An eventbrite like website where users can add their events, and also like and dislike events.

## Steps to run a local server

1. Install the required modules
   ```shell
    pip install -r requirements.txt
    ```
2. Make migrations
    ```shell
    python manage.py makemigrations profiles
    python manage.py makemigrations events
    ```
3. Apply migrations
    ```shell
    python manage.py migrate
    ```
4. Create superuser
   ```shell
    python manage.py createsuperuser
    ```
5. Run server
    ```shell
    python manage.py runserver
    ```
