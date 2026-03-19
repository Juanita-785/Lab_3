# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:32:37 2026

@author: manue
"""
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, find_peaks

#------------------------------------------------------------------------------
#PARTE A
# Diccionario
audios = {
    "Mujer 1": "Cami.wav",
    "Mujer 2": "Juanita.wav",
    "Mujer 3": "Shara.wav",
    "Hombre 1": "Duvan.wav",
    "Hombre 2": "Serna.wav",
    "Hombre 3": "Profe 2.wav"
}
#Recorte de ruido
recortes={
    "Mujer 1": (1, 4),
    "Mujer 2": (1, 3.5),
    "Mujer 3": (1, 3.5),
    "Hombre 1": (2, 4.5),
    "Hombre 2": (1.5, 3.5),
    "Hombre 3": (2, 4)    
}

def recortar_senal(sonido, fs, nombre, recortes):
    if nombre in recortes:
        inicio, fin = recortes[nombre]
        return sonido[int(inicio*fs):int(fin*fs)]
    return sonido

# Ciclo para generar una ventana independiente por cada audio
for nombre, ruta in audios.items():
    
    muestreo, sonido = waves.read(ruta)
    
    if len(sonido.shape) > 1:
        sonido = sonido[:, 0]

    # Normalizar señal de 16 bits
    sonido = sonido.astype(np.float32) / 32768.0
    
    sonido = recortar_senal(sonido, muestreo, nombre, recortes)

    # Tiempo actualizado
    tiempo = np.arange(len(sonido)) / muestreo
    
    plt.figure(figsize=(10, 4)) 
    plt.plot(tiempo, sonido, linewidth=0.5)
    plt.title(f"{nombre}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud []")
    plt.grid(True)

plt.show()

# 2. Ciclo para procesar la FFT de cada señal
for nombre, ruta in audios.items():
    # Leer el archivo .wav
    fs, sonido = waves.read(ruta)
    
    # Si es estéreo, convertir a monofónico tomando el primer canal
    if len(sonido.shape) > 1:
        sonido = sonido[:, 0]
    # Normalizar señal
    sonido = sonido.astype(np.float32) / 32768.0
    
    sonido = recortar_senal(sonido, fs, nombre, recortes)
    
    # --- Cálculo de la Transformada de Fourier ---
    n = len(sonido)
    X_fft = np.fft.fft(sonido)
    
    # Calcular la magnitud y tomar solo la primera mitad (frecuencias positivas)
    # Se normaliza dividiendo por el número de muestras
    mag = np.abs(X_fft[:n // 2]) / n 
    
    # Crear el vector de frecuencias para el eje X (de 0 a fs/2)
    frecuencias = np.linspace(0, fs / 2, n // 2)

    plt.figure(figsize=(10, 4)) 
    plt.semilogx(frecuencias, mag, color='red')
    plt.title(f"Espectro de Magnitudes: {nombre}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud []")
    plt.grid(True)

plt.show()

print(f"{'Señal':<12} | {'F0 (Hz)':<10} | {'Brillo (Hz)':<12} | {'Energía (RMS)':<12}")
print("-" * 55)

for nombre, ruta in audios.items():
    try:
        # Cargar audio y normalizar
        fs, sonido = waves.read(ruta)
        if len(sonido.shape) > 1: sonido = sonido[:, 0]
        sonido = sonido.astype(np.float32) / 32768.0
        
        sonido = recortar_senal(sonido, fs, nombre, recortes)
        
        # Intensidad (Energía RMS)
        # La energía es la raíz cuadrada del promedio de los cuadrados de la amplitud
        intensidad_rms = np.sqrt(np.mean(sonido**2))

        # Transformada de Fourier para Frecuencia y Brillo
        n = len(sonido)
        X_fft = np.fft.fft(sonido)
        mag = np.abs(X_fft[:n // 2])
        freqs = np.linspace(0, fs / 2, n // 2)

        # Brillo (Centroide Espectral)
        brillo_centroid = np.sum(freqs * mag) / np.sum(mag)

        # Frecuencia Fundamental (F0) mediante Cepstrum
        # Proceso: FFT -> log de magnitud -> FFT inversa
        cepstrum = np.fft.ifft(np.log(np.abs(X_fft) + 1e-10)).real #Pequeña constante para evitar log(0)
        
        # Buscar el pico máximo en el rango de voz humana (aprox. 50Hz a 500Hz)
        idesde, ihasta = int(fs/500), int(fs/50)
        pico_quefrency = np.argmax(np.abs(cepstrum[idesde:ihasta])) + idesde
        f0 = fs / pico_quefrency

        print(f"{nombre:<12} | {f0:>8.2f} | {brillo_centroid:>12.2f} | {intensidad_rms:>12.4f}")

    except Exception as e:
        print(f"Error en {nombre}: {e}")
        

#------------------------------------------------------------------------------
#PARTE B

# 1. Configuración: { "Nombre": (ruta, [inicio_voz, fin_voz], [inicio_ruido, fin_ruido]) }
config_snr = {
    "Audio 1": ("Cami.wav", [1.5, 3.0], [0.5, 1.0]),
    "Audio 2": ("Juanita.wav", [1.3, 3.1], [0.5, 1.0]),
    "Audio 3": ("Shara.wav", [1.5, 3.3], [0.5, 1.2]),
    "Audio 4": ("Duvan.wav", [2.1, 4.2], [0.5, 2.0]),
    "Audio 5": ("Serna.wav", [1.7, 3.0], [0.5, 1.5]),
    "Audio 6": ("Profe 2.wav", [2.1, 4.0], [0.5, 2.0])
}
print("")
print(f"{'Señal':<12} | {'SNR (dB)':<10}")
print("-" * 30)

for nombre, (ruta, t_voz, t_ruido) in config_snr.items():
    try:
        # Cargar el archivo .wav
        fs, sonido = waves.read(ruta)
        if len(sonido.shape) > 1: sonido = sonido[:, 0] # Convertir a mono si es necesario
        
        # Normalización de la señal
        sonido = sonido / np.max(np.abs(sonido))

        # Voz
        idx_v_ini = int(t_voz[0] * fs)
        idx_v_fin = int(t_voz[1] * fs)

        # Ruido
        idx_r_ini = int(t_ruido[0] * fs)
        idx_r_fin = int(t_ruido[1] * fs)
        
        # Extraer los segmentos de la matriz de sonido
        seg_voz = sonido[idx_v_ini : idx_v_fin]
        seg_ruido = sonido[idx_r_ini : idx_r_fin]

        #Cálculo de Energía RMS
        rms_voz = np.sqrt(np.mean(seg_voz**2))
        rms_ruido = np.sqrt(np.mean(seg_ruido**2))
        
        # Relación Señal-Ruido en decibeles
        snr_db = 20 * np.log10(rms_voz / (rms_ruido + 1e-10))

        print(f"{nombre:<12} | {snr_db:>8.2f} dB")
    except Exception as e:
        print(f"Error en {nombre}: {e}")
print("")

#Definición del filtro pasa-banda Butterworth
def aplicar_filtro(datos, lowcut, highcut, fs, orden=2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(orden, [low, high], btype='band')
    return lfilter(b, a, datos)

#Configuración: { "Nombre": ("ruta.wav", inicio_seg, fin_seg) }
audios_config = {
    "Mujer 1": ("Cami.wav", 2.47, 2.5),
    "Mujer 2": ("Juanita.wav", 1.607, 1.64),
    "Mujer 3": ("Shara.wav", 1.585, 1.625),
    "Hombre 1": ("Duvan.wav", 2.67, 2.705),
    "Hombre 2": ("Serna.wav", 2.13, 2.19),
    "Hombre 3": ("Profe 2.wav", 3.58, 3.62)
}

print(f"{'Señal':<10} | {'Jitt Abs(ms)':<12} | {'Jitt Rel(%)':<12} | {'Shim Abs[]':<12} | {'Shim Rel(%)':<12}")
print("-" * 75)

#Ciclo de procesamiento y graficación
for i, (nombre, (ruta, t_inicio, t_fin)) in enumerate(audios_config.items()):
    try:
        # Cargar audio
        fs, sonido_completo = waves.read(ruta)
        if len(sonido_completo.shape) > 1: sonido_completo = sonido_completo[:, 0]
        
        #EXTRACCIÓN DEL SEGMENTO
        idesde = int(t_inicio * fs)
        ihasta = int(t_fin * fs)
        sonido = sonido_completo[idesde:ihasta]
        
        # Normalización del segmento
        sonido = sonido / np.max(np.abs(sonido))

        #FILTRADO DIFERENTE
        if i < 3:
            low, high = 300.0, 3000.0
            color_p = 'blue'
        else:
            low, high = 80.0, 500.0
            color_p = 'green'
        
        sonido_f = aplicar_filtro(sonido, low, high, fs)
        #FFT DE LA SEÑAL FILTRADA
        n_f = len(sonido_f)
        X_fft_f = np.fft.fft(sonido_f)

        # Magnitud normalizada (solo mitad positiva)
        mag_f = np.abs(X_fft_f[:n_f // 2]) / n_f
        freqs_f = np.linspace(0, fs / 2, n_f // 2)

        # Gráfica
        plt.figure(figsize=(10, 4))
        plt.semilogx(freqs_f, mag_f, color='purple')
        plt.title(f"FFT Señal Filtrada: {nombre}")
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Magnitud []")
        plt.grid(True)
        
        #CÁLCULO DE JITTER Y SHIMMER
        dist_min = fs / 300 
        indices_picos, _ = find_peaks(sonido_f, distance=dist_min, height=0.4, prominence=0.2)
        
        if len(indices_picos) > 2:
            # Tiempos entre picos (Periodos fundamentales)
            Ti = np.diff(indices_picos) / fs
            # Amplitudes de los picos seleccionados
            Ai = sonido_f[indices_picos]
            
            #Jitter Relativo
            # Suma de las diferencias absolutas de periodos consecutivos
            j_abs_sum = np.sum(np.abs(np.diff(Ti)))
            j_rel = (j_abs_sum / (len(Ti) - 1)) / np.mean(Ti) * 100

            #Shimmer Relativo
            # Suma de las diferencias absolutas de amplitudes consecutivas
            s_abs_sum = np.sum(np.abs(np.diff(Ai)))
            s_rel = (s_abs_sum / (len(Ai) - 1)) / np.mean(Ai) * 100
            
            # Jitter Absoluto para la tabla (en ms)
            j_abs_ms = (np.mean(np.abs(np.diff(Ti)))) * 1000
            # Shimmer Absoluto
            s_abs = np.mean(np.abs(np.diff(Ai)))

            print(f"{nombre:<10} | {j_abs_ms:>11.4f} | {j_rel:>11.4f}% | {s_abs:>11.4f} | {s_rel:>11.4f}%")

            plt.figure(figsize=(10, 4))
            t_segmento = np.linspace(t_inicio, t_fin, len(sonido_f))
            
            plt.plot(t_segmento, sonido_f, color=color_p, linewidth=0.7, label='Señal Filtrada')
            plt.plot(indices_picos/fs + t_inicio, Ai, "ro", markersize=3, label='Picos detectados') # Mostrar picos Ai
            
            plt.title(f"Análisis Segmentado: {nombre} ({t_inicio}s - {t_fin}s)")
            plt.xlabel("Tiempo (s)")
            plt.ylabel("Amplitud []")
            plt.legend(loc='upper right')
            plt.grid(True)
            
        else:
            print(f"{nombre:<10} | Segmento sin picos suficientes")

    except Exception as e:
        print(f"Error en {nombre}: {e}")

plt.show()