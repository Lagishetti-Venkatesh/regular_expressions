import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
            including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
            The panic selling prompted by the coronavirus has wiped £2.7tn off the value of\
            STOXX 600 shares since its all-time peak on 19 February."

result = re.search(r'\d{3}', string)
print(result)
print('='*200)

result = re.split(r"\d{2,}", string)
print(result)
print('='*200)

result = re.sub(r"[A-Z]{2,}", "INDEX", string, 2)
print(result)  # will just return the string with the replaced data.
print('='*200)

result = re.subn(r"[A-Z]{2,}", "Index", string, 2)
print(result)  # will return string with replaced data and the count of elements it replaced.
print('='*200)

result = re.search(r".+(\d\d).+(\d\d\d).", string)
print(result.groups())

