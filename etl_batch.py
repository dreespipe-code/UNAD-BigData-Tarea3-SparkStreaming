from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, year, month, hour, when, count

spark = (SparkSession.builder
         .appName("UNAD-Tarea3-Batch")
         .config("spark.sql.shuffle.partitions", "200")
         .getOrCreate())

df = (spark.read.option("header", True)
               .option("inferSchema", True)
               .csv("data/accidentes.csv"))

df2 = (df.withColumn("ts", to_timestamp(col("fecha_hora")))
         .withColumn("anio", year(col("ts")))
         .withColumn("mes", month(col("ts")))
         .withColumn("hora", hour(col("ts")))
         .withColumn("lesionados", when(col("lesionados").isNull(), 0).otherwise(col("lesionados"))))

eventos_barrio_hora = (df2.groupBy("barrio","hora").agg(count("*").alias("eventos")))

(eventos_barrio_hora
 .repartition("anio","mes")
 .write.mode("overwrite")
 .partitionBy("anio","mes")
 .parquet("output/batch/eventos_barrio_hora"))

top10 = (eventos_barrio_hora.orderBy(col("eventos").desc()).limit(10))
top10.write.mode("overwrite").json("output/batch/top10_barrios")

spark.stop()
