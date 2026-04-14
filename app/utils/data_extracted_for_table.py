def clean_extracted_table(raw_table):
    """
    পিডিএফ থেকে পাওয়া Raw টেবিলকে ক্লিন করে JSON ফরম্যাটে রূপান্তর করে।
    """
    if not raw_table or len(raw_table) < 2:
        return []

    # প্রথম রো-কে হেডার হিসেবে ধরছি (যেমন: Date, Description, Amount)
    headers = [str(h).replace("\n", " ").strip() for h in raw_table[0] if h is not None]
    
    cleaned_rows = []
    
    # দ্বিতীয় রো থেকে ডাটা রিড করা শুরু
    for row in raw_table[1:]:
        # যদি রো-তে অন্তত কিছু ডাটা থাকে (সব None নয়)
        if any(cell is not None for cell in row):
            # হেডার এবং সেলের ডাটাকে ম্যাপ করা
            row_dict = {}
            for i, cell in enumerate(row):
                if i < len(headers):
                    key = headers[i]
                    value = str(cell).replace("\n", " ").strip() if cell is not None else ""
                    row_dict[key] = value
            cleaned_rows.append(row_dict)
            
    return cleaned_rows