# cmput404-lab04

## Getting started

1. Initialize database
   ```sh
   python manage.py migrate
   ```
2. Run server at port 3000
   ```sh
   python manage.py runserver
   ```

## Maintenance

Questions and choices under `/polls` can be created by a super user. This super user can be created by running

```sh
python manage.py createsuperuser
```

You should enter the desired user credentials. You can test this credentials by vising the admin page at [localhost:8000/admin](localhost:8000/admin).
