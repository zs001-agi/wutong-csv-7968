import argparse
import csv
import sys

def main():
    parser = argparse.ArgumentParser(description='CSV viewer/filter/sort/merge tool')
    parser.add_argument('input', nargs='+', help='Input CSV files to process')
    parser.add_argument('--json', action='store_true', help='Output as JSON instead of CSV')
    parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help='Output file')

    args = parser.parse_args()

    if args.json:
        import json
        output_data = []

    for input_file in args.input:
        with open(input_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

            if args.json:
                output_data.extend(data)
            else:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(args.output, fieldnames=fieldnames)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)

    if args.json:
        json.dump(output_data, args.output, indent=4)

if __name__ == '__main__':
    main()