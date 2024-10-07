import sys
from urllib.parse import urlparse
from nmap_scan import run_nmap_scan
from subdomain_enum import run_subdomain_enum
from zap_scan import run_zap_scan


def main(target_url, run_zap=True, run_nmap=True, run_subdomains=True):
    print("Running security scans...")

    try:
        parsed_url = urlparse(target_url)
        if not parsed_url.scheme or not parsed_url.netloc:
            print("Invalid URL provided. Please include the scheme (http or https).")
            sys.exit(1)

        if parsed_url.scheme not in ['http', 'https']:
            print("URL must start with http:// or https://")
            sys.exit(1)

        if run_zap:
            run_zap_scan(target_url)
        if run_nmap:
            run_nmap_scan(parsed_url.netloc)
        if run_subdomains:
            run_subdomain_enum(parsed_url.netloc)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run security scans on a target URL.')
    parser.add_argument('target_url', help='The target URL to scan.')
    parser.add_argument('--no-zap', action='store_false', help='Disable ZAP scan.')
    parser.add_argument('--no-nmap', action='store_false', help='Disable Nmap scan.')
    parser.add_argument('--no-subdomains', action='store_false', help='Disable subdomain enumeration.')

    args = parser.parse_args()
    main(args.target_url, run_zap=args.no_zap, run_nmap=args.no_nmap, run_subdomains=args.no_subdomains)