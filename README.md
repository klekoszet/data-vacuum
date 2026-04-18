# [EN] Survey Data Cleaner - Automated Quality Control

A professional Quality Control (QC) tool for Data Processing. This Python application automates the detection and removal of low-quality responses in survey datasets (`.sav`). It implements industry-standard data cleaning algorithms, including multivariate outlier detection.

## 🚀 Key Features
- **Speeder Detection:** Identifies respondents who completed the survey too quickly based on a customizable median time threshold.
- **Straightliner Detection:** Calculates row variance across matrix questions to flag respondents giving identical answers (flatlining).
- **Long String Analysis:** Finds the maximum consecutive identical responses in grid questions.
- **Missing Data Filter:** Flags cases exceeding a specified percentage of missing values.
- **Mahalanobis Distance:** Uses `scipy.stats` to calculate multivariate outliers, identifying unusual response patterns across multiple numeric variables based on Chi-Square p-values.
- **Scrollable UI:** A user-friendly graphical interface capable of handling datasets with hundreds of variables effortlessly.

## 🛠️ Requirements
- Python 3.x
- Libraries: `pandas`, `numpy`, `pyreadstat`, `scipy`

`pip install pandas numpy pyreadstat scipy`

## 📖 How to Use
1. Run `python odkurzacz_danych.py`.
2. Load the raw SPSS dataset (`.sav`).
3. Toggle the desired quality control filters and adjust their specific thresholds.
4. Select the relevant variables for each test using the checkbox panels.
5. Click the execution button. The tool will filter the data, generate a summary report, and save the clean dataset to the output directory.

---

# [PL] Odkurzacz Danych - Automatyczna Kontrola Jakości (QC)

Profesjonalne narzędzie do Kontroli Jakości (QC) dla działów Data Processing. Aplikacja w Pythonie automatyzująca proces wykrywania i usuwania problematycznych obserwacji z baz ankietowych (`.sav`). Implementuje rynkowe standardy czyszczenia danych, włączając w to detekcję wielowymiarowych wartości odstających.

## 🚀 Kluczowe Funkcje
- **Detekcja Speederów:** Identyfikuje obserwacje z nienaturalnie krótkim czasem wypełnienia, bazując na konfigurowalnym progu mediany czasu.
- **Detekcja Straightlinerów:** Oblicza odchylenie standardowe wierszy dla pytań matrycowych, w celu identyfikacji braku wariancji w odpowiedziach.
- **Analiza Long Strings:** Wyszukuje najdłuższe ciągi identycznych odpowiedzi w wyznaczonych bateriach pytań.
- **Filtr Braków Danych:** Weryfikuje i odrzuca obserwacje przekraczające dozwolony próg systemowych braków danych.
- **Odległość Mahalanobisa:** Wykorzystuje bibliotekę `scipy` do wyliczania wielowymiarowych wartości odstających w modelu numerycznym (weryfikacja na bazie p-value rozkładu chi-kwadrat).
- **Interfejs UI:** Zoptymalizowany pod kątem dużych baz danych, wykorzystujący przewijane panele wyboru zmiennych.

## 🛠️ Wymagania
- Python 3.x
- Biblioteki: `pandas`, `numpy`, `pyreadstat`, `scipy`

`pip install pandas numpy pyreadstat scipy`

## 📖 Instrukcja Obsługi
1. Uruchom skrypt `odkurzacz_danych.py`.
2. Wczytaj surowy plik bazy danych SPSS (`.sav`).
3. Aktywuj wymagane filtry badawcze i dostosuj ich parametry progowe.
4. Zaznacz zmienne podlegające analizie na listach wyboru.
5. Uruchom proces czyszczenia. Program odfiltruje bazę, wyświetli podsumowanie i zapisze gotowy plik wynikowy w folderze docelowym.
