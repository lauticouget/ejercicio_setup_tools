import setuptools

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ejercicio_setup_tools",
    version="0.1.0",
    author="Lutz",
    author_email="lutz@lutz.com",
    description="Ejercicio setup tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lauticouget/ejercicio_setup_tools",
    project_urls={
        "Bug Tracker": "https://github.com/lauticouget/ejercicio_setup_tools/issues"
    },
    license="None",
    packages=["humai_utils"],
    install_requires=["requests"],
)
