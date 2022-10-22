#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--test_csv", type=str, default="./test.csv")
parser.add_argument("--save", type=str, default="./")
parser.add_argument("--name", type=str)


args = parser.parse_args()


def main(args):
    df_test = pd.read_csv(args.test_csv)

    df_test["test"] = df_test["slides_name"].map(
        lambda x: x.split("/")[-1]
    )
    df_test["test_label"] = df_test["label"]
    df_test = df_test.drop(labels=["slides_name", "label"], axis=1)


    df_test.to_csv(os.path.join(args.save, args.name))


if __name__ == "__main__":
    main(args)

