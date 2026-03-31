from pypdf import PdfReader

def extractpdf(pdf_doc): # module to load and extract text from the PDF
    try:
        pdf = PdfReader(pdf_doc)
        
        raw_text = ''
        for index, page in enumerate(pdf.pages):  #  by uindex, page from the loaded doc
            text = page.extract_text() # from page it will extract text alone 
            if text:
                raw_text += text
        
        return raw_text
    except Exception as e:
        return f'Error in the pdf'
                