.PHONY: clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

clean: clean-media clean-output

clean-output:
	rm -f output/*

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-media:
	rm -f peachtree_converter/media/*


patch: clean ## package and upload a release
	git-flow release start $(REL)
	bumpversion patch
	git add .
	git commit -m "Updating version to $(REL)"

minor: clean ## package and upload a release
	git-flow release start $(REL)
	bumpversion minor
	git add .
	git commit -m "Updating version to $(REL)"

build-spa: clean ## package
	npm run --prefix tt_frontend build
	git add .
	git commit -m "Building frontend SPA"

release-patch: patch build-spa

release-minor: minor build-spa

heroku:
	git push origin master
	git push origin develop
	git push --tags
	git push heroku master
	heroku run python manage.py migrate
