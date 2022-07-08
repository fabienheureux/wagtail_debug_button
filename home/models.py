from django.db import models

from wagtail.models import Page


class HomePage(Page):
    def crm_sync(self):
        self.title = "Another title"
        self.save()
