# Curs 7_1_2: API, RestAPI, HTTP
## 📝 OBIECTIVE
- Virtual environments
- Sa intelegem ce este un API
- Sa discutam despre ce reprezinta Rest/Restful API


## 📌 Virtual environments
- Este folosit pentru a gestiona python packages pentru diferite
proiecte.
- Avantaje virtual environment:
  - putem descarca pachete in proiectul nostru fara privilegii de administrator
  - putem crea un pachet cu aplicatia noastra si ulterior o putem partaja cu alti programatori
  - putem crea cu usurinta o lista de dependinte si subdependinte intr-un fisier
, ceea ce face mai usor pentru alti programatori sa reproduca/dezvolte
si sa instaleze toate dependintele utilizate de noi in virtual environment
- Instalare virtualenv (adica programul care ne ajuta sa cream si sa folosim un virtual env)
  - putem folosi comanda: pip install virtualenv
- Avem 3 parti importante in folosirea lui:
1. Creare: python -m venv <nume_folder_venv> - aici de obicei
folosim env/venv/myenv pentru acel nume de folder, sa zicem de exemplu
ca il numim myenv. Crearea se face o singura data!
2. Activare: trebuie sa il activam ori de cate ori avem nevoie
sa rulam proiectul, sa instalam o librarie; comanda de activare e diferita in functie
de sistemul de operare:
- OSX: source myenv/bin/activate
- Windows Powershell: myenv/Scripts/Activate.ps1
- Windows cmd/Pycharm Terminal: myenv/Scripts/activate.bat
3. Dezactivare: asta o putem face cand vrem in acelasi terminal sa trecem
sa lucram la un alt proiect, comanda e: deactivate

## 🔶 Cum functioneaza internetul?
- **Internetul** este o rețea globală de calculatoare interconectate,
care permite oamenilor din întreaga lume să comunice,
să acceseze informații și să împărtășească resurse.
- Pentru a accesa informatiile de pe internet, utilizam browser-ul.
- Browser-ul ne permite sa accesam pagini web, sa vizualizam continutul acestora si
sa interactionam cu el.
- Codul sursa/implementarea aplicatiilor web este stocate pe **servere** (calculatoare).

- Ce se intampla cand accesam o pagina web?
1. Utilizatorul introduce in browser un link/adresa web a site-ului
2. **Browser-ul (client)** face un **request/o cerere** catre **server-ul** care contine codul sursa al site-ului cerut.
- Cererea se face prin **protocolul HTTP/HTTPS**
- Serverul analizeaza/proceseaza cererea primita si trimite
un **raspuns/response** clientului/browser-ului.
- Browser-ul interpreteaza raspunsul si afiseaza rezultatul.

## 🔶 Structura de baza a unei aplicatii web
- 3 layere
1. Layer-ul de prezentare / Front-end / UI
2. Layer-ul de business logic / Back-end
3. Layer-ul de stocare / baza de date

- Front-end-ul comunica cu back-end-ul prin intermediul api-urilor

