#!/usr/bin/env python

import os
import marvin
import sys
from pydantic import BaseModel
from enum import Enum
import subprocess

args = sys.argv
# model = "gpt-3.5-turbo-1106" if "-4" not in args else "gpt-4-1106-preview"
model = "gpt-4-1106-preview"
marvin.settings.llm_model = f"openai/{model}"

local_co_authors_file = ".co-authors"
global_co_authors_file = os.path.join(os.path.expanduser("~"), ".co-authors")


class HumanIntention(Enum):
    UPDATE_CO_AUTHORS = 1


def exists(file: str) -> bool:
    return os.path.isfile(file)


def create_co_authors_file():
    if exists(file=local_co_authors_file):
        return

    with open(local_co_authors_file, "w") as f:
        f.write("")


def get_user_input() -> str:
    return " ".join(args[1:])


class CoAuthor(BaseModel):
    name: str
    email: str

    def __str__(self):
        return f"Co-authored-by: {self.name} <{self.email}>"


@marvin.ai_fn
def determine_co_authors(
    user_input: str, current_co_authors: str, known_co_authors: str
) -> list[CoAuthor]:
    """
    Determines the co-authors based on
    the user input and
    the current co-authors and
    known co-authors.
    """


def read_co_authors_file(file: str) -> str:
    if exists(file=file):
        return open(file, "r").read()
    else:
        return None


def get_current_co_authors():
    return read_co_authors_file(file=local_co_authors_file)


def read_co_authors_from_git_history():
    try:
        authors = subprocess.check_output(
            "git log --pretty=format:'%an <%ae>' | sort | uniq",
            shell=True,
            text=True,
        )
        print("Authors from git history:", authors, file=sys.stderr)
        co_authors_output = subprocess.check_output(
            "git log --pretty=format:'%B' | grep -i 'Co-authored-by' | sort | uniq || true",
            shell=True,
            text=True,
        )
        print("Co-authors from git history:", co_authors_output, file=sys.stderr)

        return "\n".join([authors, co_authors_output])
    except subprocess.CalledProcessError as e:
        print(
            "An error occurred while reading co-authors from git history:",
            e,
            file=sys.stderr,
        )
        return ""


def get_known_co_authors():
    return "\n".join(
        [
            str(read_co_authors_file(file=global_co_authors_file)),
            read_co_authors_from_git_history(),
        ]
    )


def format_co_authors(co_authors: list[CoAuthor]) -> str:
    return "\n".join([str(co_author) for co_author in co_authors])


def update_co_authors(co_authors: list[CoAuthor]):
    new_co_authors = format_co_authors(co_authors)
    print("New co-authors:", new_co_authors, file=sys.stderr)
    with open(local_co_authors_file, "w") as f:
        f.write(new_co_authors)


def config_git_to_use_commit_template():
    os.system(f"git config commit.template {local_co_authors_file}")


def git_ignore_co_authors_file():
    os.system(f"echo {local_co_authors_file} >> .gitignore")


def set_up():
    config_git_to_use_commit_template()
    git_ignore_co_authors_file()


def main():
    set_up()
    update_co_authors(
        co_authors=determine_co_authors(
            user_input=get_user_input(),
            current_co_authors=get_current_co_authors(),
            known_co_authors=get_known_co_authors(),
        )
    )


if __name__ == "__main__":
    main()
