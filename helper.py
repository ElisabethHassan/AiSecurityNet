import PyPDF2
import json
from flask import request
import re

def pdf_to_json(pdf_file):
    try:
        # Read the PDF file
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)
        extracted_data = []

        # Extract text from each page of the PDF
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            extracted_data.append(page.extract_text())

        # Convert extracted data to JSON format
        json_data = json.dumps(extracted_data)

        # Define the output file path for JSON data
        json_output_path = 'path_to_output_json_file.json'

        # Write JSON data to the output file
        with open(json_output_path, 'w') as json_file:
            # json_file.write(json_data)
            return json_data
    except Exception as e:
        # Print error message if an exception occurs
        print("The following error occurred: " + str(e))


def pdf(file_path):
    try:
        # Read the PDF file
        with open(file_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)

            # Get the number of pages in the PDF
            num_pages = len(pdf_reader.pages)
            extracted_data = []

            # Extract text from each page of the PDF
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                extracted_data.append(page.extract_text())

            # Convert extracted data to JSON format
            json_data = json.dumps(extracted_data)

            # Define the output file path for JSON data
            json_output_path = 'path_to_output_json_file.json'

            # Write JSON data to the output file
            with open(json_output_path, 'w') as json_file:
                json_file.write(json_data)

            # Convert JSON data back to a list, then join the list elements to form a string
            text_data = ' '.join(json.loads(json_data))
            return text_data
    except Exception as e:
        # Print error message if an exception occurs
        print("The following error occurred: " + str(e))
        

# The doc_to_json function and the doc function are removed

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'DFJASLJKDLASJLKF'
    app.run(debug=True, host='0.0.0.0', port='5000')
