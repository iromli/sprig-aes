.PHONY: test clean all develop install zipapp
.DEFAULT_GOAL := develop

develop:
	/usr/bin/env pip install -r requirements-dev.txt

install:
	/usr/bin/env pip install -r requirements.txt

zipapp:
	shiv --compressed -o sprig-aes.pyz -p '/usr/bin/env python3' -e sprig_aes.cli:cli . --no-cache --no-build-isolation
