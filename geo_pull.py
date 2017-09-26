from g_keys import gkey
import json
import requests as req

url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s,+%s&key=%s" % (city, state, gkey)

