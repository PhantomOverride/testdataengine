import argparse
from testdatagenerator import PersonalNumberGenerator


def main():
    parser = argparse.ArgumentParser(description="A tool for generating input data. Use stand-alone or in an existing workflow to supply data.")
    parser.add_argument('-p', '--pnr', action='store_true', default=False, help="Generate Personal Number")
    args = parser.parse_args()
    
    if args.pnr:
        print(PersonalNumberGenerator.pnr())
    else:
        print("No options supplied!")


if __name__ == "__main__":
    main()