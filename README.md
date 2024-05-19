# Disributed_Hadoop_Assignment


### Installations anf setup

1. Install docker-Desktop and login
2. clone docker-hadoop
3. make build
4. docker-compose up -d [ To start 5 basic containers in hadoop ].
5. docker exec -it namenode bash
    -   It is basically a mini-linux. It will allow us to manage our HDFS file system.
6. Created new folder /user/root/ in namenode
7. exit
8. Downloaded Map-Reduce.jar
9. Moved .jar, .txt to namenode:/tmp
10.  docker exec -it namenode bash
11. Create /input in /user/root and put the .txt file in /user/root/input/ [hdfs dfs -put /tmp/file.txt /user/root/input]
12. hadoop jar hadoop-mapreduce-examples-2.7.1-sources.jar org.apache.hadoop.examples.WordCount input output
13. docker-compose down , after restarting docker, files in tmp are vanished, but files in /user/root/input exists.


### runner-script 
- Usage: ./runner-script.py
- Helps in preprocessing input[-ps No preprocessing using runner-script in the assignment]
- copying input files to docker-hadoop
- executing hadoop map-reducer .jar in hdfs 


#### Running in Hadoop

hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files mapper.py,reducer.py -input /in/adj.txt -output /out/ -mapper mapper.py -reducer reducer.py

./runner-script.py /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar ./input /in /out

"""
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-* \
-input input.txt \
-output output \
-mapper "python3 mapper0.py | { for i in {1..10}; do python3 mapper1.py | python3 reducer0.py; done; }" \
-reducer "python3 reducer1.py" \
-file mapper0.py \
-file mapper1.py \
-file reducer0.py \
-file reducer1.py
"""

"""
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-* \
-input input.txt \
-output output \
-mapper "python3 your_mapper.py" \
-numReduceTasks 0 \
-file your_mapper.py
"""
