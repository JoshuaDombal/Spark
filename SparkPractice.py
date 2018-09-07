from pyspark import SparkContext




sc = SparkContext()

textFile = sc.textFile('example.txt')