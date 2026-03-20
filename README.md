# Laboratorio No.3 "Análisis espectral de la voz"
## Shara Cetina y Juanita Gómez

## Descripción
Este proyecto contiene el código y la información para comprender el espectro de la voz, además de analizar señales de voz con ayuda de técnicas de análisis espectral como la transformada de Fourier y caracterizar la señal con parámetros como frecuencia fundamental, brillo, intensidad, jitter y shimmer.

## Propósito
<p align="justify">
El propósito de este laboratorio es que el estudiante aplique técnicas de análisis espectral y comprenda la importancia del cálculo de atributos en el dominio de la frecuencia dentro del procesamiento de señales, específicamente en señales de voz. Se busca que el estudiante entienda el análisis espectral como una herramienta que permite observar la distribución de la energía al descomponer una señal en sus componentes de frecuencia y amplitud. Asimismo, mediante el cálculo de parámetros de inestabilidad en señales periódicas, como el Jitter y Shimmer, junto con el análisis espectral de señales biológicas, se pretende que el estudiante evalúe el impacto de estos procedimientos en la detección de posibles patologías a partir de señales de voz y reconozca su relevancia en aplicaciones propias del ámbito de la ingeniería biomédica. Además, se busca que el estudiante relacione estos parámetros con características fisiológicas y de calidad de la señal, permitiendo la interpretación de diferencias entre distintos tipos de voz.

## Metodología
<p align="justify">
Para llevar a cabo el análisis de la voz se tomaron 6 muestras a una misma frecuencia de muestreo (44.1 KHZ), de las cuales la mitad fueron hombres y la otra mitad mujeres, todas estas fueron exportadas en formato .wav a la multiplataforma Spyder, en donde se llevaron a cabo distintos procedimientos con el propósito de profundizar en su estudio. Primeramente se calculó y graficó la transformada de Fourier la cual nos permite descomponer la señal de voz en sus componentes de frecuencia, después se caracterizó la señal por medio de la frecuencia fundamental, brillo e intensidad.

<p align="justify">
Luego se aplicó un filtro pasa-banda con distintos rangos de frecuencia dependiendo del género, en los hombres se utilizó 80-400 Hz y en las mujeres 150-500 Hz, en donde fue necesario adquirir el SNR para obtener la segunda constante y calcular el órden del filtro. Por consiguiente se realizó la medición del Jitter y Shimmer absoluto y relativo de las señales por medio las siguientes fórmulas:

### Jitter absoluto

$$
Jitter_{abs} = \frac{1}{N - 1} \sum_{i=1}^{N-1} |T_i - T_{i+1}|
$$

### Jitter relativo (%)

$$
Jitter_{rel} = 
\frac{
\frac{1}{N-1} \sum_{i=1}^{N-1} |T_i - T_{i+1}|
}{
\frac{1}{N} \sum_{i=1}^{N} T_i
}
\times 100
$$
### Shimmer absoluto

$$
Shimmer_{abs} = \frac{1}{N - 1} \sum_{i=1}^{N-1} |A_i - A_{i+1}|
$$

### Shimmer relativo (%)

$$
Shimmer_{rel} = 
\frac{
\frac{1}{N-1} \sum_{i=1}^{N-1} |A_i - A_{i+1}|
}{
\frac{1}{N} \sum_{i=1}^{N} A_i
}
\times 100
$$
<p align="justify">
Finalmente en base a todos los resultados obtenidos se llevó a cabo el respectivo análisis con el fin de relacionar los datos teóricos con los prácticos.
  
## Diagrama de flujo 

### Parte A
<img width="1024" height="768" alt="1" src="https://github.com/user-attachments/assets/3714d795-4e5f-49ea-b165-22283c9aaa0f" />
<img width="1024" height="768" alt="2" src="https://github.com/user-attachments/assets/ff12c81e-5eed-4623-9f7c-04b961845a23" />

