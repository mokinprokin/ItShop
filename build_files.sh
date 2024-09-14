#!/bin/bash
python3 -m pip install -r requirements.txt
apt install libsqlite3-dev
python3 ./AkademyShop/shop/manage.py runserver