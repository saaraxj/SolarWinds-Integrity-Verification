# Software Supply Chain Integrity Verification System

## Project overview
An educational Python prototype prepared for the **SolarWinds Orion software supply chain attack** case study. It generates a trusted SHA-256 baseline, checks an artifact against that baseline, simulates an unauthorized file change, and rejects the modified artifact.

**GitHub repository:** `https://github.com/saaraxj/SolarWinds-Integrity-Verification`


## Files in this submission
- `integrity_demo.py` — complete Python source code
- `release/orion_update_demo.txt` — sample artifact
- `trusted_baseline/manifest.json` — demonstration reference SHA-256 hash
- `build_exe_windows.bat` — creates a Windows EXE using PyInstaller
- `requirements-build.txt` — optional package needed **only** to build the EXE
- `README.md` — setup, commands, limitations, and repository link field

## Option A — Run from Python source (Windows / VS Code)
**Requirements:** Windows, macOS, or Linux, and Python 3.9+; no third-party Python packages are needed to run the source.

Open a terminal in the folder containing `integrity_demo.py`, then run:

```powershell
python integrity_demo.py setup
python integrity_demo.py verify
python integrity_demo.py tamper
python integrity_demo.py verify
```

On Windows, use `py` instead of `python` if needed.

Expected behavior:
1. Setup creates a fresh sample file and records its baseline hash.
2. First verify prints `PASS: integrity verified. Deployment allowed in this demo.`
3. Tamper appends one harmless line to the file.
4. Final verify prints `BLOCKED: integrity mismatch. Deployment denied in this demo.`

**Important:** The final verification exits with status code `1` on purpose: an altered file fails validation. To reset the sample, run `python integrity_demo.py setup` again.

## Option B — Build and run the Windows EXE
A Windows `.exe` must be built **on Windows**. The Windows executable is included in the submission ZIP. It can also be rebuilt using the provided build script. On a Windows PC with Python installed:

1. Double-click `build_exe_windows.bat` (or run it from Command Prompt).
2. The batch file installs PyInstaller if necessary and produces `dist\integrity_demo.exe`.
3. Open a terminal in the `dist` folder and run:

```powershell
.\integrity_demo.exe setup
.\integrity_demo.exe verify
.\integrity_demo.exe tamper
.\integrity_demo.exe verify
```

The EXE creates its `release` and `trusted_baseline` folders next to the EXE. A terminal is required because the application is command-line based. If your instructor requires an EXE inside the uploaded ZIP, **copy `dist\integrity_demo.exe` into the main submission folder and create a new ZIP** before uploading. Ensure its size stays under 100 MB.

## Evidence for case study
Capture actual screenshots of:
- the original file passing verification (`PASS`)
- the tampering command
- the modified file failing verification (`BLOCKED`)

## Security scope and limitations
- This is a non-malicious simulation: it does not run SUNBURST or recreate the original breach.
- The baseline JSON is only logically separate from the release folder, not cryptographically authenticated or access-controlled.
- A matching hash shows equality with the reference; it **does not** prove a file is safe or malware-free.
- If a build process or the baseline is compromised before hash generation, the attack may not be detected.
- `Deployment allowed/denied` describes a decision printed by the demo; the program does not control a real CI/CD deployment system.