### Parte B
<img width="1024" height="768" alt="3" src="https://github.com/user-attachments/assets/07ebdafb-9d42-4bb9-88c8-54db115caf42" />
<img width="1024" height="369" alt="44" src="https://github.com/user-attachments/assets/ddaac546-3567-4bae-bdd0-d11454d94b5a" />


### Parte C

**¿Qué diferencias se observan en la frecuencia fundamental?** 

<p align="justify">
Las diferencia que se puede observar en la frecuencia fundamental se encuentra relacionada con el género, ya que los resultados obtenidos en mujeres dan en un rango de 208 - 336 Hz, en cambio en los hombres da entre 85 - 255 Hz, dejando en evidencia que el género femenino cuenta con una frecuencia fundamental mucho más alta en comparación con los hombres. 


**¿Qué otras diferencias notan en términos de brillo, media o intensidad?**
<p align="justify">
En los datos obtenidos se observa que las voces femeninas presentan, en general, valores más altos de brillo y frecuencia fundamental. De acuerdo con la literatura, esto se debe a que las cuerdas vocales femeninas suelen ser más cortas y delgadas, lo que produce vibraciones más rápidas, una mayor frecuencia fundamental y una mayor presencia de componentes de alta frecuencia, percibidas como mayor brillo. Por otro lado, en las voces masculinas, las cuerdas vocales tienden a ser más larga y gruesas, lo que genera vibraciones más lentas, una frecuencia fundamental más baja y un sonido perceptivamente más grave en comparación con las voces femeninas. 

**Comportamiento de la voz en hombres y mujeres a partir de los análisis realizados.** 
<p align="justify">
En base a los resultados obtenidos se puede observa como las mujeres manejan la frecuencia fundamental y el brillo de la voz mucho más alto en comparación con los hombres, sin embargo, la intensidad de energía de los hombres si es superior. Todo esto se puede atribuir a diversos factores, especialmente a las características anatómicas que diferencian ambos sexos. En el caso de los hombres debido a la testosterona su laringe crece y las cuerdas vocales se engrosan alcanzando una longitud entre 17 y 25 mm, generando vibraciones más lentas, por ende, un tono más grave; en cambio los estrógenos de las mujeres no alteran significativamente la estructura laríngea, manteniendo una longitud aproximadamente de 12 a 17 mm, produciendo vibraciones más rápidas y agudas. Por eso mismo la intensidad de energía de los hombres da alta (su amplitud es mayor), pero su frecuencia fundamental que hace referencia a la frecuencia más baja que un sistema vibratorio u ondulatorio puede oscilar es inferior al igual que el brillo, siendo este una característica que permite ver la presencia de frecuencias altas (agudos).

**Importancia clínica del jitter y shimmer en el análisis de la voz.**
<p align="justify">
El jitter y el shimmer son pilares fundamentales del análisis acústico, los cuales permiten evaluar la estabilidad de la vibración de las cuerdas vocales de manera objetiva. El jitter mide la variación temporal del "ritmo" de la frecuencia fundamental (FO), y el shimmer cuantifica la variación de la ampllitud o "intensidad" de la onda sonora ciclo a ciclo. Su importancia clínica radica en la detección de patologías debido a valores elevados, ya que tanto el jitter como el shimmer manejan un porcentaje por debajo del 5% si la persona se encuentra sana, en el caso del jitter debe ser menor al 1% y en el shimmer al 5%. Ambos funcionan como biomarcadores de inestabilidad vocal, por eso mismo si se llegase a obtener valores elevados por medio de su estudio es posible identificar de forma óptima diversas patologías atribuidas principalmente al mal funcionamiento de las cuerdas vocales, enfermedades como nódulos, pólipos, quistes, edemas, parálisis o inflamaciones, sin embargo, también permiten identificar falencias neurológicas, puesto que la mayoría de trastornos afectan el control neuromotor de la voz, tales como el Parkinson, la esclerosis lateral amiotrófica (ELA), esclerosis múltiple o disfonía espasmódica. A su vez nos permiten analizar la eficacia de las intervenciones médicas, quirúrgica o logopédicas que se le realicen a los pacientes, esperando obtener como resultados valores bajos si el procedimiento funcionó.

  
## Resultados
### Señales de voz de las mujeres
<p align="center">
  <img src="https://github.com/user-attachments/assets/0017eaf1-fe7f-43d5-a2b8-d343241e8ef5" width="300"/>
  <img src="https://github.com/user-attachments/assets/dbf3e8b8-a23b-4952-b4b8-54d938e330c5" width="300"/>
  <img src="https://github.com/user-attachments/assets/e90d05ff-4bd8-4264-a98d-a142a196b892" width="300"/>
