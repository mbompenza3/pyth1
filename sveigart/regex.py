import re
phReg=re.compile(r'\d{3}-\d{3}-\d{4}')
phReg1=re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo=phReg1.search('my number: 415-555-4242')
# print(mo.groups())
# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))

# ? neobyazat
batReg=re.compile(r'Bat(wo)?man')
m1=batReg.search('The adventures of Batman')
m2=batReg.search('The adventures of Batwoman')

print(m1.group())
print(m2.group())