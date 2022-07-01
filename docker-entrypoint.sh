#!/bin/bash

set -e

pip install -e .

case "$1" in
    test)
        python example/manage.py test example.app
    ;;
    coverage)
        coverage run example/manage.py test example.app
        coverage report
        coverage html
    ;;
    release)
        python setup.py sdist upload
    ;;
    shell)
        python example/manage.py shell
    ;;
    manage)
        python example/manage.py "${@:2}"
    ;;
    python)
        python "${@:2}"
    ;;
    tox)
        tox "${@:2}"
    ;;
    bash)
        bash
    ;;
    *)
        python example/manage.py migrate
        python example/manage.py loaddata data
        python example/manage.py runserver 0.0.0.0:8001
    ;;
esac
