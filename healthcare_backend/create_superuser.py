import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare_backend.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser(username, email, password):
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created successfully.")
    else:
        print(f"Superuser '{username}' already exists.")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python create_superuser.py <username> <email> <password>")
    else:
        _, username, email, password = sys.argv
        create_superuser(username, email, password)
