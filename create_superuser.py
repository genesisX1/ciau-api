import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ciau_admin.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "ciauadmin"
email = "joackimdate0@gmail.com"
password = "ciauadmin"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser créé avec succès.")
else:
    print("Le superuser existe déjà.")
