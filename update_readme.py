#!/usr/bin/env python3
import inspect
import logging
import sys
from pathlib import Path

from google_cloud_helper.BigQueryHelper import BigQueryHelper  # noqa: F401
from google_cloud_helper.GoogleBucketHelper import GoogleBucketHelper  # noqa: F401
from google_cloud_helper.SecretManagerHelper import SecretManagerHelper  # noqa: F401

logging.basicConfig(level=logging.INFO)


PACKAGE_NAME = "google_cloud_helper"
CLASS_NAMES = ["BigQueryHelper", "GoogleBucketHelper", "SecretManagerHelper"]

sys.path.insert(0, str(Path(__file__).resolve().parent / "google_cloud_helper"))

README_PATH = Path(__file__).parent / "README.md"


def get_classes(module):
    """Return all classes defined in a module."""
    return [
        cls
        for name, cls in inspect.getmembers(module, inspect.isclass)
        if cls.__module__ == module.__name__
    ]  # exclude imported classes


def get_public_methods(cls):
    """Return public methods of a class."""
    return sorted(
        (name, obj)
        for name, obj in inspect.getmembers(cls)
        if callable(obj) and not name.startswith("_")
    )


def get_method_args(method):
    """Return argument names of a method."""
    sig = inspect.signature(method)
    return list(sig.parameters.keys())


def update_section(readme_text, marker_name, new_content):
    start_marker = f"<!-- {marker_name} START -->"
    end_marker = f"<!-- {marker_name} END -->"
    if start_marker not in readme_text or end_marker not in readme_text:
        sys.exit(f"Error: README missing markers for {marker_name} section.")
    before = readme_text.split(start_marker)[0] + start_marker + "\n"
    after = "\n" + end_marker + readme_text.split(end_marker)[1]
    return before + new_content + after


def main():
    logging.info("Updating README with class method lists...")

    readme = README_PATH.read_text(encoding="utf-8")

    # For each helper class, get its methods and update the README
    for cls_name in CLASS_NAMES:
        try:
            cls = globals()[cls_name]
            # try:
            #    instance = cls()
            # except TypeError:
            #    instance = cls("test")
        except AttributeError:
            sys.exit(
                f"Error: Class '{cls_name}' not found in package '{PACKAGE_NAME}'."
            )

        methods = get_public_methods(cls)
        if len(methods) == 0:
            methods_md = "_No public methods found_"
            continue
        methods_md = ""
        for name, method in methods:
            args = get_method_args(method)
            methods_md += f"- `{name}({', '.join(args)})`\n"

        readme = update_section(readme, cls_name.upper(), methods_md)

    README_PATH.write_text(readme, encoding="utf-8")
    logging.info("README updated with class method lists.")


if __name__ == "__main__":
    main()
