import re
from numbers import Number

time_units = (
    dict(
        divider=1e-9, singular="nanosecond", plural="nanoseconds", abbreviations=["ns"]
    ),
    dict(
        divider=1e-6,
        singular="microsecond",
        plural="microseconds",
        abbreviations=["us"],
    ),
    dict(
        divider=1e-3,
        singular="millisecond",
        plural="milliseconds",
        abbreviations=["ms"],
    ),
    dict(
        divider=1,
        singular="second",
        plural="seconds",
        abbreviations=["s", "sec", "secs"],
    ),
    dict(
        divider=60,
        singular="minute",
        plural="minutes",
        abbreviations=["m", "min", "mins"],
    ),
    dict(divider=60 * 60, singular="hour", plural="hours", abbreviations=["h"]),
    dict(divider=60 * 60 * 24, singular="day", plural="days", abbreviations=["d"]),
    dict(
        divider=60 * 60 * 24 * 7, singular="week", plural="weeks", abbreviations=["w"]
    ),
    dict(
        divider=60 * 60 * 24 * 7 * 52,
        singular="year",
        plural="years",
        abbreviations=["y"],
    ),
)


def format_duration(timespan):
    duration = []

    for character in re.split(r"(\d+(?:\.\d+)?)", timespan):
        character = character.strip()
        if re.match(r"\d+\.\d+", character):
            duration.append(float(character))
        elif character.isdigit():
            duration.append(int(character))
        elif character:
            duration.append(character)

    if duration and isinstance(duration[0], Number):
        if len(duration) == 1:
            return float(duration[0])

        if len(duration) == 2 and isinstance(duration[1], str):
            normalized_unit = duration[1].lower()
            for unit in time_units:
                if (
                    normalized_unit == unit["singular"]
                    or normalized_unit == unit["plural"]
                    or normalized_unit in unit["abbreviations"]
                ):
                    return float(duration[0]) * unit["divider"]

    msg = "Failed to format timespan! (input {} was tokenized as {})".format(
        timespan, duration
    )
    raise InvalidTimespan(msg)


if __name__ == "__main__":
    duration_str = "2m"
    duration_sec = format_duration(duration_str)
    print(duration_sec)