</p>

### Señales de voz de los hombres
<p align="center">
  <img src="https://github.com/user-attachments/assets/3198dfe9-711b-4a83-a416-e6ec3e1bd27f" width="300"/>
  <img src="https://github.com/user-attachments/assets/84ff3119-42e4-4150-8aea-12b7f719af9e" width="300"/>
  <img src="https://github.com/user-attachments/assets/d350be9a-aeee-4e1e-8aca-c18f78888d98" width="300"/>
</p>

### Transformadas de Fourier 
#### Mujeres
<p align="center">
  <img src="https://github.com/user-attachments/assets/f263a0f0-6c0c-40fc-9546-b142c56cf975" width="300"/>
  <img src="https://github.com/user-attachments/assets/c795572b-c129-47ef-b83e-6c56c182916b" width="300"/>
  <img src="https://github.com/user-attachments/assets/3f2c7cb7-87c9-40ff-a35e-fb1918c4670a" width="300"/>
</p>

#### Hombres
<p align="center">
  <img src="https://github.com/user-attachments/assets/b8badd49-9050-459c-8cef-5e3fa6afb1f0" width="300"/>
  <img src="https://github.com/user-attachments/assets/da03834c-5bd6-4cf5-820f-87eeef92c13c" width="300"/>
  <img src="https://github.com/user-attachments/assets/0825aec0-b0b9-459b-bb21-43b32d82b26d" width="300"/>
</p>

### Señales filtradas
#### Mujeres
<p align="center">
  <img src="https://github.com/user-attachments/assets/930c7e35-bb29-43bb-9df4-4927ce7a7253" width="300"/>
  <img src="https://github.com/user-attachments/assets/04ea7a35-2615-463b-84bd-69da778f7e7d" width="300"/>
  <img src="https://github.com/user-attachments/assets/df77c78d-88e3-4fd1-b5cf-784fabb6e368" width="300"/>
</p>

#### Hombres
<p align="center">
  <img src="https://github.com/user-attachments/assets/de2da697-2767-44f3-a759-8acf52bcdfcc" width="300"/>
  <img src="https://github.com/user-attachments/assets/782f6129-3d57-4563-b250-2f263f3021a8" width="300"/>
  <img src="https://github.com/user-attachments/assets/c26b7e90-f115-4582-bbf4-0d237505f497"  width="300"/>
</p>

### Transformadas de Fourier filtradas
#### Mujeres
<p align="center">
  <img src="https://github.com/user-attachments/assets/f268910e-f636-4ef9-af43-a866296911cd" width="300"/>
  <img src="https://github.com/user-attachments/assets/b13c7194-b3d8-4776-826f-1db1243507e1" width="300"/>
  <img src="https://github.com/user-attachments/assets/e2774c98-306f-41c7-9ab4-4a352e640852"  width="300"/>
</p>

#### Hombres
<p align="center">
  <img src="https://github.com/user-attachments/assets/8fc57cf4-2ca1-4446-b19b-2d4cd7397217" width="300"/>
  <img src="https://github.com/user-attachments/assets/dce34607-9ae0-4ca5-b30c-eb1e5f43e71d" width="300"/>
  <img src="https://github.com/user-attachments/assets/f841da02-c105-4bac-a051-a6d2ba0b2000""  width="300"/>
</p>

