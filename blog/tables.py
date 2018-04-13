import django_tables2 as tables
from .models import Guru

class GuruTable(tables.Table):
    class Meta:
        model = Guru
        template_name = 'home.html'