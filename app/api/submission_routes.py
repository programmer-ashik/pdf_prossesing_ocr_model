
from fastapi import APIRouter, Depends, File, UploadFile
from app.utils.file_save import save_file_locally
from app.utils.check_pdf_file_type import check_file_type
from app.utils.digital_pdf_process import process_digital_pdf


router=APIRouter(
    prefix="/submissions",
    tags=["submissions"]
)
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)): #File(...) means in this route file must be send
    saved_path = save_file_locally(file)
    file_type = check_file_type(saved_path)
    file_name=file.filename or 'unknown File'
    if file_type == "DIGITAL_PDF":
        # আপনার বর্তমান pdfplumber লজিক এখানে চালান
        return await process_digital_pdf(saved_path, file_name)
        
    elif file_type == "SCANNED_PDF" or file_type == "IMAGE":
        # এখানে আমরা ভবিষ্যতে OCR বা Gemini Vision লজিক যোগ করব
        return {"status": "OCR_REQUIRED", "message": "This is a scanned file or image. Need OCR."}
        
    else:
        return {"error": "Unsupported or corrupted file type."}
 

    