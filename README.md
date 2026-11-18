# Horizon Hour

Keep the next sunrise or sunset in view. The countdown uses the observer’s coordinates. A small sun rises or sinks beside the reading. The ground color follows the local meteorological season, and the forecast adds clouds, rain or snow.

## Setup

Copy the Kyiv example and replace `latitude`, `longitude` and `place` for your observer. Use decimal degrees, with south and west negative. The companion selects the local time zone from the coordinates and refreshes the forecast every fifteen minutes. Python needs access to IANA time-zone data. On Windows install the `tzdata` package if ZoneInfo reports a missing zone. The public Open-Meteo endpoint is for eligible non-commercial use.

From the repository root, copy the example and start the companion with Python 3.10 or newer.

```sh
cp companion/example.json config.json
# Edit config.json for your source before starting the server.
python3 companion/serve.py --config config.json
```

In the emulator, run `~/.busy-emulator/bin/busy-emulator allow-local 8770` and approve that port. Open **Apps → Horizon Hour → Setup**, set **Local companion URL** to `http://127.0.0.1:8770/reading`, save, then reopen the app. For a physical bar, start the companion with `--host YOUR_LAN_IP` and replace `127.0.0.1` with that address. Bind only to your trusted network. Open `/reading` on the host to inspect the current reading. Keep credentials in the host environment.

## Find the next event

Read SUNRISE or SUNSET and the time left. The rear shows the event’s local clock time. After sunset the next upcoming sunrise replaces it automatically. At high latitudes, the app reports when no crossing appears in the four-day forecast.

![The sunset countdown changes to the current sky page.](media/guide/use-1.gif)

## Check the sky before heading out

Turn to SKY for the weather category and season. Turn back to the countdown to see the moving sun and weather marks. The recording uses a rainy autumn example in Kyiv.

![The rain page returns to the animated sunset countdown.](media/guide/use-2.gif)

## Run in the emulator

Install BUSY Bar Emulator and open it. From this repository run the following command, then press **Back** when you finish.

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

The recordings use example responses on emulator firmware. Each display pixel is enlarged to a 9 × 9 square.

Forecast and astronomical times by [Open-Meteo](https://open-meteo.com/en/docs).

[Rear display](screenshots/back-1.png) · [MIT license](LICENSE)
