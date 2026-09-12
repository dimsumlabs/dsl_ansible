#!/usr/bin/env python3
"""Load the userdb and ensure the uids are all unique"""

import argparse
import pytest
import yaml


# TODO:
# a list of userdb files, so we can check the intersection


def argparser():
    args = argparse.ArgumentParser(description=__doc__)

    args.add_argument(
        "--userdb",
        default="vars/userdb.yml",
        help="Select the file to load and check",
    )
    result = args.parse_args()

    return result


def check_uid_ok(userdb):
    uids = set()

    for username, user in userdb.items():
        uid = user["uid"]
        if uid in uids:
            raise ValueError(f"ERROR: duplicate uid {uid} user {username}")

        uids.add(uid)

    return True


def test_check_uid_ok():
    userdb = {
        "larry": {
            "uid": 10,
        },
        "moe": {
            "uid": 20,
        },
        "curly": {
            "uid": 30,
        },
    }

    assert check_uid_ok(userdb)

    userdb["curly"]["uid"] = 10
    with pytest.raises(ValueError):
        check_uid_ok(userdb)


def main():
    args = argparser()

    # TODO: while files to load
    with open(args.userdb) as f:
        userdb = yaml.safe_load(f)
        # TODO:
        # - merge into
        # - report..

    check_uid_ok(userdb)


if __name__ == "__main__":
    main()
