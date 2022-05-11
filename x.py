import re

s = 'sasadasdsadasd324sdfsdfdsfdsfdsf'

d = re.findall('[0-9]', s)

st = ''.join([str(x) for x in d])
st = int(st)
print(st)