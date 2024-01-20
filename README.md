# Opis
To repozytorium zawiera pliki potrzebne do zrealizowania urządzenia, które za pomocą lasera będzie komunikowało się z inteligentnym asystentem głosowym.
Projekt jest podzielony na dwie części: 

- **BASIC**
Uproszczona wersja projektu potrafiąca jedynie przesłać za pomocą lasera jeden plik audio. Przygotowane są cztery polecenia, z których należy wybrać jedno, które będzie nadawane jednorazowo po włączeniu Arduino.

- **PRO MEGA SUPER**
Ulepszona wersja części BASIC, rozszerzona o dodatkową pamięć oraz przyciski do wyboru odpowiedniej komendy.

# Schemat urządzenia

![[1.png]]

![[2.png]]

# Instalacja na Arduino
1. Sklonuj repozytorium
```
git clone https://github.com/wojtekbakun/Laser_FIZ2
```
2. Dodaj bibliotekę .zip do Arduino znajdującą się w Laser_FIZ2/libraries
3. Otwórz plik laser_fiz2.ino
# Dodatkowe informacje
## Więcej informacji
- [Simple Arduino audio samples](https://highlowtech.org/?p=1963)
## Wersja PRO MEGA SUPER
Jeszcze nie powstała, jak trzeba będzie to się zrobi.
## Oryginalny plik tekstowy
W katalogu z plikami txt znajduje się `original.txt`, czyli ciąg znaków reprezentujący dźwięk z przykładu. Można też go wybrać poprzez **File>Examples>PCM>playback** (to tak żeby się upewnić czy działa)
## Tworzenie własnych poleceń
- Za pomocą FFmpeg skonwertowałem plik MP3 na PCM (Pulse Code Modulation - zamiana sygnału analogowego na cyfrowy)
```
ffmpeg -i input.mp3 -f s16le -acodec pcm_s16le output.pcm
```

- Następnie skonwertowałem plik PCM na ciąg znaków dzięki skryptowi w Python wpisując w nim odpowiednie nazwy plików
```
python pcm_to_txt.py
```
