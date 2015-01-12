import re

# Function to validate ip address
def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

# Function to check hostname
def is_valid_hostname(hostname):
    res = {}
    a = hostname.split('.')
    if "localhost" in a or "localhost." in a:
        res["result"] = False
        return res
    if a[0].isdigit():
        res["result"] = False
        return res
    if len(a) > 2:
        if a[0].isdigit() or a[1].isdigit():
            res["result"] = False
            return res
    if len(a) > 3:
        if a[0].isdigit() or a[1].isdigit() or a[2].isdigit():
            res["result"] = False
            return res
    if len(a) > 4:
        res["result"] = False
        return res
    elif len(a) <= 3:
        res["token_type"] = 'PQDN'
    else:
        res["token_type"] = 'FQDN'
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    rsp = all(allowed.match(x) for x in hostname.split("."))
    res["result"] = rsp
    return res


