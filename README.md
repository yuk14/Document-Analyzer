# Document Analyzer

A web application that analyzes PDF documents and provides detailed text statistics and insights.

## Features

- PDF document upload (drag & drop or file selection)
- Text analysis including:
  - Word count
  - Character count (with and without spaces)
  - Sentence count
  - Average word length
- Word frequency analysis
  - Top 20 most frequent words
  - Option to exclude common words (stop words)
- Responsive design (mobile-friendly)
- Real-time analysis with loading indicators
- Interactive word frequency visualization

## Tech Stack

- Frontend: HTML, CSS (Tailwind CSS), JavaScript
- Backend: Python, Django
- Text Processing: spaCy
- PDF Processing: PyPDF2
- Visualization: Chart.js

## Installation

1. Clone the repository 
bash
git clone https://github.com/yourusername/document-analyzer.git
cd document-analyzer

2. Create and activate a virtual environment:

```bash

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:

```bash
pip install -r requirements.txt

4. Download spaCy model
```bash
python -m spacy download en_core_web_sm
```

5. Create necessary directories
```bash
mkdir media
```

6. Apply migrations
```bash
python manage.py migrate
```

7. Run the development server
```bash
python manage.py runserver
```

Visit http://localhost:8000/upload/ to use the application.

## Usage

1. Upload a PDF document using drag & drop or file selection
2. Wait for the analysis to complete
3. View detailed statistics about your document
4. Toggle the "Exclude common words" option to filter out stop words
5. Explore the word frequency visualization

## API Documentation

### POST /upload/
Analyzes an uploaded PDF document.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body:
  - file: PDF file (required)
  - exclude_stopwords: boolean (optional)

**Response:**
```json
{
    "word_count": integer,
    "char_count": integer,
    "char_count_no_spaces": integer,
    "sentence_count": integer,
    "avg_word_length": float,
    "word_frequency": {
        "word1": count1,
        "word2": count2,
        ...
    }
}
```

## Design Decisions and Trade-offs

1. **spaCy vs NLTK**
   - Chose spaCy for better performance and easier setup
   - Trade-off: Larger package size but better accuracy

2. **Frontend Framework**
   - Used vanilla JavaScript for simplicity
   - Trade-off: Less structured code but no build process required

3. **File Storage**
   - Local storage in media directory
   - Trade-off: Simple setup but not scalable for production

4. **Word Frequency Analysis**
   - Limited to top 20 words for performance
   - Trade-off: Less comprehensive but better visualization

## Future Improvements

1. **Features**
   - Support for PDF with images, handwritten text, scanned documents, etc.
   - Support for more file formats (DOC, DOCX, TXT)
   - Advanced text analysis (readability scores, sentiment analysis)
   - Export analysis results
   - Batch processing multiple files

2. **Technical**
   - Add user authentication
   - Implement file upload progress
   - Add unit tests
   - Use Redis for caching analysis results
   - Implement cloud storage for files

3. **UI/UX**
   - Add dark mode
   - Implement more interactive visualizations
   - Add comparison feature for multiple documents
   - Add a chatbot for real-time queries

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [2025](Yukthi R) file for details.



