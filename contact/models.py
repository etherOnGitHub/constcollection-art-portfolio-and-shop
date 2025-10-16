from django.db import models


class ContactMessage(models.Model):
	"""Stores messages sent via the contact form."""
	name = models.CharField(max_length=120)
	email = models.EmailField()
	subject = models.CharField(max_length=200, blank=True)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return f"{self.name} <{self.email}> - {self.subject or 'no subject'}"
