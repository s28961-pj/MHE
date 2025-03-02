# Metaheurystyki

`Heurystyka` - jest specjalizowana metoda rozwiązywania konkretnego problemu. Znajduje dobre rozwiązania przy akceptowalnym wysiłku, bez gwarancji osiągnięcia optymalności celu.

`Metaheurystyka` - ogólna metoda służąca za szablon do konstrukcji heurystyki rozwiązującej dowolny problem dający się opisać za pomocą pojęć z tej metody.

<details>
  <summary>
    O przedmiocie MHE
  </summary>

  Nauczymy się praktycznego zastosowania metaheurystyk. Poznamy w jakich sytuacjach warto spróbować zastosować rozwiązania z tej dziedziny, a kiedy nie. Zajmiemy się:<br>
  - Programowanie genetyczne<br>
  - Programowanie ewolucyjne<br>
  - Strategie ewolucyjne<br>
  - Symulowane wyżarzanie<br>
  - Algorytm genetyczny<br>
  - Algorytm Tabu<br>

  ### Co na zajęciach
Wykład jest przygotowaniem do laboratoriów. Na wykładzie omawiane będą algorytmy, metody i ich właściwości. Przedstawione zostaną także elementy teorii które są konieczne do zrozumienia tematu.
Językiem wykładowym będzie C++17 oraz Python. Zachęcam do poznania obu.
Zajęcia są zebrane w czterech zjazdach. 
 
Ćwiczenia proszę traktować jako okazję do dyskusji/pracy i oddawania projektów.
</details>

<details>
  <summary>
    Zasady zaliczenia
  </summary>
  
  ### Laboratoria
Praktyczne ćwiczenia/laboratoria dążące do stworzenia kompletnego projektu. Każdy uczestnik powinien wybrać sobie temat przewodni. Będą dodatkowe punkty przyznawane za aktywność czy to na ćwiczeniach czy na wykładzie - w losowych momentach.
W oddzielnym wpisie przedstawię co jest do zrobienia do końca semestru.
Egzamin - ze wszystkiego.
Jeśli udało się uzyskać ocenę co najmniej 4.0 z lab, to może ona zostać przepisana na ocenę z wykładu.

Materiały:
- MHE na github (pantadeusz)
- Slajdy z wykładów w plikach na Teams
- Stare zajęcia dla trybu dziennego - http://szuflandia.pjwstk.edu.pl/~pantadeusz/zajecia/mhe/2019_2020_dzienne.old/
- https://pl.frwiki.wiki/wiki/M%C3%A9taheuristique

Książki
(dostępne w bibliotece)
Każdą z tych pozycji polecam. Ja poznawałem ten temat zapoznając się z książkami w takiej kolejności jak wymienione. Natomiast wydaje mi się że lepiej zacząć w odwrotnej kolejności.
- A. Michalewicz - Algorytmy genetyczne + struktury danych = programy ewolucyjne
- D. A. Goldberg - Algorytmy genetyczne i ich zastosowanie
- J. Arabas - Wykłady z Algorytmów Ewolucyjnych

</details>

<details>
  <summary>
    Egzamin - zakres
  </summary>
  
  Egzamin pisemny. Szybkie przeglądowe zadania. Tematy poniżej:  
- Co to jest heurystyka, a co to jest metaheurystyka
- Schematy (pseudokod) algorytmów:
  - algorytm wspinaczkowy
  - algorytm symulowanego wyżarzania
  - algortym genetyczny (wersja klasyczna na ciągach bitów i wersja dostosowana - program ewolucyjny)
  - algorytm tabu
  - strategia ewolucyjna
