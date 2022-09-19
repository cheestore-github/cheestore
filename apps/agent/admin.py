from django.contrib import admin
from .models import (AgentUser, Rule, Transfer)

admin.site.register(AgentUser)
admin.site.register(Rule)
admin.site.register(Transfer)


