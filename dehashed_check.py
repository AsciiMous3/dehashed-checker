import argparse
import csv
import sys
from time import sleep

import requests

parser = argparse.ArgumentParser(description="Search for leaked credentials using Dehashed API.")
parser.add_argument("-d", "--domain", help="Domain to search for")
parser.add_argument("-e", "--email", help="Email address to search for")
parser.add_argument("-a", "--auth", help="Dehashed API credentials (email and API key), separated by a comma")
parser.add_argument("-o", "--output", default="gee_die_ding_ander_naam.csv", help="Output CSV file name (Default: gee_die_ding_ander_naam.csv)")
parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose output")
args = parser.parse_args()

headers = {
    'Accept': 'application/json',
}

if args.domain:
    search_query = f"domain:{args.domain}"
elif args.email:
    search_query = f"email:{args.email}"
else:
    print("Error: Please provide either a domain or an email to search for.")
    sys.exit(1)

auth_email, auth_key = args.auth.split(",")

with open(args.output, "a") as data_file:
    csv_writer = csv.writer(data_file)

    head_keys = (["id", "email", "ip_address", "username", "password", "hashed_password", "name", "vin", "address", "phone", "database_name"])
    csv_writer.writerow(head_keys)

    print(f"Checking for {search_query}...")
    total_results = 0
    page = 1
    entries_per_page = 10000
    while True:
        response = requests.get(f"https://api.dehashed.com/search?query={search_query}&size={entries_per_page}&page={page}", headers=headers, auth=(auth_email.strip(), auth_key.strip()))
        data = response.json()

        if args.verbose:
            print(f"Server response status: {response.status_code} {response.reason}")

        if "entries" not in data:
            print(f"Error: API returned an unexpected response: {data}")
            break

        hash_data = data["entries"]
        if data["total"] > 0:
            total_results += len(hash_data)
            for entry in hash_data:
                csv_writer.writerow(entry.values())
            sleep(0.2)
        else:
            break

        if page * entries_per_page >= data["total"]:
            break
        else:
            page += 1

    print(f"Done! {total_results} results found.")
