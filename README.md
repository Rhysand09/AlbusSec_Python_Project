# Wi-Fi Deauthentication Attack Tool

## Description

This tool sends de-authentication packets to a target device in order to disrupt its Wi-Fi connection. This type of attack is known as a de-authentication attack or deauth attack. It leverages vulnerabilities in the Wi-Fi protocol to force devices to disconnect from a network.

**Note:** This tool is intended for educational purposes and should only be used in a legal and controlled environment. Unauthorized use of this tool is illegal and unethical.

## Requirements

- Python 3.x
- Scapy library
- A wireless network interface card (NIC) capable of packet injection (e.g., Alfa AWUS036NHA)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the Scapy library using pip:

    ```sh
    pip install scapy
    ```

## Usage

1. Save the script to a file, for example, `deauth_attack.py`.
2. Open a terminal and navigate to the directory where the script is saved.
3. Run the script with the necessary arguments. You must provide the target MAC address, the access point MAC address, and the network interface to use. For example:

    ```sh
    sudo python3 deauth_attack.py -t XX:XX:XX:XX:XX:XX -a YY:YY:YY:YY:YY:YY -i wlan0
    ```

    Replace:
    - `XX:XX:XX:XX:XX:XX` with the target device's MAC address
    - `YY:YY:YY:YY:YY:YY` with the access point's MAC address
    - `wlan0` with the appropriate network interface on your system

## Example

```sh
sudo python3 deauth_attack.py -t 00:11:22:33:44:55 -a 66:77:88:99:AA:BB -i wlan0
```

# Web Crawler Tool

## Description

This web crawler tool recursively navigates web pages starting from a specified URL and stores the retrieved content into files. The tool filters JavaScript and PHP files into separate directories while organizing other file types into distinct paths within the file system.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `argparse` library

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries using pip:

    ```sh
    pip install requests beautifulsoup4 argparse
    ```

## Usage

1. Save the script to a file, for example, `web_crawler.py`.
2. Open a terminal and navigate to the directory where the script is saved.
3. Run the script with the starting URL and the output directory as arguments. For example:

    ```sh
    python3 web_crawler.py https://example.com /path/to/output
    ```

    Replace:
    - `https://example.com` with the starting URL for the web crawler
    - `/path/to/output` with the directory where the retrieved content will be stored

## Example

```sh
python3 web_crawler.py https://example.com /home/user/web_content

