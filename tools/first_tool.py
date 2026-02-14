"""First tool to show how to clarify the tool module.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

import argparse

from src.modules.first_module import print_hello


def parse_args() -> argparse.Namespace:
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        description="First tool to show how to clarify the tool module.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-i1", "--input1", type=str, default="Hello", help="First input."
    )
    parser.add_argument(
        "-i2", "--input2", type=str, default="World", help="Second input."
    )

    return parser.parse_args()


def main() -> None:
    """Main function."""
    args = parse_args()
    print(f"{args.input1}, {args.input2}!")
    print_hello(args.input2)


if __name__ == "__main__":
    main()
