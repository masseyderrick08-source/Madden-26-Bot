# SMARTONOMY Landing Page – Elementor-Template für das Aiero-Theme

Nachbau der Landing Page **smartonomy.de** als importierbares Elementor-Template,
optimiert für das WordPress-Theme **Aiero** (AI & Machine Learning Theme).

## Inhalt

| Datei | Zweck |
|---|---|
| `smartonomy-landing-elementor.json` | Elementor-Seiten-Template (kompletter One-Pager, ohne Bilder) |
| `smartonomy-landing-elementor-mit-bildern.json` | Wie oben, aber inkl. Original-Bilder: Hero-Hintergrundbild mit Navy-Overlay und SMARTONOMY-Logo im Hero |
| `smartonomy-landing-elementor-ewebot.json` | **Exakter Klon für das eWebot-Theme**: Original-Hero (helles Design, Bild rechts, weißes 105°-Verlaufs-Overlay, linksbündiger Text), Original-Buttons (`.hero-cta-primary`/`.hero-cta-ghost`), Trust-Badges als weiße Pills, Original-Markenverlauf `#2563EB → #7C3AED`, Karten-Rahmen/-Schatten — das komplette CSS ist als `<style>`-Block **in der JSON eingebettet**, es muss nichts separat eingefügt werden |
| `smartonomy-custom.css` | Zusatz-CSS (Inter-Font, Hover-Effekte, FAQ-Kartenstil, Smooth Scrolling) |
| `images/hero-bg.jpg` | Hero-Hintergrundbild (1600×1067) von smartonomy.de |
| `images/smartonomy-logo.png` | SMARTONOMY-Logo (847×294, transparent) |
| `images/favicon.png` | Favicon (identisch mit Logo) |

**Hinweis zu den Bildern:** Die Bild-Variante der JSON referenziert die Bilder per
URL direkt von `https://smartonomy.de`. Für den Produktivbetrieb die Dateien aus
`images/` in die WordPress-Mediathek hochladen und in Elementor neu zuweisen
(Hero-Sektion → Stil → Hintergrundbild sowie das Logo-Bild-Widget im Hero) —
sonst bleiben es Hotlinks auf die alte Seite.

## Enthaltene Sektionen (in Reihenfolge)

1. **Hero** – „Jeder verpasste Anruf ist ein verlorener Auftrag. Wir ändern das." mit CTA-Buttons und Trust-Badges (DSGVO, 48h-Setup, Geld-zurück-Garantie …)
2. **Probleme** – 3 Karten (verpasste Anrufe, tote Leitung nach 17 Uhr, überlastete Rezeption)
3. **Branchen** – Karten für Praxen & Ärzte, KFZ & Handwerk, Pflegedienste inkl. Kosten-Vergleich
4. **Ergebnisse** – 4 animierte Zähler (+280 % Terminbuchungen, 15 h Zeitersparnis, 92 % Sofortantworten, −60 % Servicekosten)
5. **Audio-Demo** – „So klingt Ihr KI-Assistent" (Platzhalter für eigenes Audio-Widget, s. u.)
6. **Leistungen** – KI-Telefonassistent, Chat & WhatsApp, Prozess-Automatisierung
7. **Ablauf** – 3 Schritte (Analyse → Setup → Go-Live)
8. **Preise** – Starter €99 / Standard €179 / Pro €249 mit Feature-Listen, Geld-zurück- und BNI-Hinweis
9. **ROI-Rechner** – voll funktionsfähig als HTML-Widget (reines Inline-JS, kein Plugin nötig)
10. **Kundenstimmen** – 3 Testimonials
11. **FAQ** – Akkordeon mit 7 Fragen/Antworten
12. **Kontakt/CTA** – „Kostenlos testen." mit Telefonnummer und Termin-Button

Es werden **nur kostenlose Elementor-Widgets** verwendet (Heading, Text, Button,
Icon-Box, Icon-Liste, Counter, Testimonial, Akkordeon, HTML) – **Elementor Pro ist
nicht erforderlich**.

## eWebot-Theme: Besonderheiten

Die Datei `smartonomy-landing-elementor-ewebot.json` funktioniert identisch zur
Aiero-Variante (eWebot nutzt ebenfalls Elementor). Unterschiede:

- **CSS ist eingebettet:** Die erste (unsichtbare) Sektion enthält ein HTML-Widget
  mit dem kompletten `<style>`-Block — Inter-Font, Button-Stile, Karten-Rahmen,
  Pill-Badges, Markenverlauf. Schritt 3 (Zusatz-CSS) entfällt daher.
- **Exakter Hero wie im Original:** helles Design, Hintergrundbild rechts sichtbar,
  weißes Verlaufs-Overlay (105°), Text linksbündig, Logo oben links.
