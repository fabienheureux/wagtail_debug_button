from wagtail.admin import messages
from wagtail.models import Page
from django.shortcuts import redirect


def sync_page(request):
    id = request.GET.get("id")

    page = Page.objects.get(id=id).specific
    page.crm_sync()
    messages.success(request, "The page has been synchronised")

    return redirect("wagtailadmin_pages:edit", id)
