# main.py — entry program for "Sum up 21 November's world news in one image".
# Stdlib only, no network. Copies the broadsheet (entry.png, drawn in-session
# from verified Saturday 21 November 2026 reporting) to /output/entry.png.
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out = os.environ.get("OUTPUT_PATH", "/output/entry.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    shutil.copyfile(src, out)
    # Verify the copy is complete: source and destination must match in size.
    if os.path.getsize(src) != os.path.getsize(out):
        raise SystemExit("entry.png copy size mismatch")
    print(f"wrote {out}: {os.path.getsize(out)} bytes")


if __name__ == "__main__":
    main()