- **eWebot-Einstellungen:** Unter Theme Options → General den Page Title Bar für
  diese Seite deaktivieren und im eWebot-Header ein Menü mit den Anker-Links
  anlegen (`#vorteile`, `#leistungen`, `#preise`, `#ablauf`, `#faq`, `#kontakt`).
  Header-Button „Termin buchen" auf `#kontakt` in Orange `#F97316`.

## Import-Anleitung

### 1. Template importieren

1. WordPress-Admin → **Templates → Gespeicherte Templates** (Elementor-Bibliothek)
2. Oben auf **Templates importieren** klicken
3. `smartonomy-landing-elementor.json` auswählen und hochladen

### 2. Seite anlegen

1. **Seiten → Erstellen**, Titel z. B. „Start", **Mit Elementor bearbeiten**
2. In Elementor auf das **Ordner-Symbol** (Bibliothek) klicken → Tab **Meine Templates**
3. Template **„SMARTONOMY – Landing Page (Aiero)"** einfügen
4. Das Template nutzt das Seitenlayout **„Elementor Header/Footer"** – Header und
   Footer des Aiero-Themes bleiben damit erhalten. Alternativ **„Elementor Canvas"**
   wählen, wenn die Seite komplett ohne Theme-Rahmen laufen soll.
5. **Einstellungen → Lesen** → diese Seite als statische Startseite festlegen

### 3. Zusatz-CSS einbinden

Inhalt von `smartonomy-custom.css` einfügen unter:

- **Elementor → Website-Einstellungen (⚙) → Benutzerdefiniertes CSS** (empfohlen, Pro), oder
- **Design → Customizer → Zusätzliches CSS** (ohne Pro)

### 4. Aiero-Theme anpassen

- **Header/Menü:** Im Aiero-Header ein Menü mit Anker-Links anlegen:
  `#vorteile` (Vorteile) · `#leistungen` (Leistungen) · `#preise` (Preise) · `#ablauf` (Ablauf) · `#faq` (FAQ) · `#kontakt` (Termin buchen)
- **Header-CTA:** Aiero-Header-Button auf `#kontakt` verlinken, Farbe Orange `#F97316`
- **Footer:** Im Aiero-Footer eintragen: Kurzbeschreibung
  („KI-Automatisierung für den deutschen Mittelstand."), Kontakt
  (info@smartonomy.de · +49 176 931 40437), Social Links (LinkedIn, Instagram)
  sowie Links auf Impressum, Datenschutz und AGB
- **Theme-Farben** (Customizer / Theme Options → Colors):
  - Primär: `#3B82F6` (Blau)
  - Sekundär: `#6D28D9` (Violett)
  - Akzent/Buttons: `#F97316` (Orange)
  - Dunkler Hintergrund: `#0D1226` (Navy)
  - Heller Hintergrund: `#F8FAFC`
  - Schrift: **Inter** (Google Font, wird auch per CSS geladen)

### 5. Noch zu ergänzen (Assets, die nicht im Template stecken)

- **Hero-Hintergrundbild:** Eigenes Bild in der Hero-Sektion hinterlegen
  (Sektion bearbeiten → Stil → Hintergrund). Aktuell liegt dort ein Navy-Verlauf.
- **Audio-Demo:** In der Sektion „So klingt Ihr KI-Assistent" die eigene MP3
  einfügen (WordPress-Audio-Shortcode im Text-Widget oder ein Audio-Player-Widget).
- **Kontaktformular:** Der CTA-Button verlinkt aktuell auf
  `mailto:info@smartonomy.de`. Für ein echtes Formular z. B. das Aiero/Elementor-
  Formular-Widget oder Contact Form 7 einsetzen und den Button-Link anpassen.
- **Terminbuchung:** Button „Direkt Termin buchen" auf Ihr Buchungstool
  (z. B. Calendly/Cal.com) verlinken.
- **Rechtsseiten:** Impressum, Datenschutzerklärung und AGB als separate
  WordPress-Seiten anlegen und im Footer verlinken.

## Anker-IDs im Template

| Sektion | Anker |
|---|---|
| Hero | `#start` |
| Probleme/Vorteile | `#vorteile` |
| Branchen | `#branchen` |
| Audio-Demo | `#demo` |
| Leistungen | `#leistungen` |
| Ablauf | `#ablauf` |
| Preise | `#preise` |
| ROI-Rechner | `#roi` |
| Kundenstimmen | `#kunden` |
| FAQ | `#faq` |
| Kontakt | `#kontakt` |

## Voraussetzungen

- WordPress ≥ 6.0
- Aiero-Theme aktiv
- Elementor (kostenlose Version genügt)
- Font Awesome ist in Elementor enthalten (Icons der Listen/Boxen)
