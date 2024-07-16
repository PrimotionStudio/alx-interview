import re

txt = '225.56.25.224 - [2024-07-16 13:50:00.263930] "GET /projects/260 HTTP/1.1" 404 948'
list_of_log = txt.split(" ")
# ip
try:
    ip = list_of_log[0]
    hyphen = list_of_log[1]
    datetime_with_start_bracket = list_of_log[2]
    datetime_with_end_bracket = list_of_log[3]
    method_with_start_quote = list_of_log[4]
    path = list_of_log[5]
    protocol_with_end_quote = list_of_log[6]
    status_code = list_of_log[7]
    size = list_of_log[8]

    valid_status_code = [200, 301, 400, 401, 403, 404, 405, 500]

    # Check valid ip
    if re.match(r"[1-255]{1}\d?\d?\.[1-255]{1}\d?\d?\.[1-255]{1}\d?\d?", ip):  # 225.56.25.224
        print("IP is valid")
    # Check hyphen
    if hyphen == "-":
        print("Hyphen is valid")
    # Check valid datetime with start bracket
    if re.match(r"\[\d{4}-[01]\d-[0-3]\d", datetime_with_start_bracket):
        print("Datetime with start bracket is valid")
    # Check valid datetime with end bracket
    if re.match(r"[0-2]\d:[0-5]\d:[0-5]\d\.\d{6}", datetime_with_end_bracket):
        print("Datetime with end bracket is valid")
    if method_with_start_quote + " " + path + " " + protocol_with_end_quote == '"GET /projects/260 HTTP/1.1"':
        print("Method with start quote, path and protocol with end quote is valid")
    if int(status_code) in valid_status_code:
        print("Status code is valid")
    if re.match(r"^(0|[1-9][0-9]{0,2}|1000|1024)$", size):
        print("Size is valid")
except IndexError:
    print("Doesnt conform to rule")