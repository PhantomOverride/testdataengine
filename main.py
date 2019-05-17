import argparse
from testdatagenerator import PersonalNumberGenerator

def main():
    parser = argparse.ArgumentParser(description="A tool for generating relevant testdata for testing.")
    parser.add_argument('--pnr', action='store_true', default=False, help="Generate Personal Number") 
    args = parser.parse_args()
    
    if args.pnr:
        print(PersonalNumberGenerator.pnr())
    else:
        print("test")




if __name__ == "__main__":
    main()