## 🔶 API
- **API (Application Programming Interface)**
- Reprezinta un set de reguli si protocoale care **permit aplicatiilor
software sa comunice intre ele**
- **Codul care defineste si implementeaza modul in care 2 aplicatii
pot interactiona**
- Un **"intermediar" / "pod de legatura"** intre **user/client** si
**resursele/servicii** pe care doreste sa le utilizeze
- Un API in general este o aplicatie fara partea de prezentare (UI)
care permite comunicarea intre client si server prin intermediul unor reguli.
- Un API poate sa **expuna** unul sau mai multe **url-uri/endpoint-uri**
prin care comunicam cu partea de logica.
- Exemplu 1: un API contine un link care ne expune o lista cu carti.
- Exemplu 2: 
1. Un user intra pe facebook si vrea sa vada o postare.
2. Face **o cerere/ HTTP request** ca sa vada postarea.
3. Pentru asta, aplicatia facebook ne expune un api care contine un link (ex:
https://wwww.facebook.com/posts/cosmina/post1) care ne returneaza acea postare.
4. Aceasta postare este returnata sub forma unui **raspuns HTTP**.
5. Raspunsul HTTP este apoi procesat de catre UI si 
astfel putem vedea postarea ceruta.

## 🔶 HTTP/HTTPS

- HTTP/S = Hypertext Transfer Protocol/ Secure
- Protocol de comunicare intre client si server
- Ne ajuta sa transferam informatii/date prin retea

## 🔶 HTTP Request
- Partile componente ale unui request HTTP:
1. request URL/URI (aka adresa/endpoint, de ex: https://wwww.facebook.com/posts/cosmina/post1)
2. metoda (GET/POST/PUT/DELETE/...)
3. headers: detalii despre mesaj
4. request body: mesajul requestului 
(in cazul requestului POST asa se trimit datele)

## 🔶 HTTP Response
- Partile componente ale unui response HTTP:
1. status code:
- informational: 100 - 199
- successful: 200 - 299
- redirectional: 300 - 399
- client side error: 400 - 499 
- server side error: 500 - 599
2. response body: mesajul cu informatia/resursa ceruta

## 🔶 Status codes
- informational: 100 - 199
- successful: 200 - 299
- redirectional: 300 - 399
- client side error: 400 - 499 
- server side error: 500 - 599

- Cele mai folosite:

  - 200 OK - succes - de obicei când se cer date de la server
  - 201 Created - success - când se pun date în server
  - 204 No Content - success - de obicei când ștergem ceva
  - 400 Bad request - ceva nu a mers bine, probabil valori invalide pentru parametri
  - 401 Unauthorized - nu suntem logați în app
  - 403 Forbidden - suntem logați dar nu avem drepturi de edit de exemplu
  - 404 Not Found - nu găsește endpoint - probabil
  - 408 Request Timeout - a durat prea mult până să ajungă la server requestul
  - 500 Internal Server Error - requestul ajunge la server dar cel mai probabil este un bug
  - 503 Service Unavailable - serverul e oprit pentru mentenanță de exemplu

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


## 🔶 CRUD Operations
- sunt operatiile care pot fii facute pe o baza de date si sunt aferente
metodelor HTTP
- Create: adaugarea unei noi intrari in DB - POST
- Read: citim intrari din DB - GET
- Update: actualizarea unei/unor intrari din DB - PUT/PATCH
- Delete: stergerea unei intrari din DB - DELETE 

## 🔶 Interactiune API
- Manual: Postman
- Din cod: libraria requests din Python

## 🔶 Instalare Postman
- https://www.postman.com/downloads/

## 🔶 Exemplu de API pentru testare: 
- https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

## 🔶 REST = REpresentational State Transfer
- set de constrangeri arhitecturale utilizate in web development
pentru a crea servicii web
- e un design pattern pt API-uri
- implementeaza modelul request-response 
(mai exista si alte modeluri de comunicaare pe internet
precum websockets): la fiecare mesaj de request al clientului,
serverul trimite un raspuns care contine si o resursa 

- request = mesaj trimis de catre client/user catre un server
pentru a initia o actiune (de ex: user cere o resursa de la server - profilul cuiva pe fb)
- response = mesaj trimis ca raspuns de server

- Principalele constrangeri ale API-urilor RESTful 
(pt ca un API sa fie REST, trebuie sa le respecte):
1. Uniform interface (interfata uniforma):
- toate requesturile catre aceeasi resursa trebuie sa arate la fel
indiferent de unde e facut request-ul.
- informatiile unei resurse apartin unui singur identificator (URI / URL)
- mesajele nu trebuie sa fie mari,
dar trebuie sa contina toata informatia de care are nevoie clientul

2. Client-server decoupling (client decuplat de server):
- client si server independente, fiecare avand propria aplicatie
(de ex: o app Django/Flask/DRF/FastAPI/.. 
scrisa in Python pe partea de backend (server),
si o app React/Angular/.. scrisa in JS pe frontend (client))
- clientul cunoaste doar URI/URL-ul (endpoint/locatie) resursei
pe care o cere si interactioneaza cu 
serverul doar prin request-uri la aceste endpoint
- server nu poate trimite mesaje fara sa-i fie cerute
in prealabil de catre client

3. Statelessness (nu are stare):
- fiecare request trebuie sa contina toate informatia necesara
pentru a putea fi procesat de server
- nu exista sesiuni, serverul nu are voie sa stocheze date
referitoare la requestul unui client 
(la fiecare request clientul trebuie sa zica cine e)

4. Cacheability (abilitatea de cache):
- cand e posibil, resursele ar trebui sa fie cache-uite
(salvate) pe client sau server pt a imbunatati
performanta in requesturi (de ex: pe un site librarie,
daca user cere succesiv lista de carti ale aceluiasi autor)
aceasta sa va cache-ui si se va returna ulterior
din memoria cache si nu din DB)
- raspunsurile serverului trebuie sa mentioneze daca cache e activ

5. Layered system architecture (arhitectura de sistem pe niveluri):
- req si resp trec prin mai multe niveluri intermediare
(de ex: client->securitate->servicii->DB->date)
6. Code on demand:
- in general REST API trimite resurse statice,
dar sunt cazuri cand serverul trimite cod executabil
sub forma unui script JS 
