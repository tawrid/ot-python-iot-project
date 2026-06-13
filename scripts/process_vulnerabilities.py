import os
import json
import subprocess
import datetime

def run_trivy_scan():
    print("Running automated software composition analysis via Trivy...")
    cmd = ["trivy", "fs", "--format", "json", "--exit-code", "0", "--output", "trivy_report.json", "."]
    subprocess.run(cmd, check=True)

def evaluate_vulnerabilities():
    report_file = "trivy_report.json"
    if not os.path.exists(report_file):
        print("Error: Trivy report was not generated.")
        return

    with open(report_file, "r") as f:
        data = json.load(f)

    extracted_cves = []
    results = data.get("Results", [])
    for result in results:
        vulnerabilities = result.get("Vulnerabilities", [])
        for vuln in vulnerabilities:
            extracted_cves.append({
                "CVE_ID": vuln.get("VulnerabilityID"),
                "Package": vuln.get("PkgName"),
                "InstalledVersion": vuln.get("InstalledVersion"),
                "FixedVersion": vuln.get("FixedVersion"),
                "Severity": vuln.get("Severity"),
                "Description": vuln.get("Title", "No title available")
            })

    if extracted_cves:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        output_filename = f"vulns/cve-alert-{current_date}.json"
        
        os.makedirs("vulns", exist_ok=True)
        with open(output_filename, "w") as out_file:
            json.dump({"date": current_date, "vulnerabilities": extracted_cves}, out_file, indent=4)
        
        print(f"Alert: Critical vulnerabilities found. Recorded in {output_filename}")
        with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
            print("VULNS_FOUND=true", file=fh)
    else:
        print("Success: No active vulnerabilities found in project dependencies.")
        with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
            print("VULNS_FOUND=false", file=fh)

if __name__ == "__main__":
    run_trivy_scan()
    evaluate_vulnerabilities()
