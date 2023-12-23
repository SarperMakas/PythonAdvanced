from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument("square", help="Squares a given number", type=int, default=0)  # choices=[1, 2, 3, 4]
parser.add_argument("-v", "--verbose", help="Provides a verbose desc",
                    action="store_true", required=True)


args: Namespace = parser.parse_args()

if args.verbose:
    print(f"{args.square} squared is {args.square ** 2}")
else:
    print(args.square**2)