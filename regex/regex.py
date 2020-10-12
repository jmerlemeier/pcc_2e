import re

phone_num1 = '206-555-2452'
phone_num2 = '425-555-6939'
phone_num3 = '818-555-2220'
phone_num4 = '808-555-1075'

sea_area_code_regex = r'\d{3}-5{3}-\S*'

print(re.search(sea_area_code_regex, phone_num1))

# https://regex101.com/ 