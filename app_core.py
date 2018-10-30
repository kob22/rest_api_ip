from ip_validator import validator_ips
import requests

def get_northcountires_names(ips):
    if ips and len(ips) < 6:
        print(ips)
        validated_ips = validator_ips(ips)
        countries_unordered = {}
        for ip in validated_ips:
             print(ip)
             response = requests.get('https://ipvigilante.com/json/'+ip).json()
             if float(response['data']['latitude']) > 0:
                countries_unordered[response['data']['country_name']]  =0
        countries = sorted(countries_unordered)
        return countries
    return []