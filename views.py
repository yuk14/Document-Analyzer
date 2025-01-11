import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import PyPDF2
import spacy
from collections import Counter
import io

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

@csrf_exempt
def upload_document(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file uploaded'}, status=400)
        
        file = request.FILES['file']
        
        if not file.name.endswith('.pdf'):
            return JsonResponse({'error': 'Invalid file type. Please upload PDF files only.'}, status=400)
        
        try:
            # Read PDF content
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            # Process text with spaCy
            doc = nlp(text)
            
            # Calculate statistics
            words = [token.text.lower() for token in doc if not token.is_space]
            sentences = list(doc.sents)
            
            # Remove stopwords and punctuation for frequency analysis
            words_no_stop = [token.text.lower() for token in doc 
                           if not token.is_stop and not token.is_punct and token.text.strip()]
            
            # Calculate statistics
            word_count = len(words)
            char_count = len(text)
            char_count_no_spaces = len(text.replace(" ", ""))
            sentence_count = len(sentences)
            avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
            
            # Word frequency (top 20)
            word_freq = Counter(words_no_stop).most_common(20)
            
            analysis = {
                'word_count': word_count,
                'char_count': char_count,
                'char_count_no_spaces': char_count_no_spaces,
                'sentence_count': sentence_count,
                'avg_word_length': round(avg_word_length, 2),
                'word_frequency': dict(word_freq)
            }
            
            return JsonResponse(analysis)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return render(request, 'analyzer/upload.html') 