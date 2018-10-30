def validate_address_ip(ip):
    ip_block = ip.split('.')

    if len(ip_block) !=4:
        return False
    new_ip = ''
    for digit in ip_block:
        if digit.isdigit():
            digit=int(digit)
            if digit >=0 and digit < 256:
                new_ip = new_ip + str(digit) + '.'
            else:
                return False
        else:
            return False

    return new_ip[:-1]


def validator_ips(list_ip):
    validateed_ips = []
    for ip in list_ip:
        validate_ip = validate_address_ip(ip)
        if validate_ip:
            validateed_ips.append(ip)

    return validateed_ips