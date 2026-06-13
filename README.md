# Secure Open-Source OT Python IoT Project

This repository establishes an Operational Technology (OT) deployment pipeline aligned with secure software supply chain requirements.

## Features
- **Continuous Integration Pipeline**: Automatically executes static analysis using `Bandit` and builds a complete machine-readable `CycloneDX SBOM`.
- **Daily Automated Vulnerability Triage**: Executes via GitHub cron schedules to scan project footprints using `Trivy`.
- **Automated Logging Engine**: Captures emerging dependency threats daily, committing automated tracking reports right into the repository history.
