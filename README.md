# django_auth_extension
Extend Django Auth Module 

##Requirement:
1. Setup Python
2. Setup Django
3. Create project "django-admin startproject <project_name>"

##STEPS:
1. Add this module name in projects(ex <project_name>) installed apps

```html INSTALLED_APPS = (
  .....
  'auth_module',
  .....
)```
2. Add Auth_Module urls in projects(ex <project_name>)

```html urlpatterns = [
    ..........
    url(r'^',include('auth_module.urls')),
    ..........
]```
