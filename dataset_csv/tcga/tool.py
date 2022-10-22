#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--train_csv", type=str)
parser.add_argument("--val_csv", type=str)
parser.add_argument("--test_csv", type=str, default="./test.csv")
parser.add_argument("--save", type=str, default="./")
parser.add_argument("--name", type=str)


args = parser.parse_args()


def main(args):
    df_train = pd.read_csv(args.train_csv)
    df_val = pd.read_csv(args.val_csv)
    df_test = pd.read_csv(args.test_csv)
    import ipdb;ipdb.set_trace()

    df_train["train"] = df_train["slides_name"].map(
        lambda x: x.split("/")[-1]
    )
    df_train["train_label"] = df_train["label"]
    df_train = df_train.drop(labels=["slides_name", "label"], axis=1)
    df_val["val"] = df_val["slides_name"].map(
        lambda x: x.split("/")[-1]
    )
    df_val["val_label"] = df_val["label"]
    df_val = df_val.drop(labels=["slides_name", "label"], axis=1)
    df_test["test"] = df_test["slides_name"].map(
        lambda x: x.split("/")[-1]
    )
    df_test["test_label"] = df_test["label"]
    df_test = df_test.drop(labels=["slides_name", "label"], axis=1)

    df_total = pd.concat([df_train, df_val, df_test], axis=1)

    df_total.to_csv(os.path.join(args.save, args.name))


if __name__ == "__main__":
    main(args)