## Análisis Estadístico //Shara
### Parámetros calculados
<div align="center">

#### Características de la señal

| Señal   | F0 (Hz) | Brillo (Hz) | Energía (RMS) |
|--------|--------:|------------:|--------------:|
| Mujer 1 | 336.64 | 2234.38 | 0.0640 |
| Mujer 2 | 222.73 | 2283.06 | 0.0639 |
| Mujer 3 | 208.02 | 3032.19 | 0.0656 |
| Hombre 1 | 113.37 | 1635.25 | 0.0831 |
| Hombre 2 | 149.49 | 2731.53 | 0.0885 |
| Hombre 3 | 279.11 | 1632.99 | 0.0650 |

</div>
<p align="justify">
Al calcular la frecuencia fundamental, se obtienen valores para las voces femeninas entre 208 Hz a 336 Hz, mientras que en los hombres oscila entre 113 Hz y 279 Hz. Al comparar estos resultados con la literatura, se observa que la frecuencia fundamental típica de la voz femenina se encuentra entre 165 Hz y 255 Hz, mientras que en la voz masculina oscila entre los 85 Hz y 155 Hz. En general, existe concordancia entre los valores experimentales y los teóricos. Sin embargo, se destacan algunos casos atípicos, la mujer 1 y el hombre 3, quienes presentan frecuencias fundamentales más elevadas de lo esperado. 
  
<p align="justify">
En cuanto al brillo, las voces femeninas presentan un rango de 2234 Hz a 3032 Hz, mientras que las voces masculinas se encuentran entre 1632 Hz a 2751 Hz, al comparar con los rangos teóricos (2500 Hz a 3500 Hz en voces femeninas y 1500 Hz a 2500 Hz en voces masculinas), se observa una buena concordancia, con excepción del hombre 2 que presenta un brillo más alto del esperado.
  
<p align="justify">
Por otro lado, el RMS calculado para las seis personas se encuentra en un rango de 0.06 a 0.08, lo que coincide con los valores teóricos de 0.03 a 0.08 en una conversación normal. 
  
<p align="justify">
En términos generales, los datos experimentales coinciden con los valores teóricos, aunque se presentan algunas variaciones que pueden atribuirse al tono de voz de individual, la edad, el ruido ambiental, la distancia al micrófono y la calidad de la grabación. 

<div align="center">

#### Relación señal-ruido (SNR)

| Señal   | SNR (dB) |
|--------|---------:|
| Audio 1 | 13.91 |
| Audio 2 | 9.33 |
| Audio 3 | 16.44 |
| Audio 4 | 17.21 |
| Audio 5 | 13.58 |
| Audio 6 | 8.94 |

</div>
<p align="justify">
Para calcular la relación señal ruido (SNR), se recortó el primer fragmento de la grabación, correspondiente a un tramo donde la persona no habla y solo se percibe el ruido ambiental. Posteriormente, se realizó el cálculo del SNR, obteniendo los valores presentados en la tabla. A partir de estos datos, se obtuvo un SNR promedio de 13.24 dB.
  
<p align="justify">
Este valor permite determinar los parámetros necesarios para el diseño de un filtro pasa-banda, incluyendo las constantes y las frecuencias necesarias para establecer el orden del filtro. Además, se verifica el correcto cálculo del filtro al comparar la transformada de Fourier de la señal antes y después del filtro.

<div align="center">

#### Jitter y Shimmer

| Señal   | Jitt Abs (ms) | Jitt Rel (%) | Shim Abs | Shim Rel (%) |
|--------|--------------:|-------------:|---------:|-------------:|
| Mujer 1 | 0.1663 | 4.0870 | 0.0615 | 8.9792 |
| Mujer 2 | 0.1361 | 2.9777 | 0.0629 | 11.5473 |
| Mujer 3 | 0.1550 | 3.2740 | 0.0439 | 6.7933 |
| Hombre 1 | 0.2041 | 2.5641 | 0.0284 | 3.8049 |
| Hombre 2 | 0.0777 | 1.1608 | 0.0195 | 3.8633 |
| Hombre 3 | 0.0680 | 0.5935 | 0.0410 | 7.8568 |

