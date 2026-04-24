# [EN] Survey Data Cleaner - Automated Quality Control

## 1. Project Goal
A local GUI application designed to automate Quality Control (QC) and data cleaning for quantitative survey research (`.sav` files). The tool implements industry-standard data validation algorithms—from basic speeder detection to advanced multivariate outlier identification—ensuring the high methodological integrity of research datasets.

## 2. Vibe Coding & Development Approach
This project was built using the "vibe coding" methodology in collaboration with AI. As the domain expert, my focus was strictly on the methodological architecture rather than manually writing Tkinter boilerplate. I defined the statistical rules for exclusion (e.g., standard deviation thresholds for straightliners, Chi-Square p-value limits for Mahalanobis distance) and critically evaluated the AI-generated code to ensure the statistical transformations were mathematically sound. This demonstrates how AI can be utilized to quickly prototype robust analytical tools while human oversight guarantees methodological correctness.

## 3. Key Features
- **Speeder Detection:** Flags respondents who completed the survey suspiciously fast, based on a customizable percentage of the median completion time.
- **Straightliner Detection:** Calculates row variance across matrix questions to identify respondents giving identical answers (flatlining).
- **Long String Analysis:** Finds the maximum consecutive identical responses in defined grid questions.
- **Missing Data Filter:** Flags cases exceeding a specified threshold of missing values.
- **Multivariate Outliers (Mahalanobis Distance):** Uses `scipy.stats` to calculate Mahalanobis distance, identifying unusual response patterns across a numerical model based on Chi-Square distribution p-values.
- **Optimized UI:** A scrollable, checkbox-based interface built to comfortably handle datasets with hundreds of variables.

## 4. Security & Data Protection
**Zero-Cloud Architecture.** Data cleaning is inherently sensitive. This script runs 100% locally on the user's machine using `pandas` and `pyreadstat`. No raw respondent data is sent to external APIs, language models, or cloud servers. This architecture ensures absolute compliance with GDPR and university/corporate data ethics standards.

## 5. Performance & Limitations
- **In-Memory Processing:** The application processes the dataset entirely in RAM. It is highly performant for typical survey sample sizes (thousands of respondents), but extremely massive datasets may hit system memory limits.
- **Environment Limit:** The script relies on a hardcoded output directory (`C:\DP_Bazy`), restricting its out-of-the-box use to Windows OS.
- **Complete Case Analysis:** Currently, the Mahalanobis distance calculation strictly drops NA values (`dropna()`) for the numerical model, which may reduce the evaluated sample size if missing data is prevalent.

## 6. Future Roadmap
To continue evolving the tool, the following upgrades are planned:
- **Dynamic Pathing:** Replacing the hardcoded output path with a user-selected directory via GUI.
- **Detailed Exclusion Logs:** Exporting a `.csv` or `.xlsx` report that flags exactly which rows were removed and by which specific QC test, allowing for better auditing.
- **Imputation Options:** Adding the ability to impute missing values (e.g., mean/median substitution) before running the Mahalanobis test to preserve sample size.

## 🛠️ Requirements & Execution
- Python 3.x
- Libraries: `pip install pandas numpy pyreadstat scipy`
- Run: `python odkurzacz_danych.py`

---

# [PL] Odkurzacz Danych - Automatyczna Kontrola Jakości (QC)

## 1. Cel projektu
Lokalna aplikacja z interfejsem graficznym stworzona do automatyzacji kontroli jakości (QC) i czyszczenia baz danych z badań ilościowych (pliki `.sav`). Narzędzie implementuje rynkowe standardy walidacji danych – od podstawowej detekcji speederów po zaawansowane wyszukiwanie wielowymiarowych wartości odstających, zapewniając wysoką rzetelność metodologiczną analizowanego materiału.

## 2. Podejście do tworzenia (Vibe Coding)
Aplikacja powstała w modelu "vibe codingu" przy ścisłej współpracy z AI. Zamiast skupiać się na ręcznym pisaniu kodu interfejsu, przyjąłem rolę architekta metodologicznego. Zdefiniowałem statystyczne zasady odrzucania obserwacji (np. progi wariancji dla straightlinerów, wykorzystanie rozkładu chi-kwadrat przy odległości Mahalanobisa) i poddałem krytycznej weryfikacji wygenerowane algorytmy. Projekt pokazuje, jak kompetencje badawcze pozwalają skutecznie kierować modelami AI w celu tworzenia profesjonalnych narzędzi analitycznych, gwarantując poprawność matematyczną całego procesu.

## 3. Kluczowe Funkcje
- **Detekcja Speederów:** Identyfikuje zbyt szybkie wypełnienia bazując na konfigurowalnym procencie od mediany czasu z całej próby.
- **Detekcja Straightlinerów:** Oblicza odchylenie standardowe wierszy w pytaniach matrycowych, identyfikując brak wariancji.
- **Analiza Long Strings:** Wyszukuje maksymalne ciągi identycznych odpowiedzi w zdefiniowanych blokach pytań.
- **Filtr Braków Danych:** Odrzuca obserwacje przekraczające dozwolony próg systemowych braków.
- **Odległość Mahalanobisa:** Wykorzystuje bibliotekę `scipy` do identyfikacji nietypowych wzorców odpowiedzi w modelu numerycznym, bazując na p-value.
- **Zoptymalizowany Interfejs:** Przewijane panele z checkboxami ułatwiające pracę z bazami liczącymi setki zmiennych.

## 4. Bezpieczeństwo i ochrona danych
**Brak integracji z chmurą.** Proces czyszczenia danych wymaga najwyższych standardów poufności. Skrypt działa w 100% lokalnie za pomocą bibliotek `pandas` i `pyreadstat`. Żadne dane respondentów nie opuszczają urządzenia i nie są wysyłane do zewnętrznych API. Gwarantuje to pełną zgodność z wymogami RODO oraz standardami etyki badań naukowych i rynkowych.

## 5. Wydajność i ograniczenia
- **Przetwarzanie w RAM:** Aplikacja ładuje całą bazę do pamięci operacyjnej. Działa błyskawicznie dla typowych prób badawczych, jednak przy gigantycznych zbiorach danych może napotkać limity sprzętowe.
- **Zależność od Windows:** Ze względu na zaszytą w kodzie ścieżkę zapisu wyników (`C:\DP_Bazy`), program w obecnej formie jest dostosowany do systemu Windows.
- **Obsługa Braków (Mahalanobis):** Obecnie algorytm liczący odległość Mahalanobisa automatycznie odrzuca obserwacje z brakami danych (`dropna()`) w wybranym modelu, co w specyficznych bazach może zawężać pulę testowanych przypadków.

## 6. Perspektywy rozwoju
Aplikacja posiada otwartą architekturę, a plany jej rozbudowy obejmują:
- **Wybór folderu docelowego:** Zastąpienie stałej ścieżki zapisu oknem dialogowym w GUI.
- **Raport wykluczeń:** Dodanie eksportu pliku `.csv` / `.xlsx` z logami (ID respondenta + powód odrzucenia), co ułatwi audytowanie usuniętych rekordów.
- **Imputacja danych:** Wprowadzenie opcji zastępowania braków danych (np. średnią/medianą) przed obliczeniem odległości Mahalanobisa, aby nie tracić wielkości próby.

## 🛠️ Wymagania i Uruchomienie
- Python 3.x
- Biblioteki: `pip install pandas numpy pyreadstat scipy`
- Uruchomienie: `python odkurzacz_danych.py`
