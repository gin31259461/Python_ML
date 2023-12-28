import re

import numpy as np


# normalizes a string by converting to lower case, replacing all spaces with _
def normalize_name(s: str):
    if s is np.nan or s is None:
        return np.nan
    s = s.strip().lower()
    return re.sub(r"\s+", "_", s)


# cleans the breed type, returning a normalized form of the primary breed and an indicator
# variable if it's a mix
# returning a pd.Series is very slow for some reason
# instead return a single string with / as the separator
def clean_breed(s: str, keep_both: bool = True):
    s = s.lower()
    if "/" in s:
        b, b2, *_ = s.split("/")
        b = normalize_name(b)
        b2 = normalize_name(b2)
        m = "1"
    elif "mix" in s:
        b = s.replace("mix", "")
        b, b2, m = normalize_name(b), "", "1"
    else:
        b, b2, m = normalize_name(s), "", "0"

    if keep_both:
        return "/".join([b, b2, m])
    else:
        return "/".join([b, m])


# converts age string into an age number in months
# returns 1000 if age information is missing
# i'm assuming that lack of age information is greater than any other age,
# i.e. old animals and animals with age information have similar properties
def clean_age(a: str):
    if a is np.nan:
        return 1000
    age, unit = a.strip().lower().split()
    age = float(age)
    if "week" in unit:
        age *= 12 / 52
    elif "year" in unit:
        age *= 12
    return age


# converts a multi-class np.array into a list of dicts with one-hot encoded features
def array_to_dict(class_arr: np.array):
    result = list()
    for row in class_arr:
        # create a dictionary for each row
        feats = dict()
        for c in row:
            # assumes feature value is either a string or np.nan
            # np.nan can't be used on strings so using alternative method to detect np.nan
            if isinstance(c, str):
                feats[c] = 1
        result.append(feats)
    return result


def clean_normalized_sex(s: str):
    if s == "unknown":
        return "/".join(["0.5", "0.5"])

    neutered = np.nan
    sex = np.nan
    s1, s2 = s.split("_")

    if s1 == "intact":
        neutered = "0"
    elif s1 == "neutered" or s1 == "spayed":
        neutered = "1"

    if s2 == "female":
        sex = "0"
    elif s2 == "male":
        sex = "1"

    return "/".join([neutered, sex])
