import argparse
from testdatagenerator import PersonalNumberGenerator, PersonNameGenerator



def main():
    parser = argparse.ArgumentParser(description="A tool for generating input data. Use stand-alone or in an existing workflow to supply data.")
    parser.add_argument('-p', '--pnr', action='store_true', default=False, help="Generate Personal Number")
    parser.add_argument('-n', '--name', action='store_true', default=False, help="Generate Personal Number")
    args = parser.parse_args()
    
    if args.pnr:
        p = PersonalNumberGenerator.PersonalNumberGenerator()
        print(p.pnr())

    elif args.name:
        p = PersonNameGenerator.PersonNameGenerator()
        print(p.full_name())

    else:
        print("No options supplied!")


if __name__ == "__main__":
    main()