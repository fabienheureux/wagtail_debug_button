# Wagtail - Debug sync page

This repo holds a reproducible example of a bug noticed while developping a wagtail website. 

## Setup

### With poetry

```bash
poetry install
```
  
```bash
poetry shell
```

### Without poetry

```bash
pip install -r requirements.txt
```

## Run example
  
```bash
python manage.py runserver
```

1. [Go to the homepage](http://localhost:8000/admin/pages/3/edit/)
2. Login with admin / admin
3. Edit the title
4. Click the dropdown (in the same place as the publish button)
5. Hit the "Sync page" button
6. The title should not be up-to-date 
