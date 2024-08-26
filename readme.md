# sd_lab2
Laboratorio 2 de la asignatura Sistemas Distribuidos. Desarrollado por Matías Barolo y Hernán Aravena.
## Requisitos:
	- Python 3.10.7
	- Apache Kafka 3.8.0
	- Apache Spark 3.5.2
	- Librería kafka-python 2.0.2
	- Librería pyspark 3.5.2
	- Librería findspark 2.0.1

## Utilización:
	
	1. Instalar requisitos (Sección anterior)
	
	2. Comandos para ejecuciÃ³n de Apache Kafka y Apache Spark:

		-Kafka debe estar instalado en una ruta como la siguiente: "C:\kafka_2.12-3.8.0\"

		-En esta misma ruta, ejecutar ZoeKeeper con el siguiente comando: 
		```	
	bin\windows\zookeeper-server-start.bat config\zookeeper.properties
		```

		-En otro terminal (en la misma ruta) iniciar Kafka con el siguiente comando:
		```
			bin\windows\kafka-server-start.bat config\server.properties
		```	