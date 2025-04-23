def generate_unique_digit_rc_post_2000():
    from itertools import permutations
    
    valid_numbers = []
    digits = '0123456789'
    
   
    for year in range(1, 24):
        year_str = f"{year:02d}"
        
        
        for month in range(1, 13):
            month_str = f"{month:02d}"
            
           
            if month == 2:
                max_day = 28
            elif month in [4, 6, 9, 11]:
                max_day = 30
            else:
                max_day = 31
                
            
            for day in range(1, max_day + 1):
                day_str = f"{day:02d}"
                
               
                date_part = year_str + month_str + day_str
                
                
                if len(set(date_part)) == 6:
               
                    remaining_digits = [d for d in digits if d not in date_part]
                    
                    
                    for suffix in permutations(remaining_digits, 4):
                        suffix_str = ''.join(suffix)
                        full_number = date_part + suffix_str
                        
                       
                        if int(full_number) % 11 == 0:
                         
                            rc = f"{date_part[:2]}{date_part[2:4]}{date_part[4:6]}/{suffix_str}"
                            valid_numbers.append(rc)
    
    return valid_numbers


valid_rc_numbers = generate_unique_digit_rc_post_2000()


print(f"Celkový počet nalezených rodných čísel: {len(valid_rc_numbers)}")
if valid_rc_numbers:
    print("\nUkázka prvních 20 rodných čísel:")
    for rc in valid_rc_numbers[:20]:
        print(rc)