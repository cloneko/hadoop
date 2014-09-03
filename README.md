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
