import json
from datetime import datetime


def export_json(data):

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    return filename


def export_txt(data):

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:

        for item in data:

            f.write("=" * 60 + "\n")

            for k, v in item.items():
                f.write(f"{k}: {v}\n")

    return filename