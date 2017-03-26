#!/bin/bash

set -e

pip install -e .

case "$1" in
    test)
        python example/run_tests.py
    ;;
    coverage)
        coverage run example/run_tests.py
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
    bash)
        bash
    ;;
    *)
        python example/manage.py migrate
        python example/manage.py loaddata data
        python example/manage.py runserver 0.0.0.0:8001
    ;;
esac
