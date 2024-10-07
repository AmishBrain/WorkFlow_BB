import subprocess
import os


def run_zap_scan(target_url):
    zap_path = r"C:\Program Files\ZAP\Zed Attack Proxy\zap.bat"
    if not os.path.exists(zap_path):
        print(f"OWASP ZAP executable not found at {zap_path}")
        return

    command = [
        zap_path,
        '-daemon',
        '-newsession', 'zap_session',
        '-quickurl', target_url,
        '-quickout', 'zap_report.xml',
        '-dir', r"C:\Program Files\ZAP\Zed Attack Proxy",
        '-config', 'api.disablekey=true'
    ]

    try:
        print("Starting ZAP scan...")
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("ZAP is running. Waiting for the scan to complete...")
        if result.stderr:
            print("Error during ZAP scan:", result.stderr)
    except subprocess.TimeoutExpired:
        print("ZAP scan timed out.")
    except Exception as e:
        print(f"Error during ZAP scan: {e}")
