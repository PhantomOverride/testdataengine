#!/usr/bin/env python3

import argparse
from testdatagenerator import PersonalNumberGenerator, PersonNameGenerator, \
                              EmailGenerator


def main():
    parser = argparse.ArgumentParser(description="A tool for generating input data. Use stand-alone or in an existing workflow to supply data.")
    tool = parser.add_mutually_exclusive_group()
    tool.add_argument('-p', '--pnr', action='store_true', default=False, help="Generate Personal Number")
    tool.add_argument('-n', '--name', action='store_true', default=False, help="Generate Personal Name")
    tool.add_argument('-e', '--email', action='store_true', default=False, help="Generate Personal Email")

    parser.add_argument('-c', '--count', type=int, default=1, help="Number of items to generate")

    args = parser.parse_args()

    if args.pnr:
        p = PersonalNumberGenerator.PersonalNumberGenerator(True)

    elif args.name:
        p = PersonNameGenerator.PersonNameGenerator()

    elif args.email:
        p = EmailGenerator.EmailGenerator()

    else:
        print("No arguments given, exiting...")
        exit()

    count = args.count
    while count > 0:
        print(p.generator())
        count -= 1


if __name__ == "__main__":
    main()
