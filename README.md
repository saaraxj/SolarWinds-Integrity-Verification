# Software Supply Chain Integrity Verification Demo

Educational proof-of-concept for a SolarWinds Orion case study. Python 3 required, no external libraries.

## Run (Windows PowerShell or VS Code terminal)

Open this folder in VS Code, then run each command separately:

```powershell
python integrity_demo.py setup
python integrity_demo.py verify
python integrity_demo.py tamper
python integrity_demo.py verify
```

If `python` is not recognized on Windows, use `py` instead.

**Important:** The last verification intentionally rejects the tampered file and exits with code 1. That is expected, not a crash.

Run `python integrity_demo.py setup` to reset the demonstration and restore the original file.

## What to screenshot

- First verification: `PASS: integrity verified. Deployment allowed in this demo.`
- After tampering: `BLOCKED: integrity mismatch. Deployment denied in this demo.`

## Security limitations

- The baseline is *assumed trusted*. If an attacker compromises both the update and the baseline manifest, hashing will not detect the attack.
- The separate trusted_baseline folder is a demonstration of logical separation, not actual access-control enforcement; production systems need independently protected baselines, authenticated provenance and secure build pipelines.
- A matching hash only proves consistency with the baseline, not absence of malicious code.
- This demo does not replicate the SUNBURST malware or SolarWinds environment.
