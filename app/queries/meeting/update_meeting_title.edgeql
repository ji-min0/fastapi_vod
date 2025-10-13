with
    url_code := <str>$url_code,
    title := <str>$title,
update Meeting
filter .url_code = url_code
set {title := title}