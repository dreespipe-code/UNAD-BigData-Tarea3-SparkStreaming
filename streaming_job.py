from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window, count, expr
from pyspark.sql.types import StructType, StringType, IntegerType

spark = (SparkSession.builder
         .appName("UNAD-Tarea3-Streaming")
         .getOrCreate())

schema = (StructType()
          .add("ts", StringType())
          .add("barrio", StringType())
          .add("tipo_evento", StringType())
          .add("lesionados", IntegerType()))

raw = (spark.readStream
       .format("kafka")
       .option("kafka.bootstrap.servers","localhost:9092")
       .option("subscribe","accidentes_rt")
       .option("startingOffsets","latest")
       .load())

json_df = raw.selectExpr("CAST(value AS STRING) AS v")              .select(from_json(col("v"), schema).alias("data"))              .select("data.*")

agg = (json_df
       .withColumn("ts_ts", expr("to_timestamp(ts)"))
       .groupBy(window(col("ts_ts"), "1 minute", "30 seconds"), col("barrio"))
       .agg(count("*").alias("eventos")))

query_console = (agg.writeStream.outputMode("update")
                 .format("console").option("truncate","false")
                 .start())

query_fs = (agg.writeStream.outputMode("append").format("parquet")
            .option("path","output/stream/accidentes_win")
            .option("checkpointLocation","output/stream/_chk")
            .start())

query_console.awaitTermination()
query_fs.awaitTermination()
