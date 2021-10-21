from datetime import datetime


def get_iso_format_date(date: str) -> datetime:
    try:
        return datetime.fromisoformat(date)
    except ValueError:
        date = convert_date_str_to_iso_format(date)
        return datetime.fromisoformat(date)


def convert_date_str_to_iso_format(date: str) -> str:
    if date.endswith("Z"):
        return date.replace("Z", "+00:00")
    if date.endswith("+0000"):
        return date.replace("+0000", "+00:00")
    if date.endswith("-0000"):
        return date.replace("-0000", "-00:00")
