install-deps:
	pip install -r requirements.txt

run:
	export LC_ALL=pt_BR.utf-8; \
	export LANG=pt_BR.utf-8; \
	FLASK_APP=webpresence_app.py flask run

debug:
	export LC_ALL=pt_BR.utf-8; \
	export LANG=pt_BR.utf-8; \
	export FLASK_DEBUG=1; \
	FLASK_APP=webpresence_app.py flask run

