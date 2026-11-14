import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time

fs = 44100  
duration = 3.0  

def grabar_y_procesar_segmento(nombre_vocal):
    print(f"\n[ACCIÓN] Pronuncie y mantenga la vocal '{nombre_vocal}'...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float32')
    sd.wait()
    print(f"Grabación de '{nombre_vocal}' finalizada.")
    
    if len(audio.shape) > 1 and audio.shape[1] > 1:
        x_mono = np.mean(audio, axis=1)
    else:
        x_mono = audio.flatten()
        
    start_idx = int(1.0 * fs)
    end_idx = int(2.0 * fs)
    return x_mono[start_idx:end_idx]

# 1. Construcción de referencias
vocales = ['A', 'E', 'I', 'O', 'U']
referencias = {}

print("=== ETAPA 1: REFERENCIAS ===")
for v in vocales:
    print(f"\nPrepárese para la vocal '{v}'...")
    time.sleep(2)
    referencias[v] = grabar_y_procesar_segmento(v)

# 2. Captura de la vocal de prueba
print("\n=== ETAPA 2: PRUEBA DESCONOCIDA ===")
print("Prepárese. La grabación comenzará en 3 segundos...")
time.sleep(3)
x_T = grabar_y_procesar_segmento("DESCONOCIDA")

# 3. Procesamiento y Correlación Normalizada
similitudes = {}
correlaciones_norm = {}
E_T = np.sum(x_T**2)

plt.figure(figsize=(12, 8))

for i, v in enumerate(vocales):
    x_ref = referencias[v]
    E_ref = np.sum(x_ref**2)
    
    corr = np.correlate(x_T, x_ref, mode='full')
    
    if E_T > 0 and E_ref > 0:
        rho = corr / np.sqrt(E_T * E_ref)
        correlaciones_norm[v] = rho
        similitudes[v] = np.max(rho)
    else:
        correlaciones_norm[v] = corr
        similitudes[v] = 0.0

    # Subgráfica para cada correlación cruzada normalizada (Exigido por la guía)
    plt.subplot(3, 2, i+1)
    plt.plot(rho, color='tab:blue')
    plt.title(f"Correlación Normalizada: Prueba vs {v}")
    plt.xlabel("Desplazamiento k (muestras)")
    plt.ylabel("Amplitud / Similitud")
    plt.grid(True, linestyle='--', alpha=0.6)

vocal_identificada = max(similitudes, key=similitudes.get)
C_max = similitudes[vocal_identificada]

plt.tight_layout()
plt.show()

# 4. Resultados por consola
print("\n==================================================")
print(" RESULTADOS FINALES DEL SISTEMA")
print("==================================================")
for v in vocales:
    print(f"Medida de similitud C_{v}: {similitudes[v]:.4f}")
print(f"Valor máximo (C_max): {C_max:.4f}")
print(f"--> Vocal identificada: {vocal_identificada}")
print("==================================================")

# 5. Gráfica de barras resumen de similitudes
plt.figure(figsize=(8, 4))
plt.bar(similitudes.keys(), similitudes.values(), color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
plt.title(f"Medidas de Similitud Normalizada (Identificada: {vocal_identificada})[cite: 1]")
plt.xlabel("Vocales de Referencia[cite: 1]")
plt.ylabel("Similitud Máxima Normalizada (C_v)[cite: 1]")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, 1.05)
plt.show()