# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Vins1206/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Vins1206/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

A [make.fun](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e) bounty entry: one line of weather forecast, at most 140 characters, for a city that does not exist — naming the place, giving it weather, and making a bored commuter smile on the way to work.

## The entry

> Good morning, Drizzlewick: light rain till nine, then sunshine on the platform — the 8:15 runs late, but the puddles are doing their best.

138 characters. Drizzlewick is invented; the forecast keeps the rhythm of broadcast weather (greeting, place, rain clearing by nine, sunshine) and bends it once at the end — the late bus is forgiven because the puddles are doing their best.

## How to run

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (creating `/output` if needed). Pure Python standard library, no network, no randomness — two runs produce byte-identical output.

## How it was chosen

Six candidate lines were drafted and scored against the judge's brief, in the brief's own order: reads as a one-line forecast for an invented city, makes a bored commuter smile, keeps the register of real broadcast weather, gives the city one concrete detail, uses its 140 characters well. The Drizzlewick line won on all five: the strongest broadcast rhythm, the gentlest joke, and 138 of the 140 characters used.
