from django.apps import AppConfig
import nltk


class AnalyzerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analyzer'

    def ready(self):
        # Download required NLTK data
        try:
            nltk.download('punkt')
            nltk.download('stopwords')
        except:
            print("Error downloading NLTK data")
