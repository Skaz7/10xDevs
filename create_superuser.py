#!/usr/bin/env python
"""
Create a Django superuser by connecting directly to the database.
Usage: python create_superuser.py <username> <email> <password>
"""
import os
import sys
import django
from django.contrib.auth.models import User

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'embedded_projects_assistant.settings')
django.setup()

if len(sys.argv) < 4:
    print("Usage: python create_superuser.py <username> <email> <password>")
    sys.exit(1)

username = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

# Create superuser
if User.objects.filter(username=username).exists():
    print(f"User '{username}' already exists!")
    sys.exit(1)

User.objects.create_superuser(username=username, email=email, password=password)
print(f"✓ Superuser '{username}' created successfully!")
