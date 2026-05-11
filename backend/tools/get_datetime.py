from datetime import datetime


def get_datetime() -> dict[str, str]:
    now = datetime.now()

    return {
        "current_datetime": now.isoformat(timespec="seconds"),
        "date": now.date().isoformat(),
        "time": now.time().isoformat(timespec="seconds"),
    }
