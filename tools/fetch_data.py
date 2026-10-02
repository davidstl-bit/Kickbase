#!/usr/bin/env python3
"""Holt alle Spieler von api.kbstats.de und schreibt data/players.json (nur die benötigten Felder)."""
import json, sys, datetime, urllib.request

URL = "https://api.kbstats.de/api/v1/players"
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (kickbase-analyse)", "Accept": "application/json"})
with urllib.request.urlopen(req, timeout=60) as r:
    raw = json.load(r)

def n(v, d=None):
    """Zahl lesen; auch Zahlen, die als Text geliefert werden (z. B. teamId "2")."""
    if isinstance(v, bool):
        return d
    if isinstance(v, (int, float)):
        return v
    if isinstance(v, str):
        try:
            return float(v) if "." in v else int(v)
        except ValueError:
            return d
    return d

players = []
for p in raw:
    if p.get("id") is None:
        continue
    players.append({
        "id": int(p["id"]), "t": int(n(p.get("teamId"), 0)), "fn": p.get("firstName") or "", "ln": p.get("lastName") or "",
        "mv": int(n(p.get("marketValue"), 0)), "avg": n(p.get("averagePoints")), "gp": n(p.get("gamesPlayed")),
        "pt": n(p.get("totalPoints")), "st": int(n(p.get("status"), 0)), "pos": int(n(p.get("position"), 3)),
        "img": p.get("playerImage") or "", "no": int(n(p.get("number"), 0)), "tr": int(n(p.get("trend"), 0)),
        "pr": int(n(p.get("startProbability"), 5)), "ch": int(n(p.get("marketChangeToday"), 0)),
    })
if len(players) < 300:
    sys.exit(f"Abbruch: nur {len(players)} Spieler erhalten, alte Daten bleiben erhalten.")
out = {"updated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "players": players}
with open("data/players.json", "w", encoding="utf8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
print("OK", len(players), "Spieler")
