# Python-Phase1-Practice.py
# Phase 1 practical milestone:Take a real SaaS API, call it from Python, authenticate, send a request, 
# receive JSON, parse it, handle errors, and turn the result into something useful.

# End Point: https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Cardiovascular+Disease&city=San+Francisco&state=CA&limit=10
# 1. Call the NPPES API from Python (requests library)

import requests
# url = "https://modalflo.com"
# url = "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Cardiovascular+Disease&city=San+Francisco&state=CA&limit=10"
url = "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Cardiovascular+Disease&city=Irvine&state=CA&limit=10"
# url = "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Cardiovascular+Disease&city=Cactus&state=TX&limit=10"
# 2. Authenticate — N/A for this API (good for a first practice, one less thing to debug)

# 6. Handle errors — what if the city has zero results? What if the API is down?
try:
    # 3. Send a GET request with query parameters (specialty, city, state)
    response = requests.get(url, timeout = 10)
    
# 6.1 Network Error    
except requests.exceptions.RequestException as e:
    print("Network request failed:", e)
    data = None # don't process the data.

else:
    print("Status Code: ", response.status_code)
    if response.status_code == 200:
        try:
             data = response.json()

        #6.2 JSON Parsing Error
        except ValueError as e:
            print("JSON parsing filed: ", e)
            data = None

    # 6.3 HTTP Error
    else:
        print(f"Request failed with status code: {response.status_code}")
        data = None


# Code	Meaning
# 200	Success — everything worked
# 400	Bad request — you sent something malformed
# 401	Unauthorized — missing/invalid authentication
# 404	Not found — wrong URL/endpoint
# 429	Too many requests — rate limited
# 500	Server error — the API itself broke, not your fault

# 5. Parse it — extract provider names, NPI numbers, addresses, specialties
if data is not None:
    print("data.key()", data.keys()) # Prints dict_keys(['result_count', 'results'])
    # response          # the whole HTTP response wrapper (status code, headers, raw body, etc.)
    # response.json()    # ONLY the body, converted from JSON text into a Python dict


    print("")
    print(f"data['result_count'], {data['result_count']}")
    print(f"data['result_count'], {data["result_count"]}")
    print(f"len(data['results']), {len(data['results'])}")

    if data["result_count"] > 0:
        print("")
        print("Zooming in one doctor")
        first_doctor = data["results"][0]
        print(first_doctor.keys())
        print("")
        print("Basic fields")
        print(first_doctor["basic"])
        print("")
        print("First Name: ", first_doctor["basic"]["first_name"])
        print("Last Name: ", first_doctor["basic"]["last_name"])
        print("Credential: ", first_doctor["basic"]["credential"])
        print("City: ", first_doctor["addresses"][0]["city"])
        print("State: ", first_doctor["addresses"][0]["state"])


        print("")
        for doctor in data["results"][:9]:
            basic = doctor["basic"]
            print("First Name:", basic.get("first_name", "")) #6.4 Missing Field Error
            print("Last Name:", basic.get("last_name", ""))
            print("Credential:", basic.get("credential", ""))

            addresses = doctor.get("addresses", [])
            if len(addresses) > 0:
                address = addresses[0]
                print("City: ", address.get("city", ""))
                print("State: ", address.get("state", ""))
            else:
                print("City:")
                print("State:")

            print("NPI Number: ", doctor.get("number", ""))

            for taxonomy in doctor.get("taxonomies", []):
                print("Speciality: ", taxonomy.get("desc", ""))
            print("")
    else:
        print("No doctors found for this search")

# 6.4 No Data
else:
    print("No data available. Cannot process safely.")

# 7. Turn it into something useful — e.g., print a clean formatted list, or save to CSV using pandas (Module 2!), 
# or even build a simple "find a specialist near me" lookup tool
print("")
print("Cardiovascular Specialists")
print("========================================")

for i, doctor in enumerate(data["results"], start=1):

    basic = doctor.get("basic", [])
    addresses = doctor.get("addresses", [])

    first_name = basic.get("first_name", "")
    last_name = basic.get("last_name", "")
    credential = basic.get("credential", "")
    npi = doctor.get("number", "")

    if addresses:
        city = addresses[0].get("city", "")
        state = addresses[0].get("state", "")
    else:
        city = ""
        state = ""

    print(f"{i}.{first_name} {last_name}, {credential}")
    print(f"    Speciality: Cardiovasucular Disease")
    print(f"    Location:   {city}, {state}")
    print(f"    NPI:        {npi}")
    print("")
