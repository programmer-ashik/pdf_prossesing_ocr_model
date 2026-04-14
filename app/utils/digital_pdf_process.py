from app.utils.extract_file import extract_tables_from_pdf
from app.utils.stracture_table import structure_dynamic_table
async def process_digital_pdf(saved_path, file_name:str):
    print(saved_path)
    all_formatted_tables = []
    try:
        raw_pdf_data = extract_tables_from_pdf(saved_path)
        
        # পি ল্যান্সের ওয়ার্নিং দূর করতে একটি চেক যোগ করুন
        if not raw_pdf_data:
            return {"message": "No tables found in the PDF", "data": []}

        for entry in raw_pdf_data:
            
            raw_table = entry.get("table_data", [])
            structured_data = structure_dynamic_table(raw_table)
            
            all_formatted_tables.append({
                "page": entry.get("page", 0),
                "headers": list(structured_data[0].keys()) if structured_data else [],
                "data": structured_data
            })

        return {
            "file_name": file_name,
            "total_tables": len(all_formatted_tables),
            "extracted_content": all_formatted_tables
        }
        
    except Exception as e:
        return {"error": str(e)}