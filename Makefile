setup:
	poetry install

bump_version:
	sed -i.bak "s/version = \".*\"/version = \"$(VERSION)\"/g" pyproject.toml
	sed -i.bak "s/version='.*'/version='$(VERSION)'/g" setup.py
	sed -i.bak "s/==.\+\(..var.*\)/==$(VERSION) \1/g" installer/after_install.sh
	rm pyproject.toml.bak setup.py.bak installer/after_install.sh.bak

gen_requirements:
	poetry export --without-hashes -f requirements.txt >requirements.txt

gen_requirements_dev:
	poetry export --dev --without-hashes -f requirements.txt >requirements-dev.txt

test:
	poetry run tox

clean:
	rm *.pkg || :
