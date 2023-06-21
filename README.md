# Dehashed API Credential Search

This is a Python script that allows you to search for leaked credentials using the Dehashed API.

## Usage

To use this script, follow these steps:

1. Obtain Dehashed API credentials. You can sign up for an account at [Dehashed](https://dehashed.com/) and get your API key.
2. Run the script with the desired options. You can use the following command-line arguments:

- `-d`, `--domain`: Specify the domain to search for leaked credentials.
- `-e`, `--email`: Specify the email address to search for leaked credentials.
- `-a`, `--auth`: Provide your Dehashed API credentials (email and API key), separated by a comma.
- `-o`, `--output`: Specify the output CSV file name (Default: `gee_die_ding_ander_naam.csv`).
- `-v`, `--verbose`: Enable verbose output for more detailed information.

Example command to search for a domain:

<pre><code>python3 ./dehashed_check.py -d example.com -a email@example.com,APIKEY1234567890 -v -o output.csv</code></pre>

3. The script will search for leaked credentials using the Dehashed API and store the results in a CSV file.

## Requirements

This script requires the following dependencies:

- Python 3.x
- requests (can be installed via `pip`)

## License

This project is licensed under the [MIT License](LICENSE).
