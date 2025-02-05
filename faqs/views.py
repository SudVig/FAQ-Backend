from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQserializer

class FAQview(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")  # Get lang from query params (default: English)
        
        # Check if cached data is available for the specific language
        cache_key = f"faqs_{lang}"  # A unique cache key based on the language
        cached_data = cache.get(cache_key)

        if cached_data:
            # If cache is found, return it
            print("responding from cache")
            return Response(cached_data)

        # If no cache found, fetch data from the database
        faqs = FAQ.objects.all()
        serializer = FAQserializer(faqs, many=True, context={"lang": lang})

        # Store the serialized data in the cache for 1 hour (3600 seconds)
        cache.set(cache_key, serializer.data, timeout=3600)

        return Response(serializer.data)

    def post(self, request):
        org_question = request.data.get("question")
        

        if not org_question:
            return Response(data="Invalid Question", status=400)
        
        FAQobj = FAQ(question=org_question)
        FAQobj.save()
        
        # Invalidate cache for all FAQs to refresh it
        cache.delete(f"faqs_en")
        cache.delete(f"faqs_bn")
        cache.delete(f"faqs_hi")

        serialized_FAQ = FAQserializer(FAQobj)
        return Response(serialized_FAQ.data, status=201)
