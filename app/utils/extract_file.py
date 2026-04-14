import pdfplumber

def extract_tables_from_pdf(file_path: str):
    settings = {
        "vertical_strategy": "lines", # বর্ডার লাইন অনুযায়ী কলাম ভাগ করবে
        "horizontal_strategy": "lines",
        "snap_tolerance": 3,
    }
    extracted_data = []
    tables = [] 
    page_num = 0 
    try:
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                # tables = page.extract_tables()
                tables = page.extract_tables(table_settings=settings)
                
                for table in tables:
                    if table:
                        extracted_data.append({
                            "page": page_num + 1,
                            "table_data": table
                        })
    except Exception as e:
        print(f"Error opening PDF: {e}")
                    
    return extracted_data