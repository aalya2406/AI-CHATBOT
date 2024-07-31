# streamlit run "/Users/aalyavora/Desktop/PDF Document Analyzer - GenAI copy/app.py"
import os
import requests
from PyPDF2 import PdfFileReader
from paddleocr import PaddleOCR


def save_uploaded_file(uploaded_file):
    """Saves an uploaded file to the server."""
    try:
        os.makedirs("uploaded_files", exist_ok=True)
        file_path = os.path.join("uploaded_files", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        print(f"File saved successfully: {file_path}")
        return file_path
    except Exception as e:
        print(f"Error saving file: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    """Converts a PDF file to text."""
    try:
        with open(pdf_path, "rb") as f:
            pdf_reader = PdfFileReader(f)
            text = ""
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                page_text = page.extract_text()
                print(f"Page {page_num}: {page_text}")
                text += page_text
        return text
    except Exception as e:
        print(f"Error converting PDF to text: {e}")
        return ""

def extract_text_from_image(image_path):
    ocr = PaddleOCR()
    result = ocr.ocr(image_path, cls=True)
    
    # Check the type of result and handle it appropriately
    if isinstance(result, list):
        text = ""
        for line in result:
            for word_info in line:
                text += word_info[1][0] + " "  # Concatenate detected words
        return text
    else:
        return "Error: Unexpected result format"

def get_assistant_response(query, text_content):
    """Sends a query to Gemini and retrieves a response using the provided text content."""
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyAJQICrt6u5D48UW-a6dHFphnI5zLpVWLo"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"Answer the following query based on the provided text content:\n\n{query}\n\nText Content:\n{text_content}"
                        }
                    ]
                }
            ]
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()
        generated_text = response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        if generated_text:
            return generated_text
        else:
            return "Gemini couldn't generate a response for your query."
    except requests.exceptions.RequestException as e:
        print(f"Error getting response from Gemini: {e}")
        return f"Error communicating with Gemini: {e}"
