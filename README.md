## Information om vibrationshandtagen

Handtagen har 3 hastigheter vardera; hastighet 1, hastighet 2, och hastighet 1 + 2. Dessa hastigheter bestäms av hrådvara. Enheten går att öppna och vikter kan bytas ut. Det ska även vara möjligt att öppna handtagen för att änndra rotationshastigheterna 1 och 2. Det är emellertid inte att rekommendera (såtillvida man inte vet vad man gör).

Valet avc handtag och hastighet (1, 2, eller 1 + 2) styrs med hjälp av programvara och, i princip, beror det på vilka stift i parallellporten man skickar ström genom.

Parallelporten har 25 stift (mer info: http://en.wikipedia.org/wiki/Parallel_port). Vissa stift kan använndas för input och andra för output. 

Stift 2 till 9 anväds för output. Vibrationsenheten är byggd för att upptäcka ström i pin 2, 3, 4, och 5. Till exempel, Skickar man ström till pin 2 så vibrerar det ena handtaget (med svart tejp) med hastighet 1.
Nedan följer en tabell för stift och vilket handtag samt hastighet som aktiveras genom de olika stiften;

|**Stift:**         |**Handtag:**     |**Hastighet:**    |**Värde:**        |
|-------------------|-----------------|------------------|------------------|
| 2                 | Svart           | 1                | 1                |
| 3                 | Svart           | 2                | 2                |
| 2 och 3           | Svart           | 1+2              | 3                |
| 4                 | Gult            | 1                | 4                |
| 5                 | Gult            | 2                | 8                |
| 4 och 5           | Gult            | 1+2              | 12               |
| 2 och 4           | Båda            | 1                | 5                |
| 3 och 5           | Båda            | 2                | 10               |
| 2, 3, 4, och 5    | Båda            | 1+2              | 15               |

Notera, med "Svart" och "Gult" åsyftas den tejp som finns tejpad runt handtagen.

## Att skicka signaler till handtagen

### PsychoPy
Använder vi oss av PsychoPy (http://www.psychopy.org; Peirce, 2007) fungerar det på alla datorer i labbet. För att kommunicera med parallellporten, via PsychoPy & Python, använder man sig av modulen Parallel (http://www.psychopy.org/api/parallel.html)

Följande portar gäller i labbet;

 - Input: 0xPORT
 - Output: 0x3FF8

Föratt aktivera olika stift i parallelporten använder man sig av *parallel.setData*.  Se [examplecode.py](https://github.com/marsja/vibration-device/blob/master/code/examplecode.py) för exempelkod för PsychoPy. För att handtaget ska sluta vibrera skickar man 0 (dvs., *parallel.setData(0)*). 

### Expyriment
Använder vi oss av Expyriment (http://www.expyriment.org; Krause & Lindemann, 2013) fungerar det också på alla datorer i labbet. För att kommunicera med parallellporten, via Expyriment, via Expyriment & Python använnder man sig av klasserna *ParallelPort* (http://docs.expyriment.org/old/0.6.3/expyriment.io.ParallelPort.html) och *StreamingButtonBox* (http://docs.expyriment.org/old/0.7.0/expyriment.io.StreamingButtonBox.html). 

### Referenser

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*. http://doi.org/10.3758/s13428-013-0390-6

Peirce, J. W. (2007). PsychoPy-Psychophysics software in Python. *Journal of Neuroscience Methods, 162*(1–2), 8–13. http://doi.org/10.1016/j.jneumeth.2006.11.017
