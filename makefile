babel-extract:
	pybabel extract -F babel.cfg sphinx_simplepdf/themes -o sphinx_simplepdf/locale/sphinx.pot

lang=zh

babel-init:
	pybabel init -D sphinx -i sphinx_simplepdf/locale/sphinx.pot -d sphinx_simplepdf/locale -l ${lang}

babel-update:
	pybabel update -D sphinx -i sphinx_simplepdf/locale/sphinx.pot -d sphinx_simplepdf/locale -l ${lang}

babel-compile:
	pybabel compile -D sphinx -d sphinx_simplepdf/locale
