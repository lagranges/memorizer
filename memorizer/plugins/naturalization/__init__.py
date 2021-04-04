#! /usr/bin/env python3
import os
from .parser import (
    parse_easytrangers,
)

DATA_DIR = os.path.realpath(
    os.environ["MEMPLG_NATURALIZATION_DATA_DIR"]
)
PARSERS = {
    "easytrangers": parse_easytrangers
}


def read_metadata(filepath):
    res = {}
    with open(filepath, "r") as fd:
        for line in fd.readlines():
            try:
                l, r = line.split(":", 1)
                res[l] = r.strip()
            except Exception:
                print("Unexpected format: ", line)
    return res


def load_data(name):
    folder = os.path.join(
        DATA_DIR,
        name
    )
    meta_data = read_metadata(os.path.join(folder, "data.meta"))
    parser = PARSERS[meta_data["parser"]]
    filepath = os.path.join(folder, meta_data["filename"])
    return parser(filepath)


def get_quetion_answers():
    res = {}
    dataset_names = os.listdir(DATA_DIR)[:1]
    for name in dataset_names:
        res.update(load_data(name))
    return res