- Elementy metaheurystyk
    - funkcja celu
    - funkcja oceny
    - selekcja
    - mutacja
    - krzyżowanie
    - rekombinacja
    - warunek zakończenia (oraz oczywiście co najmniej 2 przykłady)
    - populacja początkowa (oraz jak ją tworzymy: albo losowo, albo dostosowaną do zadania)
    - eksploracja a eksploatacja
    - genotyp
    - fenotyp
  - Cechy i właściwości
    - globalne i lokalne optimum
    - jaki algorytm świetnie się zrównolegla
    - o co chodzi w wyspowym algorytmie genetycznym
    - jaka metoda stosuje automatyczne dostosowanie zasięgu mutacji
    - jaka metoda zawsze zatrzyma się w minimum lokalnym
    - przedwczesna zbieżność
    - superosobnik
    - metoda ruletki
    - selekcja turniejowa
    - jakie są pożądane cechy selekcji
    - w jaki sposób stwierdzić jaki zestaw parametrów metody jest najlepszy
    - co oznaczają znaczki mu lambda rho w strategiach ewolucyjnych?
    - mamy metaheurystykę i metodę dokładną rozwiązania pewnego konkretnego problemu. Co wybieżemy jeśli:
    - chcemy wykonać obliczenia jak najszybciej.
    - chcemy wykonać obliczenia dokładnie.
    - mamy metaheurystykę i metodę dokładną rozwiązania pewnego konkretnego problemu. W jakich przypadkach zastosujemy metaheurystykę, a w jakich metodę dokładną?
    - która metoda działa szybciej - metoda pełnego przeglądu, czy algorytm (tu wstaw dowolną metaheurystykę)?
    - która metoda daje dokładniejsze wyniki - metoda pełnego przeglądu, czy algorytm genetyczny?
    - jaka metoda metaheurystyczna jest najlepsza? Uzasadnij (tak, tu jest haczyk  ).
    - jak powinien ogólnie wzrastać czas obliczeń dla metaheurystyki. Kiedy nie ma sensu stosować metaheurystyki?.
    - w jakiej metaheurystyce korzystamy z reprezentacji drzewiastej chromosomów.
  - programowanie genetyczne, co to jest?
</details>

<details>
  <summary>
    Ćwiczenia - zakres
  </summary>
  
  Projekt zaliczamy na zasadzie "obrony", należy znać każdą linijkę kodu oddawanego projektu pod groźbą niezaliczenia projektu.
Powyższy wymóg podyktowany jest praktyczną niemożliwością innej weryfikacji samodzielnej pracy. Tak więc, nawet kod który byłby wykorzystany z zajęć musi być znany. Sugeruję jednak po swojemu próbować zrobić rozwiązania i dzięki temu znać wszystko "na wylot".

`Każde oddane zadanie do przedostatniego naszego spotkania jest punktowane ze współczynnikiem 1.25 (czyli dostajesz 25% punktów gratis).`

100% punktów to 15, tak więc aby dostać 5 należy zrobić jedno zadanie z * albo oddać wcześniej.

- [x] Zanim zaczniesz - proszę przygotować repozytorium.
- [x] Zdecyduj się na temat zadania, który będzie z Tobą do końca zajęć. Tematy mogą się powtarzać, ale najlepiej, aby były w miarę równo rozłożone między uczestników. Można też wybrać jakiś dowolny temat z https://en.wikipedia.org/wiki/List_of_NP-complete_problems, ale niektóre z nich mogą być trudne..
- https://en.wikipedia.org/wiki/Dominating_set
- https://en.wikipedia.org/wiki/Minimum_k-cut
- https://en.wikipedia.org/wiki/Independent_set_(graph_theory)
- https://en.wikipedia.org/wiki/Maximum_cut
- https://en.wikipedia.org/wiki/Graph_coloring
- https://en.wikipedia.org/wiki/Clique_problem
- https://en.wikipedia.org/wiki/Subset_sum_problem
- https://en.wikipedia.org/wiki/3-partition_problem
- https://en.wikipedia.org/wiki/Bin_packing_problem
- https://en.wikipedia.org/wiki/Light_Up_(puzzle)
- https://en.wikipedia.org/wiki/Nonogram
- [x] Nazwę tematu proszę wpisać w komentarzu do zajęć. 

- [ ] Wybrany temat proszę opisać skrótowo na swoim repozytorium w pliku README.md, oraz wysłać adres repozytorium na email prowadzącego - pantadeusz@pjwstk.edu.pl - proszę w tytule wpisać "MHE Zaoczne 2025", dzięki czemu łatwiej mi będzie to zebrać. ``UWAGA`` - każdy temat będzie trzeba trochę dostosować - wyjaśnię jak to zrobić.
Przez cały semestr (do ostatniego zjazdu) proszę przygotować projekt zawierający następujące podprojekty oraz eksperymenty. Każdy element na liczbę punktów podaną w nawiasach. Cechy wspólne projektów to:
- [ ] Uruchamianie za pomocą linii komend.
- [ ] Pobieranie parametrów z linii komend a nie z standardowego wejścia.
- [ ] Pobieranie danych (zadanie do rozwiązania) z pliku albo z standardowego wejścia.
- [ ] Projekt może być podzielony na oddzielne projekty będące osobnymi programami. Ważne aby miały spójny format wywołania (argumenty/dane...). Dowolny język programowania, ale będę się czepiał wtórnych rozwiązań

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
Wnioski poprzyj wykresami i wynikami eksperymentów. Przygotuj się do pokazania jak w automatyczny sposób powtórzyć eksperyment. Ważne - przyznanie jakiegokolwiek punktu uzależniam od przygotowania wykresu krzywej zbieżności.
</details>
