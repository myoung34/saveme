setup:
	poetry install

gen_requirements:
	poetry export --without-hashes -f requirements.txt >requirements.txt

gen_requirements_dev:
	poetry export --dev --without-hashes -f requirements.txt >requirements-dev.txt

.PHONY: build test
build: clean
	fpm \
		-s dir \
		-t osxpkg \
		-v 0.0.2 \
		--after-install installer/after_install.sh \
		--before-remove installer/before_remove.sh \
		--after-remove installer/before_remove.sh \
		--prefix /opt/saveme \
		-n saveme \
		-C installer


zip: build
	@cd ./build/lib; \
	  zip -r9 ../../saveme.zip .

test:
	poetry run tox

run:
	@cd ./build/lib; \
		echo todo

clean:
	rm *.pkg || :
