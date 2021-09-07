#!/usr/bin/python3

print("content-type: text/html/json")
print()

import cgi
import requests
import xmltodict
import json



cmd= cgi.FieldStorage()
plate_num= cmd.getvalue("plate_number")
print(plate_num)


def get_vehicle_info(plate_num):
    r = requests.get("https://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={}&Tejashwini690".format(plate_num))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    df = json.loads(jdata)
    df1 = json.loads(df['Vehicle']['vehicleJson'])
    return df1

output = get_vehicle_info(plate_num)
plate_num_data=get_vehicle_info(plate_num)
print(output)





"""
#print('Access-Control-Allow-Origin:*')
"""
print("Car Owner        : ",plate_num_data["Owner"])
print("Car Model                    : ",plate_num_data["CarModel"]["CurrentTextValue"])
print("Car Company Name             : ",plate_num_data["CarMake"]["CurrentTextValue"])
print("Registration Year        : ",plate_num_data["RegistrationYear"])
print("Insurance Till Date      : ",plate_num_data["Insurance"])
print("Engine Number            : ",plate_num_data["EngineNumber"])
print("Fuel Type                : ",plate_num_data["FuelType"]["CurrentTextValue"])
print("Identification Number    : ",plate_num_data["VechileIdentificationNumber"])
print("Registration Date        : ",plate_num_data["RegistrationDate"])
print("Fitness Till Date        : ",plate_num_data["Fitness"])
print("Registration Location    : ",plate_num_data["Location"])
