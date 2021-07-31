"""
This script grab your commit message
and suggest a commit label;
example:
    branch_name = TEAM-123456
    message = "commenting the binary tree code"
    commit message = "[TEAM-123456][CLEAN] commenting the binary tree code"
>> pycommit.py "commenting the binary tree code"
"""
#! /usr/bin/python3
import fire
import re
from subprocess import check_output, call, DEVNULL


def grab_bug(msg: str):
    p = re.compile("bug|bugfix")
    o = re.search(p, msg)
    return '[BUGFIX]' if o is not None else ""


def grab_clean(msg: str):
    p = re.compile("comment|doc|pep|salt")
    o = re.search(p, msg)
    return '[CLEAN]' if o is not None else ""


def grab_refactor(msg: str):
    p = re.compile("refactor|reorganize")
    o = re.search(p, msg)
    return '[REFACTOR]' if o is not None else ""


def grab_build(msg: str):
    p = re.compile("cmake|build")
    o = re.search(p, msg)
    return '[BUILD]' if o is not None else ""


def grab_review(msg: str):
    p = re.compile("review")
    o = re.search(p, msg)
    return '[REVIEW]' if o is not None else ""


def grab_script(msg: str):
    p = re.compile("script|software")
    o = re.search(p, msg)
    return '[SCRIPT]' if o is not None else ""


def grab_optim(msg: str):
    p = re.compile("optim|faster|accelerat|runtime")
    o = re.search(p, msg)
    return '[OPTIM]' if o is not None else ""


def grab_dev(msg: str):
    p = re.compile("development|algorithm")
    o = re.search(p, msg)
    return '[DEV]' if o is not None else ""


def get_commit_label(msg: str):
    label = grab_bug(msg) or\
        grab_clean(msg) or\
        grab_refactor(msg) or\
        grab_build(msg) or\
        grab_review(msg) or\
        grab_script(msg) or\
        grab_optim(msg) or\
        grab_dev(msg)
    return label or "[DEV]"


def pycommit(msg: str):
    # get branch id
    a = check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    a = a.decode('utf-8')
    print('branch_name: ', a)
    p = re.compile("TEAM-[\d]+")
    o = re.search(p, a)
    label = get_commit_label(msg)
    if o is None:
        s = '['+a+']'+label+' '+msg
    else:
        s = o.group(0)
        s = '['+s+']'+label+' '+msg
    print('Your git message: ', s)
    e = check_output(['git', 'commit', '-m', s])


if __name__ == '__main__':
    import fire
    fire.Fire(pycommit)