</div>
<p align="justify">
Aunque los valore de Jitter y Shimmer no están establecidos de manera universal, existen algunos rangos de normalidad reportados en la literatura. El Jitter absoluto oscila entre 0.02 ms y 0.20 ms, datos que concuerdan con los valores obtenidos de manera experimental, aunque el hombre 1 presenta una ligera alteración. En el caso del Jitter relativo, se observa que el porcentaje de la mujer 1 es más elevado en comparación con los demás datos; además, al contrastarlo con la literatura, se encuentra dentro del rango de 0.2% a 1.5%.
Al analizar el Shimmer, se observa un rango de 3.8% a 11%, valores que, al compararse con la literatura, se alejan del rango establecido (3% a 7%).
La alteración de los resultados se puede explicar por una inestabilidad en la vibración de las cuerdas vocales, las condiciones de grabación, el tipo de voz, el tamaño de la muestra e incluso por características vocales específicas. Sin embargo, se puede observar que, en varios casos, especialmente en las mujeres, los datos se encuentran por encima del rango típico, lo que sugiere una mayor variabilidad vocal.


### Transformada de Fourier
<p align="justify">

## Análisis de Resultados: 
<p align="justify">
Durante el desarrollo de la práctica, se evidenciaron diferencias significativas en los parámetros espectrales de las señales de voz en relación con el sexo de los hablantes en cuanto a la frecuencia fundamental ($FO$), las mujeres presentaron un rango notablemente más alto (208.02 Hz a 336.64 Hz) en comparación con el rango obtenido para los hombres (113.37 Hz a 279.11 Hz) esta distinción técnica tiene una base fisiológica sólida. Durante la pubertad, la testosterona provoca que la laringe masculina crezca y las cuerdas vocales se alarguen y engrosen (alcanzando entre 17 y 25 mm), lo que genera vibraciones más lentas y tonos graves en contraste, las mujeres mantienen cuerdas más cortas y delgadas (12 a 17 mm), produciendo vibraciones más rápidas y agudas, asimismo, el brillo, que indica la presencia de armónicos de alta frecuencia, fue consistentemente superior en las muestras femeninas, reflejando el timbre característico de este género, por el contrario, la intensidad de energía (RMS) fue generalmente mayor en los hombres, alcanzando valores de hasta 0.0885, lo cual se asocia a una mayor amplitud de vibración en los pliegues vocales masculinos.
  
<p align="justify">
La eficacia del procesamiento digital de las señales fue validada mediante la comparación de las Transformadas de Fourier (FFT) antes y después del filtrado, las gráficas permitieron observar una disminución eficiente del ruido de fondo y de componentes ajenos al rango vocal humano, por lo tanto el uso de filtros pasa-banda ajustados específicamente para cada género (80–400 Hz para hombres y 150–500 Hz para mujeres) resultó adecuado para aislar la frecuencia fundamental y sus armónicos principales, garantizando así la precisión necesaria para el cálculo posterior de los parámetros de estabilidad vocal.


<p align="justify">
El análisis de la estabilidad vibratoria se realizó a través de las medidas de perturbación Jitter y Shimmer, las cuales funcionan como biomarcadores de la salud de las cuerdas vocales, según la literatura técnica, una voz sana presenta típicamente un Jitter relativo ≲ $1.04% y un Shimmer relativo ≲ 3.81%, al contrastar los resultados, se observó que la mayoría de los sujetos superaron estos umbrales, a excepción del Hombre 3, cuyo Jitter relativo fue de 0.59%, situándose dentro del rango de normalidad, no obstante, se identificaron dos casos con valores de Shimmer considerablemente altos: la Mujer 2 (11.54%) y el Hombre 3 (7.85%). Aunque niveles elevados de Shimmer suelen asociarse a patologías como nódulos o edemas, estos resultados deben interpretarse contextualmente, en el caso de la Mujer 2, la desviación puede atribuirse a factores demográficos específicos, mientras que para el Hombre 3, su edad superior influye directamente, ya que el envejecimiento natural reduce la elasticidad de los tejidos vocales y aumenta la inestabilidad de la amplitud sin representar necesariamente una enfermedad. Estos hallazgos subrayan la importancia de considerar factores individuales y ambientales antes de emitir un juicio clínico definitivo basado únicamente en parámetros acústicos.

