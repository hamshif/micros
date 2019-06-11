#!/usr/bin/env python

import json
import requests


def gossip(txt):

    h = 'http://'
    host = 'localhost'
    port = '5000'
    endpoint = 'gossip'

    url = f'{h}{host}:{port}/{endpoint}'

    payload = {
        "gossip": txt,
    }

    try:
        r = requests.post(url, params=payload)

        c = r.content

        d = json.loads(c)

        print(d)

        return r.content
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":

    gossip('lichluchim')


