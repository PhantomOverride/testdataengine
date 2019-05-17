import argparse
from testdatagenerator import PersonalNumberGenerator, PersonNameGenerator, EmailGenerator



def main():
    parser = argparse.ArgumentParser(description="A tool for generating input data. Use stand-alone or in an existing workflow to supply data.")
    parser.add_argument('-p', '--pnr', action='store_true', default=False, help="Generate Personal Number")
    parser.add_argument('-n', '--name', action='store_true', default=False, help="Generate Personal Name")
    parser.add_argument('-e', '--email', action='store_true', default=False, help="Generate Personal Email")
    args = parser.parse_args()
    
    if args.pnr:
        p = PersonalNumberGenerator.PersonalNumberGenerator()
        print(p.pnr())

    elif args.name:
        p = PersonNameGenerator.PersonNameGenerator()
        print(p.full_name())

    elif args.email:
        p = EmailGenerator.EmailGenerator()
        print(p.personal_email())

    else:
        print("No options supplied!")


if __name__ == "__main__":
    main()
