from invoke import task


@task
def setup_pip(c):
    """[pip] Setup dev environment"""
    # install ploomber in editable mode and include development dependencies
    c.run('pip install --editable ".[dev]"')


@task
def build(c):
    c.run("python setup.py build")


@task(aliases=["v"])
def version(c):
    """Release a new version"""
    from pkgmt import versioneer

    versioneer.version(project_root=".", tag=True)


@task
def test(c, report=False):
    """Run tests"""
    c.run(
        "pytest tests --durations=0 " + ("--cov-report html" if report else ""),
        pty=True,
    )
    c.run("flake8")


@task
def reformat(c):
    """Reformat the code"""
    c.run("black .")
    c.run("flake8")
