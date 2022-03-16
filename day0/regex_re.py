import re
log = "some text with process id[897342]: and error message"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
