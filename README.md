# Dehashed API Credential Search

This is a Python script that allows you to search for leaked credentials using the Dehashed API.

## Usage

To use this script, follow these steps:

1. Obtain Dehashed API credentials. You can sign up for an account at [Dehashed](https://dehashed.com/) and get your API key.
2. Run the script with the desired options. You can use the following command-line arguments:

- `-d`, `--domain`: Specify the domain to search for leaked credentials.
- `-e`, `--email`: Specify the email address to search for leaked credentials.
- `-a`, `--auth`: Provide your Dehashed API credentials (email and API key), separated by a comma.
- `-o`, `--output`: Specify the output CSV file name (Default: `rename.csv`).
- `-v`, `--verbose`: Enable verbose output for more detailed information.

Example command to search for a domain:

<pre><code>python3 ./dehashed_check.py -d example.com -a email@example.com,APIKEY1234567890 -v -o output.csv</code></pre>

3. The script will search for leaked credentials using the Dehashed API and store the results in a CSV file.

## Requirements

This script requires the following dependencies:

- Python 3.x
- requests (can be installed via `pip`)

## Disclaimer

**Important**: This script is intended for security research purposes only. By using this script, you agree to use it responsibly and in compliance with the terms and conditions outlined in Dehashed's legal documents, which can be found at [Dehashed Legal](https://www.dehashed.com/legal). Unauthorized and malicious use of this script is strictly prohibited.

The script is designed to interact with the Dehashed API to search for leaked credentials. It is your responsibility to ensure that you have the necessary permissions and legal rights to use the script and access the Dehashed service. Please refer to Dehashed's legal documents for more information on their terms of service, acceptable use policy, and any restrictions or limitations that may apply.

The author of this script assumes no liability for any unauthorized or inappropriate use of the script. It is recommended to review and comply with all applicable laws, regulations, and ethical guidelines when utilizing this script for security research purposes.

