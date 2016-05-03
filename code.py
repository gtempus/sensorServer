#!/usr/bin/env python

import web
import json

db = web.database(dbn='sqlite', db='sensorsdb')
render = web.template.render('templates/')

urls = (
  '/', 'index',
  '/cycle', 'cycle',
  '/ac', 'ac',
  '/hub_temp', 'hubTemp'
)

class index:
    def GET(self):
        pump_cycles = db.select('PumpCycle')
        return render.cycles(pump_cycles)

class cycle:
    def GET(self):
        pump_cycles = db.select('PumpCycle')
        return render.cycles(pump_cycles)

    def POST(self):
        i = json.loads(web.data())
        n = db.insert('PumpCycle', state=int(i['state']))
        return n

class ac:
    def GET(self):
        pump_ac = db.select('PumpAC')
        return render.ac(pump_ac)

    def POST(self):
        i = json.loads(web.data())
        n = db.insert('PumpAC', state=int(i['state']))
        return n

class hubTemp:
    def GET(self):
        temps = db.select('HubTemp')
        return render.hub_temps(temps)

    def POST(self):
        i = json.loads(web.data())
        temp = (int(i['state']) / 100.0 * 10) / 10
        n = db.insert('HubTemp', state=temp)
        return n;

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
