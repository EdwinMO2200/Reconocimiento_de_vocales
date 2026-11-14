# Sistema de Reconocimiento de Vocales en Tiempo Real

Implementación en Python de un sistema básico de procesamiento digital de señales para el reconocimiento de vocales en tiempo real, utilizando grabación de audio por micrófono y análisis mediante **Correlación Cruzada Normalizada**.

## 🚀 Características Principales

* **Captura de audio en tiempo real:** Utiliza `sounddevice` para adquirir señales de audio a una frecuencia de muestreo de $44,100\text{ Hz}$.
* **Recorte de segmentos estables:** Extrae un segmento de 1 segundo de la vocal sostenida para evitar transitorios de inicio y finalización.
* **Emparejamiento de patrones:** Compara la vocal de prueba contra patrones de referencia de las 5 vocales (`A`, `E`, `I`, `O`, `U`).
* **Normalización de energía:** Calcula la correlación cruzada normalizada para obtener coeficientes de similitud independientes de la amplitud de la voz.
* **Visualización avanzada:** Genera un panel gráfico con las curvas de correlación temporal y un diagrama de barras resumen con los puntajes de similitud utilizando `matplotlib`.

---

## 📋 Requisitos e Instalación

Asegúrate de tener Python instalado junto con las siguientes librerías científicas y de audio:

```bash
pip install numpy sounddevice matplotlib