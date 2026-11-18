"""Find the next sunrise or sunset for an observer using Open-Meteo local dates."""
import json,time,datetime
from urllib.request import urlopen
from urllib.parse import urlencode
from zoneinfo import ZoneInfo
from serve import page
INTERVAL=10
def snapshot(o,m):
    now=time.time();lat=float(o["latitude"]);lon=float(o["longitude"])
    if now-m.get("at",0)>900:
        query=urlencode(dict(latitude=lat,longitude=lon,daily="sunrise,sunset",current="weather_code",timezone="auto",timeformat="unixtime",forecast_days=4))
        with urlopen("https://api.open-meteo.com/v1/forecast?"+query,timeout=10) as r:m["data"]=json.load(r)
        m["at"]=now
    d=m["data"];zone=ZoneInfo(d["timezone"]);month=datetime.datetime.fromtimestamp(now,zone).month
    season=["winter","spring","summer","autumn"][((month%12)//3+(2 if lat<0 else 0))%4]
    events=[(t,k) for k in ("sunrise","sunset") for t in d["daily"][k] if t and t>now]
    if not events:return dict(state="No event in forecast",key="polar",pages=[page("HORIZON","No event","Next four local dates",season)])
    t,k=min(events);mins=int((t-now+59)//60);code=d["current"]["weather_code"]
    sky="snow" if code in [71,73,75,77,85,86] else "rain" if code>=51 else "cloud" if code else "clear"
    return dict(state=season+" / "+sky,key=k,pages=[page(k.upper(),f"{mins//60}h{mins%60:02}",season,sky,datetime.datetime.fromtimestamp(t,zone).strftime("%H:%M %Z")),page("SKY",sky,season,o.get("place","Observer"))])
