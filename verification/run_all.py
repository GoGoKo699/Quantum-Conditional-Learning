"""Run the finite checks and compare generated JSON with stored baselines."""

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys


DIRECTORY = Path(__file__).resolve().parent
ABS_TOL = 1e-10
REL_TOL = 1e-12


def compare(actual, expected, location="$"):
    """Compare structure and discrete data exactly, with tolerance for floats."""
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or actual.keys() != expected.keys():
            raise AssertionError(f"{location}: object keys differ")
        for key, value in expected.items():
            compare(actual[key], value, f"{location}.{key}")
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise AssertionError(f"{location}: list lengths differ")
        for index, (observed, reference) in enumerate(zip(actual, expected)):
            compare(observed, reference, f"{location}[{index}]")
    elif isinstance(expected, float):
        if (
            type(actual) not in (int, float)
            or not math.isfinite(actual)
            or not math.isclose(actual, expected, rel_tol=REL_TOL, abs_tol=ABS_TOL)
        ):
            raise AssertionError(
                f"{location}: observed {actual!r}, expected {expected!r}"
            )
    elif type(actual) is not type(expected) or actual != expected:
        raise AssertionError(
            f"{location}: observed {actual!r}, expected {expected!r}"
        )


def main():
    if not __debug__:
        raise RuntimeError("Verification requires assertions; do not use python -O.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DIRECTORY / "actual",
        help="Directory for generated JSON (default: verification/actual).",
    )
    args = parser.parse_args()
    output_dir = args.output_dir.expanduser().resolve()
    expected_dir = (DIRECTORY / "expected").resolve()
    if output_dir == expected_dir or expected_dir in output_dir.parents:
        parser.error("Generated output must not be written inside expected/.")
    output_dir.mkdir(parents=True, exist_ok=True)

    suites = [
        ("verify_converse.py", "converse.json", "3 Gram, 3 quotient/frame, 4 one-copy cases"),
        ("verify_synthesis.py", "synthesis.json", "1 exhaustive design, 2 physical, 2 covariance cases"),
    ]
    for script, filename, summary in suites:
        output = output_dir / filename
        baseline = expected_dir / filename
        print(f"Running {script}", flush=True)
        subprocess.run(
            [sys.executable, str(DIRECTORY / script), "--output", str(output)],
            cwd=DIRECTORY,
            check=True,
        )
        actual = json.loads(output.read_text())
        expected = json.loads(baseline.read_text())
        compare(actual, expected, filename)
        print(f"PASS {script}: {summary}; baseline matched", flush=True)

    print(
        f"PASS all checks: exact discrete comparison; "
        f"float abs_tol={ABS_TOL:g}, rel_tol={REL_TOL:g}",
        flush=True,
    )
    print(f"Generated JSON: {output_dir}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
