#!/bin/bash

export FLASK_DEBUG=1 
export FLASK_APP=app.py

flask run >flask.log 2>&1 &
