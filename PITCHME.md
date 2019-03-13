---?color=linear-gradient(to right, #c02425, #f0cb35)
@title[python]


@snap[west text-45 text-bold text-white]
python
@snapend

@snap[south-west byline text-white text-8]
@quote[Beautiful is better than ugly]
@snapend


---?image=template/img/bg/blue.jpg
@title[GPS-fil]

@snap[north span-100]
@code[ini zoom-05](src/GPS_snippet.txt)
@snapend


---?image=template/img/bg/green.jpg
@title[SOSI-fil]


@snap[north span-100]
@code[ini zoom-05](src/SOSI_snippet.txt)
@snapend


---
@title[programmering for geomatikk]

@snap[west span-100]
### GEO2061<br>Programmering for geomatikk

Obligatorisk emne i bachelor-studiet 2004-2007

@ul
- grunnleggende python-programmering
- bruk av python i ArcGIS
- avløst av java-kurs ved IMT
@ulend
@snapend


---
@title[Vitenskapelig programmering]

@snap[west span-100]
### IMT3881<br>Vitenskapelig programmering

Høynivå vitenskapelig programmering for
@ul
- visualisering av flerdimensjonale data
- lineæralgebra
- optimalisering
- m.m.
- nivå 3-emne
@ulend
@snapend


---?image=images/growth_major_languages.png&size=50%
@title[Popularitet]



---?image=template/img/bg/orange.jpg&position=right&size=50% 100%
@title[agenda]

@snap[west text-16 text-bold text-italic text-orange span-50]
Dagens tema
@snapend

@snap[east text-white span-50]
@ol[split-screen-list text-08](false)
- Om python
- Python i undervisning
- Om Jupyter Notebook
@olend
@snapend



---?image=template/img/bg/green.jpg&position=left&size=60% 100%
@title[Guido van Rossum]

@snap[west span-55 text-11 text-white]
Guido van Rossum<br><br>
@ul[split-screen-list text-08](false)
- lanserte programmeringsspåket python i 1991
- Benevolent Dictator For Life (BDFL)  til 2018
- Fan av<br>“Monty Python’s Flying Circus” 
@ulend
@snapend

@snap[east]
@img[split-screen-img span-55](images/Guido.jpg)
@snapend


---
@title[Guido van Rossum]

@snap[west span-55 byline text-11 text-green]
@quote[I want Python to be more effective for large projects, without losing sight of its use for small projects and teaching]
@snapend

@snap[east]
@img[split-screen-img span-55](images/Guido.jpg)
@snapend



---?image=template/img/bg/pink.jpg&position=left&size=60% 100%
@title[The Zen of Python]

@snap[east text-17 text-bold text-pink span-40]
The Zen<br>of Python
@snapend

@snap[west text-white span-60]
@ul[split-screen-list text-08](false)
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Complex is better than complicated
- Now is better than never
- Readability counts
@ulend
<br>
_*Tim Peters*_
@snapend




---?image=template/img/bg/green.jpg&position=left&size=100% 100%
@title[Et enkelt python-program]
@code[python zoom-21](src/range.py)



---?image=template/img/bg/blue.jpg&position=left&size=100% 100%
@title[Et enkelt C-program]
@code[c zoom-15](src/range.c)

@[3-4,10, zoom-14]
@[5, zoom-14]
@[7-9, zoom-14]



---?image=template/img/bg/blue.jpg&position=left&size=100% 100%
@title[Et kompakt C-program]
@code[c zoom-15](src/range_compact.c)



---?image=template/img/bg/green.jpg
@title[Dynamisk typebestemmelse]

@code[python zoom-15](src/dynamisk.py)



---?image=template/img/bg/green.jpg
@title[Dynamisk typebestemmelse]

@code[python zoom-15](src/dynamisk_output.py)



---?image=template/img/bg/green.jpg
@title[Dynamisk typebestemmelse]

@code[python zoom-15](src/type_conflict.py)



---?image=template/img/bg/green.jpg
@title[Dynamisk typebestemmelse]

@code[python zoom-15](src/type_conflict_output.py)



---?image=template/img/bg/blue.jpg&position=left&size=100% 100%
@title[Et enkelt C-program]
@code[c zoom-15](src/range.c)



---?image=template/img/bg/blue.jpg&position=left&size=40% 100%
@title[Static typing]

@snap[east text-17 text-bold text-blue span-60]
Språk med<br>
"Static typing"
@snapend

@snap[west text-white span-60]
@ul[split-screen-list text-12](false)
- C
- C++
- C#
- Fortran
- Java
@ulend
@snapend



---?image=template/img/bg/green.jpg&position=left&size=40% 100%
@title[Dynamic typing]

@snap[east text-17 text-bold text-green span-60]
Språk med<br>
"Dynamic typing"
@snapend

@snap[west text-white span-60]
@ul[split-screen-list text-12](false)
- Python
- JavaScript
- Perl
@ulend
@snapend


---?image=images/kompilator.png&size=75%
@title[Kompilatorer]



---?image=template/img/bg/green.jpg
@title[Datastrukturer]

@code[python zoom-8](src/datastrukturer.py)



---?image=template/img/bg/green.jpg&position=left&size=40% 100%
@title[Innebygde metoder]
@snap[east text-17 text-bold text-green span-60]
Innebygde metoder på<br>
datastrukturene
@snapend

@snap[west text-white span-60]
@ul[split-screen-list text-12](false)
- størrelse
- sortere
- reversere
- legge til
- slette
- m.m.
@ulend
@snapend



---?image=template/img/bg/green.jpg&position=left&size=50% 100%
@title[Innebygde metoder]
@snap[east text-17 text-bold text-green span-50]
Python kan utvides<br>
med eksterne moduler
@snapend

@snap[west text-white span-60]
@ul[split-screen-list text-12](false)
- matriseregning
- statistikk
- plotting
- maskinlæring
- m.m.m.
@ulend
@snapend

---?image=template/img/bg/pink.jpg&position=left&size=50% 100%
@title[The Zen of Python]

@snap[east text-17 text-bold text-pink span-50]
Python<br>
oppsummert
@snapend

@snap[west text-white span-50]
@ul[split-screen-list text-08](false)
- enkel, kompakt syntaks
- lettlest kode
- dynamisk typebestemmelse
- rike datastrukturer
- store utvidelsesmuligheter
- krever "runtime environment"
@ulend
@snapend






---?color=linear-gradient(to right, #c02425, #f0cb35)
@title[and now..]


@snap[center text-white text-14]
@quote[and now for something completey different](Monty Python Flying Circus)
@snapend


---?image=template/img/bg/green.jpg
@title[createRandomPoints]

@code[python zoom-12](src/createRandomPoints.py)

@[1-5, zoom-14]
@[6, zoom-14]
@[7, zoom-14]
@[8-10, zoom-14]
@[11, zoom-14]


---?image=template/img/bg/green.jpg
@title[createRandomPoints]

@code[python zoom-10](src/NNF.py)

@[1-2, zoom-14]
@[3, zoom-14]
@[4, zoom-14]
@[5, zoom-14]
@[6, zoom-14]
@[7, zoom-14]
@[8, zoom-14]
@[9-11, zoom-14]
@[12, zoom-14]



---?image=template/img/bg/green.jpg&position=right&size=40% 100%
@title[Ressurser]

@snap[east text-17 text-bold text-white span-40]
Veien<br>videre
@snapend

@snap[west span-60]
@ul[split-screen-list text-08](false)
- [www.python.org](https://www.python.org/)
- [www.anaconda.org](https://www.anaconda.com/)
- [folk.ntnu.no/sverrsti/python_intro](https://folk.ntnu.no/sverrsti/python_intro/)
@ulend
@snapend