with
    url_code := <str>$url_code,
    location := <str>$location,
update Meeting
filter .url_code = url_code
set {location := location}
