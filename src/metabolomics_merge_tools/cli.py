import argparse
from metabolomics_merge_tools.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Utilities to merge sample sheets, metabolite matrices, and curated panel labels.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
