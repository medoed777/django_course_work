from django.urls import path

from recipients.apps import RecipientsConfig
from recipients.views import (RecipientCreateView, RecipientDeleteView,
                              RecipientsListView)

app_name = RecipientsConfig.name

urlpatterns = [
    path("", RecipientsListView.as_view(), name="recipients"),
    path("create_recipient", RecipientCreateView.as_view(), name="create_recipient"),
    path(
        "delete_recipient/<int:pk>",
        RecipientDeleteView.as_view(),
        name="delete_recipient",
    ),
]