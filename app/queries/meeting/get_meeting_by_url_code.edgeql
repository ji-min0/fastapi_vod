with
    url_code := <str>$url_code,
select Meeting { url_code, start_date, end_date, title, location }  # 컬럼 추가
filter .url_code = url_code
limit 1