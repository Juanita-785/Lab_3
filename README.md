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
En los datos obtenidos se observa que las voces femeninas presentan, en general, valores más altos de brillo y frecuencia fundamenta. De acuerdo con la literatura, esto se debe a que las cuerdas vocales femeninas suelen ser más cortas y delgadas, lo que produce vibraciones más rápidas, una mayor frecuencia fundamental y una mayor presencia de componentes de alta frecuencia, percibidas como mayor brillo. Por otro lado, en las voces masculinas, las cuerdas vocales tienden a ser más larga y gruesas, lo que genera vibraciones más lentas, una frecuencia fundamental más baja y un sonido perceptivamente más grave en comparación con las voces femeninas. 

**Comportamiento de la voz en hombres y mujeres a partir de los análisis realizados.** // Juanita

**Importancia clínica del jitter y shimmer en el análisis de la voz.** //Juanita

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

### Transformada de Fourier
## Análisis de Resultados: //Juanita
Evalúe si existen diferencias estadísticamente significativas entre los valores de los parámetros espectrales pertenecientes a señales de voz masculinas y femeninas.

Ofrezca posibles explicaciones desde la fisiología humana que justifiquen diferencias o semejanzas entre los parámetros espectrales de cada género.

## Conclusión //Juanita
Utilidad y posibles escenarios de aplicación de las herramientas y características espectrales empleadas.

## Discusión

**¿Cómo es la frecuencia fundamental de la densidad espectral de potencia asociada a una señal de voz masculina con respecto a la que se obtiene a partir de una señal de voz femenina, mayor o menor? ¿Qué hay del valor RMS?** //Shara

**¿Qué limitaciones plantea el uso de características como shimmer y jitter para la detección de patologías como disartrias y afasias?** //Juanita
