# UNAD-BigData-Tarea3-SparkStreaming
# UNAD – Big Data  
## Tarea 3: Procesamiento de Datos con Apache Spark y Kafka  

### 📘 Descripción del proyecto  
Este proyecto fue desarrollado como parte de la **Tarea 3 – Procesamiento de Datos con Apache Spark**, del curso **Big Data** del programa **Ingeniería de Sistemas – UNAD**.  
Su objetivo es implementar una solución de análisis de grandes volúmenes de datos utilizando **Apache Spark** y **Apache Kafka**, abordando tanto el procesamiento por lotes (*batch*) como el procesamiento en tiempo real (*streaming*).

### 🚀 Tecnologías utilizadas  
- **Apache Spark 3.x**  
- **Apache Kafka 3.x**  
- **Python 3.10+**  
- **OpenJDK 17**  
- **HDFS / Parquet** (para almacenamiento de resultados)  

### ⚙️ Estructura del repositorio
UNAD-BigData-Tarea3-SparkStreaming/
│
├─ batch/
│ └─ etl_batch.py → procesamiento batch con Spark DataFrames
├─ streaming/
│ ├─ producer.py → generador de datos para Kafka
│ └─ streaming_job.py → consumo y análisis en tiempo real con Spark Streaming
├─ data/ → dataset base (ejemplo: accidentes.csv)
├─ output/ → resultados generados por Spark (Parquet/JSON)
├─ README.md → este archivo descriptivo
└─ LICENSE → licencia MIT

### 🧠 Objetivos del proyecto  
1. Investigar y comparar Hadoop vs Spark, conceptos de RDDs, DataFrames y arquitectura de Kafka.  
2. Desarrollar un procesamiento **batch** con Apache Spark.  
3. Implementar un flujo de datos **streaming** usando Kafka + Spark Structured Streaming.  
4. Documentar el flujo completo de ingestión, transformación y almacenamiento de datos.  
5. Generar un informe, presentación y video explicativo conforme a la guía de la UNAD.

### 🧩 Requisitos de entorno
#```bash
#sudo apt update
#sudo apt install openjdk-17-jdk python3-pip -y
#pip install pyspark==3.4.2 kafka-python
