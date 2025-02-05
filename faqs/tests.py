from rest_framework.test import APITestCase
from .models import FAQ
from .serializers import FAQserializer
from django.urls import reverse

class FAQModelTest(APITestCase):
    def test_translate_text(self):
        faq = FAQ.objects.create(question="Hello", answer="Answer")
        translated_text = faq.translate_text(faq.question, "bn")
        self.assertIsNotNone(translated_text)
    
    def test_faq_creation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="Django is a framework.")
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "Django is a framework.")

class FAQViewTest(APITestCase):
    def test_get_faqs(self):
        faq = FAQ.objects.create(question="What is Django?", answer="Django is a framework.")
        url = reverse('faq-list')  # Adjust the name if required
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_faq(self):
        url = reverse('faq-list')  # Adjust the name if required
        data = {'question': 'How to use Django?', 'answer': 'Use it with Python.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['question'], 'How to use Django?')
