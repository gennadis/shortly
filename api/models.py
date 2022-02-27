from django.db import models


class URL(models.Model):
    original_url = models.URLField(verbose_name="Original URL")
    url_hash = models.CharField(
        verbose_name="Original URL hash",
        max_length=20,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Time URL created at",
        auto_now_add=True,
    )

    def __str__(self):
        return f"Original URL: {self.long_url}, created at: {self.created_at}"
