SRC = $(wildcard ./*.ipynb)

all: data-science-bowl-2019 docs

data-science-bowl-2019: $(SRC)
	nbdev_build_lib
	touch data-science-bowl-2019

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist