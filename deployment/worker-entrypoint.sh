#!/bin/sh
celery -A imagegenerator worker --beat -l INFO