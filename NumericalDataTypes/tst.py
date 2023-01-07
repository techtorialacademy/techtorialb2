total_minutes=3456789
minute=1
one_hour=minute*60
one_day=one_hour* 24
one_year=one_day*365
count_of_years=total_minutes//one_year #print(count_of_years)

left_after_years_total_minutes= total_minutes%one_year #print (left_after_years)|
count_of_days=left_after_years_total_minutes // one_day
print (total_minutes, "minutes is approximatly", count_of_years, "years and", count_of_days, "dyas")



