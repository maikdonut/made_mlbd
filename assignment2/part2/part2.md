__Создадим таблицу artists в Hive и загрузим в нее данные:__

```sql
CREATE TABLE IF NOT EXISTS artists (
    `mbid` string,
    `artist_mb` string,
    `artist_lastfm` string,
    `country_mb` string,
    `country_lastfm` string,
    `tags_mb` string,
    `tags_lastfm` string,
    `listeners_lastfm` int,
    `scrobbles_lastfm` int,
    `ambiguous_artist` string
 )
 COMMENT 'Music artists popularity'
 ROW FORMAT DELIMITED
 FIELDS TERMINATED BY ','
 LOAD DATA INPATH '/home/michael/artists.csv' INTO TABLE artists
 ```
 __а). Исполнитель с максимальным числом скробблов__
 ```sql
SELECT artist_lastfm, scrobbles_lastfm
FROM artists
WHERE scrobbles_lastfm IN (
   SELECT MAX(scrobbles_lastfm)
   FROM artists
)
Результат записан в файл task_a.csv
```
 __b). Самый популярный тэг на ластфм__
 ```sql
SELECT tag, count(*) as tag_val 
FROM artists
LATERAL VIEW explode(split(tags_lastfm, ';')) tags as tag
WHERE tag != ''
GROUP BY tag
SORT BY tag_val DESC
LIMIT 3
На первом месте увидем nan, поэтому возьмем второе значение
Результат записан в файл task_b.csv
 ```
 __c). Самые популярные исполнители 10 самых популярных тегов ластфм__
 ```sql
WITH top_tags as (
    SELECT tag, count(*) as tag_val
    FROM artists
    LATERAL VIEW EXPLODE(split(tags_lastfm, ';')) tags as tag
    WHERE tag != ''
    GROUP BY tag
    SORT BY tag_val DESC
    LIMIT 10
    ),
artists_tags as (
    SELECT artist_lastfm, tag, scrobbles_lastfm
    FROM artists
    LATERAL VIEW EXPLODE(split(tags_lastfm, ';')) tags as tag
)
SELECT DISTINCT artist_lastfm, scrobbles_lastfm
FROM artists_tags
WHERE tag IN (
    SELECT tag 
    FROM top_tags
)
SORT BY scrobbles_lastfm DESC
LIMIT 10
```
Результат записан в файл task_c.csv

 __d). Топ 10 исполнителей в США__
 ```sql
SELECT artist_lastfm, country_lastfm, listeners_lastfm
FROM artists 
WHERE country_lastfm = 'United States'
SORT BY listeners_lastfm DESC
LIMIT 10
```
Результат записан в файл task_d.csv
 
