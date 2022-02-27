from random import choice
from string import ascii_letters, digits

from django.db import models

URL_HASH_SYMBOLS = ascii_letters + digits
URL_HASH_LENGTH = 7


class URL(models.Model):
    long_url = models.URLField(verbose_name="Original URL")
    hash = models.CharField(
        verbose_name="Original URL hash",
        max_length=20,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Time URL created at",
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = "".join(
                [choice(URL_HASH_SYMBOLS) for _ in range(URL_HASH_LENGTH)]
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Url hash: {self.hash}, created at: {self.created_at}"
