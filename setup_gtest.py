#!/home/jwhite/.cache/pypoetry/virtualenvs/gtest-setup-LfEI3PIb-py3.8/bin/python3

from gtest_setup import GTestSetup
import argparse


def main():
    description = "Sets up a folder for a leetcode problem w/ GTests"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("project", help="project name (no spaces)")
    parser.add_argument("-p", "--path", help="full path to project")
    args = parser.parse_args()
    GTestSetup(project=args.project, path=args.path).Setup()


if __name__ == '__main__':
    main()
