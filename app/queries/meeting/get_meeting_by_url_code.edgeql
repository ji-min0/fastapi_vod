with
    url_code := <str>$url_code,
select Meeting { url_code }
filter .url_code = url_code
limit 1