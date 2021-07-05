# Books REST API

In environment variables or in _settings.py_:
- Set database credentials (default values in _docker-compose.yml_)
- Set GOOGLE_DEVELOPER_KEY

After creating virtualenv and installing requirements run:
```bash
docker-compose up
python manage.py runserver localhost:8000
```

Schema: http://localhost:8000/openapi