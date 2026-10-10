"""Supply-chain artifact integrity demonstration.

A trusted manifest is created in a protected directory outside the release folder.
The verifier compares SHA-256 digests against that baseline and blocks a changed file.
"""
from pathlib import Path
import hashlib
import json
import argparse

ROOT = Path(__file__).resolve().parent
RELEASE = ROOT / 'release'
TRUST = ROOT / 'trusted_baseline'
ARTIFACT = RELEASE / 'orion_update_demo.txt'
MANIFEST = TRUST / 'manifest.json'


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(65536), b''):
            digest.update(chunk)
    return digest.hexdigest()


def setup() -> None:
    RELEASE.mkdir(exist_ok=True)
    TRUST.mkdir(exist_ok=True)
    ARTIFACT.write_text('SolarWinds Orion educational demo update\nVersion: 1.0\n', encoding='utf-8')
    baseline = {'artifact': ARTIFACT.name, 'sha256': sha256_file(ARTIFACT)}
    MANIFEST.write_text(json.dumps(baseline, indent=2) + '\n', encoding='utf-8')
    print('Trusted baseline initialized (simulation only).')
    print(f'Artifact: {ARTIFACT.name}')
    print(f'Expected SHA-256: {baseline["sha256"]}')


def verify() -> bool:
    if not MANIFEST.is_file():
        print('BLOCKED: trusted baseline missing. Run setup first.')
        return False
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if manifest.get('artifact') != ARTIFACT.name or not ARTIFACT.is_file():
        print('BLOCKED: artifact missing or manifest mismatch.')
        return False
    expected = manifest['sha256']
    actual = sha256_file(ARTIFACT)
    print(f'Expected SHA-256: {expected}')
    print(f'Actual SHA-256:   {actual}')
    if actual == expected:
        print('PASS: integrity verified. Deployment allowed in this demo.')
        return True
    print('BLOCKED: integrity mismatch. Deployment denied in this demo.')
    return False


def tamper() -> None:
    if not ARTIFACT.is_file():
        print('Artifact missing. Run setup first.')
        return
    with ARTIFACT.open('a', encoding='utf-8') as file:
        file.write('UNAUTHORIZED CHANGE: simulated build tampering\n')
    print('Simulated unauthorized modification added to release artifact.')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['setup', 'verify', 'tamper'])
    args = parser.parse_args()
    if args.command == 'setup':
        setup()
    elif args.command == 'tamper':
        tamper()
    else:
        raise SystemExit(0 if verify() else 1)


if __name__ == '__main__':
    main()
