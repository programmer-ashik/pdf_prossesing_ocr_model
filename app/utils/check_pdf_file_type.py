import pdfplumber

def check_file_type(file_path: str):
    # ১. যদি ফাইলটি ইমেজ হয়
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        return "IMAGE"

    # ২. পিডিএফ চেক করা
    try:
        with pdfplumber.open(file_path) as pdf:
            total_text = ""
            # প্রথম ২-৩ পেজ চেক করলেই বোঝা যায় এটি ডিজিটাল নাকি স্ক্যানড
            for page in pdf.pages[:3]:
                text = page.extract_text()
                if text:
                    total_text += text
            
            # যদি টেক্সট পাওয়া যায়, তবে এটি ডিজিটাল
            if len(total_text.strip()) > 100:
                return "DIGITAL_PDF"
            else:
                return "SCANNED_PDF"
    except Exception:
        return "CORRUPTED_OR_LOCKED"