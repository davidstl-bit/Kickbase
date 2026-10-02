# Kickbase Analyse – Einrichtung (einmalig, ca. 15 Minuten)

1. Konto auf github.com anlegen (kostenlos) und oben rechts „+ → New repository“ wählen. Name z. B. `kickbase`, Sichtbarkeit **Public**, anlegen.
2. „uploading an existing file“ wählen und den **gesamten Inhalt dieses Ordners** hochziehen (index.html, Ordner data, tools, .github). Wichtig: auch der versteckte Ordner `.github` muss mit, sonst fehlt der Zeitplan. Danach „Commit changes“.
3. Im Repository: **Settings → Pages → Source: „Deploy from a branch“ → Branch `main`, Ordner `/ (root)` → Save.** Nach ca. 1 Minute steht oben die Adresse deiner Seite (`https://DEINNAME.github.io/kickbase/`).
4. Im Repository: **Actions** öffnen, den Workflow „Marktwerte aktualisieren“ wählen, **Run workflow** klicken. Wenn der Lauf grün ist, sind die Daten live. Falls er rot ist, steht im Log der Grund (z. B. Schnittstelle blockiert Abfragen von GitHub).
5. Ab dann läuft die Aktualisierung jeden Tag um 22:20 Uhr automatisch (zusätzlich um 6:10 Uhr als Sicherheitsnetz).

Dein Team, Budget und die Transfers speichert die Seite im Browser deines Geräts. Auf einem anderen Gerät beginnst du mit dem Stand aus der Excel.
