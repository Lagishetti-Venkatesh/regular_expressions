import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \n \
            including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\n\
            The panic selling prompted by the coronavirus has wiped £2.7tn off the value of\
            STOXX 600 shares since its all-time peak on 19 February."


result = re.search(r".+", string)  # dot matches with any alphanumeric and special characters except newline
print(result.group())
print('=' * 200)

result = re.search(r"^\w{3}", string, flags=re.I & re.M)
print(result)
print('=' * 200)


result = re.findall(r"(\d{2,})\W$", string, re.M)
print(result)
print('=' * 200)