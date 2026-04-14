
from fastapi import APIRouter, Depends, File, UploadFile
from sqlmodel import Session
from app.core.database import get_session
from app.models.submission_model import FinancialSubmissionModel
from app.utils.file_save import save_file_locally
from app.utils.extract_file import extract_tables_from_pdf
from app.utils.stracture_table import structure_dynamic_table
router=APIRouter(
    prefix="/submissions",
    tags=["submissions"]
)
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    saved_path = save_file_locally(file)
    all_formatted_tables = [] # এটি সবসময় লুপের বাইরে ডিফাইন করবেন

    try:
        raw_pdf_data = extract_tables_from_pdf(saved_path)
        
        # পি ল্যান্সের ওয়ার্নিং দূর করতে একটি চেক যোগ করুন
        if not raw_pdf_data:
            return {"message": "No tables found in the PDF", "data": []}

        for entry in raw_pdf_data:
            # এখানে 'entry' এখন সেইফলি ব্যবহার করা যাবে
            raw_table = entry.get("table_data", [])
            structured_data = structure_dynamic_table(raw_table)
            
            all_formatted_tables.append({
                "page": entry.get("page", 0),
                "headers": list(structured_data[0].keys()) if structured_data else [],
                "data": structured_data
            })

        return {
            "file_name": file.filename,
            "total_tables": len(all_formatted_tables),
            "extracted_content": all_formatted_tables
        }
        
    except Exception as e:
        return {"error": str(e)}