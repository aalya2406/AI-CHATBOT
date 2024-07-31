# AI-CHATBOT

This project is a web application designed to analyze and interact with document files using AI. It allows users to upload PDF, text, and image files, processes the content, and provides responses based on user queries.

Key Features:

Upload and save PDF, text, and image files. Extract text from PDFs and images using OCR (Optical Character Recognition). Interact with the uploaded content using the Gemini AI model to generate responses based on user queries.

Tools and Technologies:

Streamlit: For building the web application interface. PyPDF2: For extracting text from PDF files. Pillow (PIL) and pytesseract: For extracting text from images. Requests: For making HTTP requests to the Gemini API. Gemini API: For generating AI responses based on the content of the uploaded files.

How to Use:

Upload a PDF, text, or image file. Process the file to extract text. Enter a query to interact with the content. Get responses generated by the Gemini AI model. Setup Instructions:

Clone the repository: git clone

Install the required dependencies: pip install -r requirements.txt Run the Streamlit application: streamlit run app.py API Key Configuration:

Obtain an API key from the Gemini API and replace it in the functions.py file. For more details on how the application works and additional configuration, refer to the documentation in the repository.
