#!/usr/bin/env python

import web
import json

db = web.database(dbn='sqlite', db='sensorsdb')
render = web.template.render('templates/')

urls = (
  '/', 'index',
  '/cycle', 'cycle'
)

class index:
    def GET(self):
        pump_cycles = db.select('PumpCycle')
        return render.cycles(pump_cycles)

class cycle:
    def POST(self):
        i = json.loads(web.data())
        n = db.insert('PumpCycle', state=int(i['state']))
        return n

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
