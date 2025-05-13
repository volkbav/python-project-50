from gendiff.core.generate_diff import generate_diff
from cli import parse_args

def main():
  args = parse_args()
  diff = generate_diff(
     args.first_file, args.second_file, args.format
     )
  print(f'diff: \n {diff}')

if __name__ == "__main__":
    main()