#!/usr/bin/env python3
"""Commit the _build directory to the gh-pages branch.

This script is crazy. Use it if you dare!
"""

import contextlib
import functools
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile

info = functools.partial(print, '**** %s:' % sys.argv[0])


def run(*command, capture=False):
    info("running", ' '.join(map(shlex.quote, command)))
    if capture:
        output = subprocess.check_output(list(command))
        return output.decode('utf-8', errors='replace')

    subprocess.check_call(list(command))
    return None     # pep-8


@contextlib.contextmanager
def switch_branch(new_branch):
    output = run('git', 'branch', capture=True)
    [old_branch] = re.findall('^\* (.*)$', output, flags=re.MULTILINE)
    run('git', 'checkout', new_branch)

    try:
        yield
    except Exception as e:
        # undo everything to make sure that going back to old_branch works
        run('git', 'reset', 'HEAD', '.')
        run('git', 'checkout', '--', '.')
        raise e
    finally:
        run('git', 'checkout', old_branch)


@contextlib.contextmanager
def git_stash():
    # git stash doesn't work if there's nothing to stash
    open('stash-dummy', 'x').close()

    run('git', 'stash', '--all')
    try:
        yield
    finally:
        run('git', 'stash', 'pop')
        os.remove('stash-dummy')


def main():
    run(sys.executable, '-m', 'sphinx', '.', '_build')

    with tempfile.TemporaryDirectory() as tmpdir:
        info("copying _build to a temporary directory")
        tmpdir = os.path.join(tmpdir, '_build')
        shutil.copytree('_build', tmpdir)

        with git_stash():
            with switch_branch('gh-pages'):
                for item in os.listdir():
                    if item[0] != '.':
                        info('removing', item)
                        if os.path.isdir(item):
                            shutil.rmtree(item)
                        else:
                            os.remove(item)

                for item in os.listdir(tmpdir):
                    if item[0] != '.' or item == '.nojekyll':
                        info('copying', item)
                        src = os.path.join(tmpdir, item)
                        if os.path.isdir(src):
                            shutil.copytree(src, item)
                        else:
                            shutil.copy(src, item)

                run('git', 'add', '--all', '.')
                run('git', 'commit', '-m', 'updating docs with ' + __file__)

        info("deleting the temporary directory")

    run('git', 'push', 'origin', 'gh-pages')


if __name__ == '__main__':
    main()
