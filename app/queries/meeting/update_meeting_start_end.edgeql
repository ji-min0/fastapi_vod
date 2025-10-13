with
    url_code := <str>$url_code,
    start_date := <cal::local_date>$start_date,
    end_date := <cal::local_date>$end_date,
select (
    update Meeting
    filter .url_code = url_code
    set {start_date := start_date, end_date := end_date}
) {url_code, start_date, end_date, location, title}
limit 1
