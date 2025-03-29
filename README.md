# Skaitļu Secības Spēle

Interaktīva stratēģijas spēle, kurā divi spēlētāji (cilvēks un AI) pēc kārtas izņem skaitļus no nejauši ģenerētas virknes. Spēlē tiek izmantots Min-Max vai Alpha-Beta algoritms, lai AI pieņemtu optimālus lēmumus.

---

## Spēles noteikumi

- Spēles sākumā tiek nejauši ģenerēta skaitļu virkne (skaitļi no 1 līdz 4).
- Virknes garumu (15–25) spēles sākumā nosaka cilvēks-spēlētājs.
- Katrs spēlētājs sāk ar 100 punktiem.
- Gājienā spēlētājs izņem vienu skaitli no virknes:
  - Ja skaitlis ir **pāra**: no sava punktu skaita tiek atņemta **2 × skaitlis**.
  - Ja skaitlis ir **nepāra**: tas tiek **pieskaitīts pretinieka** punktiem.
- Spēle beidzas, kad visi skaitļi ir izņemti.
- Uzvar tas, kuram **mazāk punktu**. Neizšķirts, ja punktu skaits vienāds.

---

## Funkcionalitāte

- **Galvenā izvēlne**: iespēja sākt spēli.
- **AI algoritma izvēle**: Min-Max vai Alpha-Beta.
- **Pirmais gājējs**: lietotājs vai dators.
- **Virknes garuma izvēle**: no 15 līdz 25.
- **Spēles gaita**: vizuāla interfeisa pogas, kas atspoguļo virknes skaitļus.
- **AI gājiens**: tiek veikts automātiski pēc nelielas aiztures.
- **Rezultāta ekrāns**: paziņo uzvarētāju vai neizšķirtu un sniedz iespēju sākt no jauna vai iziet.

---

## Instalācija un palaišana

1. Klonē repozitoriju:
```bash
git clone https://github.com/DanielsStulpe/MIP-43grupa
cd MIP-43grupa
```

2. Palaid spēli:
```bash
python game.py
```

---

## Failu apraksts

- `game.py` — galvenais GUI interfeiss, spēles plūsmas vadība.
- `node.py` — datu struktūra, spēles loģika, punktu aprēķins.
- `algorithms.py` — AI algoritmu (Min-Max, Alpha-Beta) realizācija.

---

## Izmantotās tehnoloģijas

- Python 3
- Tkinter (GUI izveidei)

---

## Autori

- Daniels Stulpe 231RDB204
- Krišjānis Kugrēns 231RDB307
