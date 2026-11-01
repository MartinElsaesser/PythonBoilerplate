# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.3",
# ]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import sys

    # add root dir as import path: https://stackoverflow.com/a/35273613
    module_path = "/workspace"
    if module_path not in sys.path:
        sys.path.append(module_path)

    sys.path
    return


@app.cell
def _():
    from typing import reveal_type, cast

    reveal_type("abc")
    cast(str, "abc")
    return


@app.cell
def _():
    from helpers.checked_cast import ccast

    lol = ccast(str, "abc")
    lol
    return


if __name__ == "__main__":
    app.run()
