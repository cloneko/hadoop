Hadoop&Hive test
============================

Description
----------------------------

...

Env
----------------------------

* Download Hadoop and Hive
* Extract Donwloaded file and Setting PATH/JAVA_HOME



Usage
----------------------------

### Convert data and Boot hive

    python3 convert.py > output.tsv
    hive

### Initialize 

    CREATE TABLE nicometa (video_id STRING, title STRING,description STRING,upload_time DATE,length INT,view_counter INT,mylist_counter INT,comment_counter INT,tags STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n'; 
    LOAD DATA LOCAL INPATH '/path/to/output.tsv' OVERWRITE INTO TABLE nicometa; 

Ref 
----------------------------

* [Hadoop](http://hadoop.apache.org/)
* [Hive](http://hive.apache.org/)
* [SQLライクにHadoop Hiveを使い倒す! (1/3)](http://www.atmarkit.co.jp/ait/articles/0903/09/news094.html)
