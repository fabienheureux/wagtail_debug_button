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
3. Edit the title as "Initial title"
4. Save the page (as a draft)

After the page has been reloaded 
1. Click the dropdown (in the same place as the publish button)
2. Hit the "Synchronise" button
3. The title should still be "Initial title"

Then
1. Publish the page
2. Restart the synchronisation by clicking the "Synchronise" button
3. The title should now be "Another title"
