setup:
	poetry install

gen_requirements:
	poetry export --without-hashes -f requirements.txt >requirements.txt

gen_requirements_dev:
	poetry export --dev --without-hashes -f requirements.txt >requirements-dev.txt

.PHONY: build test
build: clean
	fpm \
	  -s python \
	  -t tar \
	  --depends altgraph \
	  --depends chameleon \
	  --depends click \
	  --depends macholib \
	  --depends modulegraph \
	  --depends py2app \
	  --depends pyobjc-core \
	  --depends pyobjc-framework-cocoa \
	  --depends rumps \
	  --depends shellescape \
	  --prefix /opt/foo \
	  setup.py
#    --depends 'altgraph==0.17' \
#    --depends 'chameleon==3.9.0' \
#    --depends 'click==7.1.2' \
#    --depends 'macholib==1.14' \
#    --depends 'modulegraph==0.18' \
#    --depends 'py2app==0.23' \
#    --depends 'pyobjc-core==7.1' \
#    --depends 'pyobjc-framework-cocoa==7.1' \
#    --depends 'rumps==0.3.0' \
#    --depends 'shellescape==3.8.1' \
#		--prefix /opt/foo \

zip: build
	@cd ./build/lib; \
	  zip -r9 ../../saveme.zip .

test:
	poetry run tox

run:
	@cd ./build/lib; \
		echo todo

clean:
	find . -name '*.egg-info' -exec rm -rf {} \;
	find . -name '__pycache__' -exec rm -rf {} \;
	rm *.tar || :
