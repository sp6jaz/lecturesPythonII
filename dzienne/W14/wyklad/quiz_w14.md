# Quiz W14 — LLM i AI w analizie danych

**Temat:** Powtórka W13 (scikit-learn, Plotly, Polars) + nowy materiał W14 (LLM, API AI, prompty)
**Czas:** 5 minut | **Forma:** kartka lub Mentimeter

---

## Pytania (do wyświetlenia na projektorze — po jednym)

---

### Pytanie 1 (powtórka W13 — scikit-learn)

Po uruchomieniu poniższego kodu co zwróci `y_pred`?

```python
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans.fit(X)
y_pred = kmeans.labels_
print(y_pred)
```

**A)** Błąd — `KMeans` wymaga etykiet `y` do nauczenia się

**B)** Tablicę liczb zmiennoprzecinkowych — przewidywane odległości od centroidów

**C)** Tablicę liczb całkowitych — etykietę klastra (0 lub 1) dla każdego punktu danych

**D)** Dwie liczby całkowite — identyfikatory centroidów

**Odpowiedź: C** — `KMeans.fit()` to uczenie nienadzorowane — nie wymaga etykiet `y`. Po dopasowaniu `kmeans.labels_` zawiera numer klastra (0, 1, ..., k-1) przypisanego do każdej próbki. W tym przypadku 6 punktów zostanie przypisanych do jednego z 2 klastrów. Punkty bliskie [1,2] trafią do jednego klastra, punkty bliskie [8,8] do drugiego.

---

### Pytanie 2 (powtórka W13 — Plotly/Polars)

Który z poniższych fragmentów kodu tworzy **interaktywny** wykres słupkowy (można najechać myszką na słupek i zobaczyć wartość)?

**A)**
```python
import matplotlib.pyplot as plt
plt.bar(['A', 'B', 'C'], [10, 25, 15])
plt.show()
```

**B)**
```python
import plotly.express as px
fig = px.bar(x=['A', 'B', 'C'], y=[10, 25, 15])
fig.show()
```

**C)**
```python
import seaborn as sns
sns.barplot(x=['A', 'B', 'C'], y=[10, 25, 15])
```

**D)**
```python
import pandas as pd
pd.Series([10, 25, 15]).plot(kind='bar')
```

**Odpowiedź: B** — Plotly Express (`plotly.express`) tworzy wykresy HTML z pełną interaktywnością: hover tooltips, zoom, pan, download jako PNG. Matplotlib (A, D) i Seaborn (C) tworzą statyczne obrazy rastrowe bez wbudowanej interaktywności. To kluczowa różnica — Plotly nadaje się do dashboardów i raportów webowych, Matplotlib do statycznych plików PDF/druku.

---

### Pytanie 3 (nowy — tokeny i temperatura)

Tworzysz system do automatycznego generowania kodu SQL z opisów w języku naturalnym. Który parametr temperatury jest **najbardziej odpowiedni**?

**A)** `temperature=1.5` — wysoka kreatywność zapewni różnorodne zapytania SQL

**B)** `temperature=0.9` — model "myśli swobodniej" i pisze lepszy kod

**C)** `temperature=0.1` — niskie wartości dają deterministyczne, powtarzalne wyniki

**D)** Temperatura nie ma znaczenia dla jakości generowanego kodu

**Odpowiedź: C** — Przy generowaniu kodu zawsze używamy niskiej temperatury (0.0–0.2). Kod SQL musi być poprawny składniowo i logicznie — "kreatywność" jest tutaj szkodliwa. Niska temperatura oznacza że model wybiera statystycznie najbardziej prawdopodobny (czyli "najbardziej standardowy") token w każdym kroku, co daje przewidywalne, spójne wyniki. Wysoka temperatura (A, B) powoduje losowość — np. raz model może napisać `WHERE status = 'active'`, innym razem losowo `WHERE status = 'enabled'` — nawet jeśli oba mogą być sensowne, nieprzewidywalność jest problemem w systemach produkcyjnych.

---

### Pytanie 4 (nowy — API AI struktura)

Przeglądasz kod kolegi, który wywołuje OpenAI API. Znalazłeś poniższy fragment. Co robi parametr `system` w `messages`?

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Odpowiadaj tylko po polsku. Jesteś analitykiem danych."},
        {"role": "user", "content": "What is a p-value?"}
    ],
    temperature=0.2
)
```

**A)** Definiuje model który zostanie użyty (jak drugi parametr `model`)

**B)** Ustawia język interfejsu OpenAI — nie wpływa na treść odpowiedzi

**C)** Instruuje model o jego roli i zasadach zachowania — model będzie je respektować przez całą rozmowę

**D)** Szyfruje komunikację między klientem a API

**Odpowiedź: C** — `system` message to "persona" i "instrukcje" dla modelu. Wszystko co tu napiszemy, model będzie respektował przez cały czas trwania konwersacji. W tym przykładzie: mimo że pytanie jest po angielsku (`user`), model odpowie po polsku — bo tak nakazuje `system`. Można też tutaj ograniczyć model np. "odpowiadaj tylko kodem Python bez wyjaśnień" albo "nigdy nie używaj zewnętrznych bibliotek". To główny mechanizm kontroli zachowania modelu w aplikacjach.

---

### Pytanie 5 (nowy — ograniczenia LLM)

Koleżanka pyta Cię o opinie: chce wysłać do ChatGPT plik CSV z danymi klientów firmy (imię, email, historia zakupów) żeby AI wygenerowało spersonalizowane rekomendacje produktowe. Jakie jest **główne ryzyko** tej operacji?

**A)** ChatGPT nie radzi sobie z dużymi plikami CSV — to rozwiązanie technicznie nie zadziała

**B)** Dane osobowe klientów (imię, email) wysłane do publicznego API mogą naruszać RODO i wewnętrzną politykę firmy dotyczącą danych osobowych

**C)** Modele AI nie potrafią analizować danych tabelarycznych — należy użyć specjalistycznego oprogramowania

**D)** Koszt API będzie zbyt wysoki dla pliku CSV

**Odpowiedź: B** — To kluczowa kwestia etyczna i prawna. Dane osobowe (imię, email) wysłane do zewnętrznego API mogą być: logowane przez dostawcę, użyte do trenowania modelu, przechowywane na serwerach poza UE. RODO (GDPR) wymaga podstawy prawnej do przetwarzania danych osobowych przez podmiot trzeci — zwykłe "wysłanie do chatbota" jej nie zapewnia. W firmie wymaga to zgody Działu Prawnego i DPO (Data Protection Officer). Dobra praktyka: anonimizuj dane przed wysłaniem (zastąp email hashem, imię numerem klienta) albo używaj lokalnie hostowanego modelu (np. Ollama).

---

## Klucz odpowiedzi (dla prowadzącego)

| Pytanie | Odpowiedź | Temat |
|---------|-----------|-------|
| 1 | C | W13 — K-Means, labels\_ |
| 2 | B | W13 — Plotly interaktywność |
| 3 | C | W14 — temperatura LLM, generowanie kodu |
| 4 | C | W14 — system message, rola modelu |
| 5 | B | W14 — RODO, prywatność danych, etyka AI |