## Conclusión 

<p align="justify">
Durante el desarrollo de esta práctica de laboratorio, se evidenciaron diferencias significativas en los parámetros espectrales según el sexo, donde las mujeres presentaron una frecuencia fundamental ($F0$) y un brillo más elevados (208.02 Hz a 336.64 Hz) debido a sus cuerdas vocales cortas y delgadas, mientras que los hombres mostraron una mayor intensidad de energía (RMS) y tonos más graves (113.37 Hz a 279.11 Hz) producto del alargamiento y engrosamiento laríngeo inducido por la testosterona. La eficacia del procesamiento digital fue validada mediante la Transformada de Fourier (FFT) y el uso de filtros pasa-banda, los cuales permitieron reducir el ruido y aislar con precisión los componentes armónicos necesarios para el análisis de estabilidad vocal a través de las medidas de perturbación, se identificaron valores de Shimmer superiores al umbral clínico del 3.81% en la Mujer 2 (11.54%) y el Hombre 3 (7.85%), lo que sugiere inestabilidades en la amplitud que, si bien son biomarcadores de patologías como el Parkinson o edemas, en estos casos específicos se asocian a la variabilidad demográfica y al envejecimiento natural de los tejidos vocales.
  
<p align="justify">
En conclusión, este laboratorio demuestra que el análisis acústico digital transforma la voz en un biomarcador objetivo y no invasivo, fundamental para la detección temprana de trastornos neurológicos y funcionales, resaltando la necesidad de integrar estos datos en una evaluación clínica multidimensional que considere factores individuales del paciente en modelos de inteligencia artificial y softwares especializados, prometiendo de esta manera un futuro donde el diagnóstico de salud vocal sea más accesible, económico y preciso para la sociedad global.


## Discusión

**¿Cómo es la frecuencia fundamental de la densidad espectral de potencia asociada a una señal de voz masculina con respecto a la que se obtiene a partir de una señal de voz femenina, mayor o menor? ¿Qué hay del valor RMS?** //Shara

**¿Qué limitaciones plantea el uso de características como shimmer y jitter para la detección de patologías como disartrias y afasias?** 

<p align="justify">
El uso de parámetros como el jitter y el shimmer para detectar patologías como las disartrias y las afasias presentan limitaciones críticas debido a que estas medidas están diseñadas para evaluar únicamente la microestabilidad de la vibración de las cuerdas vocales y no los procesos motores o cognitivos superiores involucrados en el habla y el lenguaje. Una limitación fundamental es que estos indicadores requieren típicamente de la fonación sostenida de una vocal y pierden fiabilidad en el habla conectada, donde los cambios de tono, las pausas y las consonantes sordas impiden un cálculo preciso. En el caso de las disartrias, que afectan múltiples subsistemas como la respiración, la articulación y la resonancia, el jitter y el shimmer no pueden capturar fallos articulatorios o la hipernasalidad, e incluso pueden verse confundidos por la alta aperiodicidad de la señal en casos severos que impide la identificación correcta de los ciclos glotales. Por otro lado, las afasias son trastornos del lenguaje de origen cognitivo que afectan la producción de unidades con significado y la gramática, aspectos que no guardan relación directa con la estabilidad vibratoria glotal que estas métricas cuantifican. Finalmente, la alta sensibilidad de estas medidas ante factores externos como la intensidad de la fonación, la calidad del equipo de grabación y el ruido ambiental puede generar artefactos técnicos que distorsionan el diagnóstico clínico.
