import os
from magic_db import MAGIC_NUMBERS


def detect_type(filepath):

    try:

        with open(filepath, "rb") as f:
            header = f.read(64)

        for filetype, signatures in MAGIC_NUMBERS.items():

            for sig in signatures:

                if header.startswith(sig):
                    return filetype

                if sig == b"ftyp" and b"ftyp" in header:
                    return filetype

        return "unknown"

    except Exception:
        return "error"


def get_file_info(filepath):

    size = os.path.getsize(filepath)

    ext = os.path.splitext(filepath)[1].replace(".", "").lower()

    actual = detect_type(filepath)

    mismatch = ext != actual

    return {
        "path": filepath,
        "extension": ext,
        "actual": actual,
        "size": size,
        "mismatch": mismatch
    }