from rest_framework import serializers
from .models import FAQ

class FAQserializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id", "question", "answer", "question_bn", "question_hi"]

    def to_representation(self, instance):
        """Customize serializer output to return only selected language."""
        data = super().to_representation(instance)
        
        # Get language from context (provided in the view)
        lang = self.context.get("lang", "en")  # Default to English
        
        # Filter fields based on the requested language
        if lang == "bn":  # Bengali
            return {"id": data["id"], "question": data["question_bn"], "answer": data["answer"]}
        elif lang == "hi":  # Hindi
            return {"id": data["id"], "question": data["question_hi"], "answer": data["answer"]}
        else:  # Default English
            return {"id": data["id"], "question": data["question"], "answer": data["answer"]}

