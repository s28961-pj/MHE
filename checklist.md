# To Do List:

### Wstęp
- [x] Zanim zaczniesz - proszę przygotować repozytorium.
- [x] Zdecyduj się na temat zadania, który będzie z Tobą do końca zajęć. Tematy mogą się powtarzać, ale najlepiej, aby były w miarę równo rozłożone między uczestników. Można też wybrać jakiś dowolny temat z https://en.wikipedia.org/wiki/List_of_NP-complete_problems, ale niektóre z nich mogą być trudne..
- [x] Nazwę tematu proszę wpisać w komentarzu do zajęć.

- [x] Wybrany temat proszę opisać skrótowo na swoim repozytorium w pliku README.md, oraz wysłać adres repozytorium na email prowadzącego - pantadeusz@pjwstk.edu.pl - proszę w tytule wpisać "MHE Zaoczne 2025", dzięki czemu łatwiej mi będzie to zebrać. ``UWAGA`` - każdy temat będzie trzeba trochę dostosować - wyjaśnię jak to zrobić.
  Przez cały semestr (do ostatniego zjazdu) proszę przygotować projekt zawierający następujące podprojekty oraz eksperymenty. Każdy element na liczbę punktów podaną w nawiasach. Cechy wspólne projektów to:
- [x] Uruchamianie za pomocą linii komend.
- [x] Pobieranie parametrów z linii komend a nie z standardowego wejścia.
- [x] Pobieranie danych (zadanie do rozwiązania) z pliku albo z standardowego wejścia.
- [x] Projekt może być podzielony na oddzielne projekty będące osobnymi programami. Ważne aby miały spójny format wywołania (argumenty/dane...). Dowolny język programowania, ale będę się czepiał wtórnych rozwiązań

### Implementacja problemu optymalizacyjnego (3)
- [ ] Przygotuj swoją funkcję celu dla zadanego problemu.
- [ ] Przygotuj metodę która będzie zwracała bliskie "sąsiedztwo" bieżącego rozwiązania.
- [ ] Przygotuj funkcję która wygeneruje losowe rozwiązanie

### Algorytm pełnego przeglądu (1)
- [ ] Zaimplementuj algorytm pełnego przeglądu. Prawdopodobnie będzie potrzebna metoda generowania kolejnych punktów z dziedziny rozwiązania w taki sposób, aby udało się przejść wszystkie.

### Algorytm wspinaczkowy (1+1*)
- [ ] Zaimplementuj algorytm wspinaczkowy. Zdecyduj się na wersję, albo przygotuj obie:
- [ ] (1) klasyczny z deterministycznym wyborem najlepszego sąsiada punktu roboczego
- [ ] (1) z losowym wyborem sąsiada spośród otoczenia punktu roboczego

### Algorytm tabu (1 + 1*)
- [ ] Należy zaimplementować algorytm Tabu dla swojego problemu. Program powinien pozwalać na podanie rozmiaru tabu (pozwalamy na nieograniczone tabu). Na punkt bonusowy - zaimplementuj cofanie się na liście do ostatniego punktu roboczego z którego można było kontynuować obliczenia.

### Algorytm symulowanego wyżarzania (1)
- [ ] Zaimplementuj algorytm SA dla swojego problemu. Będzie trzeba dobrze zdefiniować, co rozumiesz przez otoczenie punktu roboczego oraz jak "zasymulować" działanie pozwalające na losowanie punktu roboczego za pomocą rozkładu normalnego zamiast jednorodnego. Zachęcam do konsultacji z prowadzącym. Parametrem niech będzie wybór schematu wyżarzania (czyli funkcja temperatury wraz z parametrami).

### Algorytm genetyczny (4 + 1*)
- [ ] Zaimplementuj GA dla Twojego zadania. Może być klasyczny, albo jako program ewolucyjny). Jest tu sporo elementów, dlatego dopuszczam częściowe rozwiązania i każde będę oceniał indywidualnie. Niech będzie:
- [ ] (1) 2 metody krzyżowania
- [ ] (1) 2 metody mutacji
- [ ] (1) 2 warunki zakończenia
- [ ] (1) Główna pętla algorytmu - cały działający algorytm
- [ ] (*1) Elita
  Parametrami niech będzie - wybór metody krzyżowania, mutacji oraz warunku zakończenia. Parametrem niech będzie także liczba osobników w populacji.
  Jeśli algorytm nie będzie działał, a chcesz mieć punkty z podpunktów, to przygotuj funkcje testujące poszczególne metody.

### Algorytm genetyczny - wersja równoległa (1*)
- [ ] Zaimplementuj algorytm genetyczny w wersji zrównoleglonej - zobacz jakie elementy algorytmu można rozbić na niezależne zadania i wykorzystaj całą dostępną moc obliczeniową Twojego komputera. Najłatwiej zrównoleglić proces liczenia funkcji oceny.

### Algorytm genetyczny - wersja wyspowa (1 lub 3*)
- [ ] Zaimplementuj algorytm wyspowy. Niech dodatkowym parametrem będą: liczba wysp, tępo migracji oraz przerwa migracyjna. Schemat łączenia migrantów jest tu dowolny, najłatwiej podmieniać losowego. Na dodatkowe 2 punkty - rozprosz obliczenia na wiele fizycznych maszyn - możesz potem uruchomić eksperyment na pracowni.

### Programowanie genetyczne - demo (1*)
- [ ] Przygotuj przykład pokazujący jak działa programowanie genetyczne. Proszę przygotować przykład inny niż typowe w dokumentacji i na tutorialach (absolutnie nie rób o pogodzie).

### Strategia ewolucyjna (1*)
- [ ] Zaimplementuj strategię ewolucyjną. Przetestuj dla co najmniej 3 funkcji testowych (w tym 2 z lokalnymi optimami) (https://en.wikipedia.org/wiki/Test_functions_for_optimization).

### Eksperyment porównujący metody (2 + ?*)
- [ ] Zaimplementuj skrypt (dowolny język) porównujący przynajmniej 2 metody rozwiązywania Twojego zadania. Im więcej metod sprawdzisz, tym więcej punktów będzie. Wnioski jakie powinieneś dać radę otrzymać to:
- [ ] jaki zestaw parametrów daje najlepsze wyniki dla każdej metody
- [ ] jaka metoda kończy się najszybciej (porównujemy dla najlepszych parametrów)
- [ ] jaka metoda zużywa najmniej zasobów przy takim samym poziomie osiągniętych wyników (porównujemy dla najlepszych parametrów)
- [ ] jaka metoda najszybciej zbiega (porównujemy dla najlepszych parametrów)