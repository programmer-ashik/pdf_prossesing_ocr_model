def structure_dynamic_table(raw_table):
    if not raw_table or len(raw_table) < 2:
        return []

    headers = []
    for i, h in enumerate(raw_table[0]):
        header_text = str(h).replace("\n", " ").strip() if h else f"col_{i}"
        headers.append(header_text)
    
    final_data = []
    # ২. Forward Fill এর জন্য একটি লিস্ট তৈরি যা প্রতিটি কলামের শেষ ভ্যালু মনে রাখবে
    last_values = [None] * len(headers)

    # ৩. ডাটা রো প্রসেস করা (হেডার বাদ দিয়ে)
    for row in raw_table[1:]:
        if not any(row): continue  # খালি রো বাদ
        
        current_row_dict = {}
        for i, cell in enumerate(row):
            if i >= len(headers): break # যদি রো-তে হেডারের চেয়ে বেশি ডাটা থাকে
            
            val = str(cell).replace("\n", " ").strip() if cell else None
            
            # ৪. Forward Fill লজিক: 
            # যদি বর্তমান সেল খালি থাকে এবং এটি প্রথম বা দ্বিতীয় কলাম হয় (যেখানে সাধারণত মার্জ থাকে)
            # তবে আগের ভ্যালুটি ব্যবহার করবে।
            if val:
                last_values[i] = val # type: ignore
            else:
                # শুধুমাত্র প্রথম ১-২টি কলামে forward fill করা নিরাপদ, 
                # কারণ ডাটা কলামে (Numbers) None মানে সেটি ০ হতে পারে।
                if i < 2: 
                    val = last_values[i]
            
            current_row_dict[headers[i]] = val if val else ""
            
        final_data.append(current_row_dict)
            
    return final_data