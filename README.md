Kiedy podnosić wersję modelu?
Należy to zrobić, gdy pojawia się zmiana hiperparametrów, wewnętrznych ustawień algorytmu, poprawa jakości lub zmiana zakresu danych.

Lista różnic i wyzwań:
- w środowisku deweloperskim zbiory informacji są statyczne i wyczyszczone, natomiast na produkcji dane napływają w czasie rzeczywistym i często różnią się od tych użytych do treningu,
- lokalnie model jest oceniany tylko raz po wytrenowaniu, a wdrożenie produkcyjne wymaga ciągłego monitorowania, aby w porę wyłapać spadek jego skuteczności,
- produkcja wymaga ścisłej konteneryzacji, aby kod działał identycznie na każdym serwerze, a tworząc model używam prostego środowiska wirtualnego, 
- lokalnie odpalane są skrypty ręcznie, a środowisko produkcyjne opiera się na automatyzacji,
- w środowisku deweloperskim zasoby często są ograniczone i z góry określone, a serwery produkcyjne muszą być elastyczne i gotowe na  bardzo szybkie obsłużenie wielu zapytań.