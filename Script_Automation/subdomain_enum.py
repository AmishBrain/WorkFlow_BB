import subprocess

def run_subdomain_enum(domain):
    print(f"Enumerating subdomains for {domain}...")
    output_file = f"subdomain_results_{domain}.txt"
    command = f"sublist3r -d {domain} -o {output_file}"
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Subdomain enumeration completed. Results saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during subdomain enumeration: {e}")
