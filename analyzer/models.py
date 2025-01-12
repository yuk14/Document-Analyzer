from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class Analysis(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    word_count = models.IntegerField()
    char_count = models.IntegerField()
    char_count_no_spaces = models.IntegerField()
    sentence_count = models.IntegerField()
    avg_word_length = models.FloatField()
    word_frequency = models.JSONField()