#!/usr/bin/env python3
from datetime import datetime

from textwrap import wrap
from datetime import datetime

# Vstupní text
input_text = """
1. 10.	Igor
2. 10.	Oliver
2. 10.	Olivia
2. 10.	Olívie
3. 10.	Bohumil
4. 10.	František
5. 10.	Elsa
5. 10.	Eliška
6. 10.	Hanuš
7. 10.	Justýna
7. 10.	Justina
7. 10.	Justin
8. 10.	Věra
8. 10.	Viera
9. 10.	Štefan
9. 10.	Sára
10. 10.	Marina
10. 10.	Marína
11. 10.	Andrej
12. 10.	Marcel
13. 10.	Renata
13. 10.	Renáta
14. 10.	Agáta
15. 10.	Tereza
16. 10.	Havel
17. 10.	Hedvika
18. 10.	Lukáš
19. 10.	Michala
19. 10.	Michaela
20. 10.	Vendelín
21. 10.	Brigita
21. 10.	Bridget
22. 10.	Sabina
23. 10.	Teodor
23. 10.	Theodor
24. 10.	Nina
25. 10.	Beáta
25. 10.	Beata
26. 10.	Erik
26. 10.	Ervín
27. 10.	Šarlota
27. 10.	Zoja
27. 10.	Zoe
29. 10.	Sylva
29. 10.	Silva
29. 10.	Silvie
30. 10.	Tadeáš
31. 10.	Stefanie
31. 10.	Štepánka
1. 11.	Felix
3. 11.	Hubert
4. 11.	Karel
5. 11.	Miriam
6. 11.	Liběna
7. 11.	Saskie
8. 11.	Bohumír
9. 11.	Bohdan
10. 11.	Eugen
10. 11.	Evžen
11. 11.	Martin
12. 11.	Benedikt
13. 11.	Tibor
14. 11.	Sáva
15. 11.	Leopold
16. 11.	Otmar
16. 11.	Otomar
17. 11.	Mahulena
18. 11.	Romana
19. 11.	Alžběta
19. 11.	Elisabeth
20. 11.	Nikola
21. 11.	Albert
22. 11.	Cecílie
23. 11.	Kliment
23. 11.	Klement
24. 11.	Emilia
24. 11.	Emílie
25. 11.	Katarína
25. 11.	Katka
25. 11.	Kateřina
26. 11.	Artur
27. 11.	Xenie
28. 11.	Renée
28. 11.	René
29. 11.	Zina
30. 11.	Ondřej
1. 12.	Iva
2. 12.	Blanka
3. 12.	Svatoslav
3. 12.	Světoslav
4. 12.	Barbara
4. 12.	Barbora
4. 12.	Bára
5. 12.	Jitka
6. 12.	Mikoláš
6. 12.	Nikolas
6. 12.	Mikuláš
7. 12.	Benjamin
7. 12.	Ambrož
8. 12.	Květoslava
9. 12.	Vratislav
10. 12.	Julie
10. 12.	Juliana
10. 12.	Julia
11. 12.	Dana
12. 12.	Šimona
12. 12.	Simeona
12. 12.	Simona
13. 12.	Lucia
13. 12.	Lucie
13. 12.	Luciana
14. 12.	Lýdie
14. 12.	Lydia
14. 12.	Lydie
15. 12.	Radana
16. 12.	Albína
17. 12.	Daniel
17. 12.	Dan
18. 12.	Miloslav
19. 12.	Ester
20. 12.	Dagmara
20. 12.	Dáša
20. 12.	Dagmar
21. 12.	Natálie
22. 12.	Simon
22. 12.	Simeon
22. 12.	Šimon
23. 12.	Vlasta
24. 12.	Eva
24. 12.	Adam
26. 12.	Štepán
26. 12.	Štěpán
27. 12.	Žaneta
28. 12.	Bohumila
29. 12.	Judita
30. 12.	David
31. 12.	Silvester
31. 12.	Silvestr
31. 12.	Sylvestr
"""

# Zpracování seznamu
entries = []
for line in input_text.strip().splitlines():
    parts = line.strip().split('\t')
    if len(parts) >= 2:
        date_raw, name = parts[0].strip(), parts[1].strip()
        try:
            date_obj = datetime.strptime(date_raw, "%d. %m.")
            formatted_date = date_obj.strftime("%d.%m.")
            month = date_obj.month
            entries.append((month, f"{formatted_date} {name}"))
        except ValueError:
            continue

# Rozdělení podle měsíců
months = {10: [], 11: [], 12: []}
for month, entry in entries:
    if month in months:
        months[month].append(entry)

# Zarovnání do sloupců
max_len = max(len(months[10]), len(months[11]), len(months[12]))
output_lines = []
for i in range(max_len):
    col1 = months[10][i] if i < len(months[10]) else ""
    col2 = months[11][i] if i < len(months[11]) else ""
    col3 = months[12][i] if i < len(months[12]) else ""
    line = f"       {col1:<16}\t\t|\t{col2:<16}\t\t|\t{col3:<16}"
    output_lines.append(line)

formatted_output = "\n".join(output_lines)

# Uložení výstupu do souboru
with open("vystup.txt", "w", encoding="utf-8") as f:
    f.write(formatted_output)
