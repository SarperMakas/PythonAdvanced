from argparse import ArgumentParser, Namespace

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group()

parser.usage = "Use it like this"

parser.add_argument("a",
                    type=int,
                    help="The base value",
                    default=0,
                    nargs="?")

parser.add_argument("b",
                    type=int,
                    help="The exponent value",
                    default=0,
                    nargs="?")

# only one of these options can run
group.add_argument("-v", "--verbose",
                   help="Provides a verbose description. Use -vv for extra verbose",
                   action="count")

group.add_argument("-s", "--silence",
                   help="Generate a silent version of the output",
                   action="store_true")



args: Namespace = parser.parse_args()
result: int = args.a ** args.b

if args.silence:
    print("Silenced!")

else:
    match args.verbose:
        case 1:
            print(f"The result is {result}")

        case 2:
            print(f"{args.a} ** {args.b} = {result}")

        case _:
            print(result)