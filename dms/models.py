from django.db import models
from common.models import CommonModel

# Create your models here.


class ChattingRoom(CommonModel):
    """Room Model Definitio"""

    users = models.ManyToManyField(
        "users.User",
        related_name="chattingrooms",
    )

    def __str__(self):
        return "Chatting Room."


class Message(CommonModel):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="massages",
    )
    room = models.ForeignKey(
        "dms.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="chattingrooms",
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"
