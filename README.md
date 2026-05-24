# Keeleõppe Programm

Lihtne Pythoni konsooliprogramm inglise, eesti ja vene keele sõnade õppimiseks.

Programm võimaldab kasutajal:

- valida lähtekeele
- valida sihtkeele
- vastata tõlkimise küsimustele
- saada punkte õigete vastuste eest
- harjutada põhisõnavara

# Funktsioonid

- mitme keele tugi
- sõnavara harjutamine
- sisendi kontrollimine

# Programmis kasutatakse Pythoni põhifunktsioone

- klassid
- objektid
- funktsioonid
- tingimuslaused (`if`)
- tsüklid (`for`)
- listid
- sõnastikud (`dictionary`)
- kasutaja sisend (`input`)
- teksti kuvamine (`print`)

# OOP (objektorienteeritud programmeerimine)

Projekt kasutab objektorienteeritud programmeerimise põhimõtteid.

Objektorienteeritud programmeerimine tähendab,
et programm jagatakse väiksemateks loogilisteks osadeks ehk klassideks.

Selles projektis kasutatakse kolme põhiklassi:

## Word

Klass `Word` hoiab ühe sõna tõlkeid erinevates keeltes.

Näide:

```python
Word("Hello", "Tere", "Привет")
```

See objekt sisaldab:

- ingliskeelset sõna
- eestikeelset tõlget
- venekeelset tõlget

## User

Klass `User` hoiab kasutaja andmeid.

Kasutajal on:

- nimi
- punktid
- sõnade kogumik

Programm salvestab kasutaja punktid ja kasutab neid tulemuste kuvamisel.

## Lesson

Klass `Lesson` vastutab kogu tunni loogika eest.

Selles klassis toimub:

- keelte valimine
- küsimuste kuvamine
- kasutaja vastuste kontrollimine
- punktide lisamine
- lõpptulemuse arvutamine

# Võimalikud tulevased arendused

Tulevikus võiks lisada:

- raskusastmed
- failidesse salvestamise
- juhuslikud sõnad
- taimeri süsteemi
- andmebaasi toe
