# [EN] Survey Data Cleaner (QC) - Automated Quality Control
A professional Quality Control (QC) tool for Data Processing specialists. This Python application automates the detection and removal of fraudulent or low-quality respondents in survey datasets (`.sav`). It implements industry-standard data cleaning algorithms, including multivariate outlier detection.

## 🚀 Key Features
- **Speeder Detection:** Identifies respondents who completed the survey too quickly based on a customizable median time threshold.
- **Straightliner Detection (Flatlining):** Calculates row variance across matrix questions to flag respondents giving identical answers.
- **Long String Analysis:** Finds the maximum consecutive identical responses in grid questions.
- **Missing Data Filter:** Flags cases exceeding a specified percentage of missing values.
- **Mahalanobis Distance (Multivariate Outliers):** Uses `scipy.stats` to calculate the Mahalanobis distance, identifying unusual response patterns across multiple numeric variables (using Chi-Square p-values).
- **Scrollable Checkbox UI:** A user-friendly graphical interface capable of handling hundreds of variables effortlessly.

## 🛠️ Requirements
- Python 3.x
- Libraries: `pandas`, `numpy`, `pyreadstat`, `scipy`

pip install pandas numpy pyreadstat scipy
📖 How to Use
Run python odkurzacz_danych.py.

Click Wczytaj bazę SPSS to load your raw .sav file.

Toggle the filters you want to apply and adjust their specific thresholds.

Select the relevant variables for each test using the scrollable checkbox panels.

Click URUCHOM CZYSZCZENIE I ZAPISZ. The tool will remove bad cases and save the clean dataset to C:\DP_Bazy\, providing a detailed summary report.

[PL] Odkurzacz Danych - Automatyczna Kontrola Jakości (QC)
Profesjonalne narzędzie do Kontroli Jakości (QC) dla specjalistów Data Processing. Aplikacja w Pythonie automatyzująca proces wykrywania i usuwania oszustów oraz respondentów niskiej jakości z baz ankietowych (.sav). Implementuje rynkowe standardy czyszczenia danych, włączając w to detekcję wielowymiarowych wartości odstających.

🚀 Kluczowe Funkcje
Detekcja Speederów: Identyfikuje osoby, które wypełniły ankietę zbyt szybko, bazując na ułamku mediany czasu.

Detekcja Straightlinerów (Choinki): Oblicza odchylenie standardowe wierszy dla pytań matrycowych, aby wyłapać brak wariancji w odpowiedziach.

Analiza Long Strings: Wyszukuje najdłuższe ciągi identycznych odpowiedzi w bateriach pytań.

Filtr Braków Danych: Odrzuca ankiety przekraczające dozwolony procent "Missing Values".

Odległość Mahalanobisa: Wykorzystuje bibliotekę scipy do wyliczania wielowymiarowych wartości odstających w modelu numerycznym (na bazie p-value rozkładu chi-kwadrat).

Interfejs oparty na checkboxach: Wygodne panele wyboru zmiennych, które bez problemu radzą sobie z bazami zawierającymi setki pytań.

🛠️ Wymagania
Python 3.x

Biblioteki: pandas, numpy, pyreadstat, scipy

Bash
pip install pandas numpy pyreadstat scipy
📖 Instrukcja Obsługi
Uruchom plik odkurzacz_danych.py.

Kliknij Wczytaj bazę SPSS, aby załadować surowy plik .sav.

Włącz wybrane filtry badawcze i dostosuj ich progi odrzucenia.

Zaznacz zmienne do analizy na wygodnych, przewijanych listach.

Kliknij URUCHOM CZYSZCZENIE I ZAPISZ. Program usunie oszustów, wygeneruje raport z czyszczenia i zapisze czystą bazę w folderze C:\DP_Bazy\.
