with
    url_code := <str>$url_code
select (
    insert Meeting {
        url_code := url_code,
    }
) {url_code}
