from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    
    question = models.TextField()
    answer = RichTextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)  # Bengali
    question_hi = models.TextField(null=True, blank=True)  # Hindi

    translator = Translator()  # Google Translator instance

    def translate_text(self, text, lang):
        """Translate text to the given language."""
        if not text:
            return None  # Return None if no text is provided
        
        try:
            translated = self.translator.translate(text, dest=lang).text  # Perform translation
            return translated
        except Exception as e:
            print(f"Translation Error: {e}")
            return text  # Return original text if translation fails

    def save(self, *args, **kwargs):
        """Override save method to auto-translate fields before saving."""
        if self.question:  # Ensure question exists before translating
            self.question_bn = self.translate_text(self.question, "bn")  # Bengali
            self.question_hi = self.translate_text(self.question, "hi")  # Hindi

        super().save(*args, **kwargs)  # Call the original save method
