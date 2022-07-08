from wagtail.admin.action_menu import ActionMenuItem
from wagtail.core import hooks

class SyncPageMenuItem(ActionMenuItem):
    name = "sync-page"
    label = "Synchronise"
    icon_name = "tick"

    def get_url(self, context):
        page = context["page"]
        return f"/sync-page/?id={page.id}"

    def is_shown(self, context):
        return True


@hooks.register("register_page_action_menu_item")
def register_sync_page_menu_item():
    return SyncPageMenuItem(order=10)
