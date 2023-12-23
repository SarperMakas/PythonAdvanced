from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

# position argument | required is an invalid argument
parser.add_argument("square",
                    help="Squares a given number",
                    type=int,
                    nargs="2",  # only looking for one argument | can be int
                    default=0)

parser.add_argument("-v", "--verbose",
                    help="Verbose description. Use -vv for extra verbose",
                    # type=int, can't use with action
                    action="count",  # value is number of v => -v: 1 -vv: 2
                    default=0)

args: Namespace = parser.parse_args()

print(args.square)

result: int = args.square ** 2

if args.verbose == 1:
    print(f"The result is {result}")
elif args.verbose == 2:
    print(f"{args.square} ** 2 = {result}")
else:
    print(result)