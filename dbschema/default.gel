module default {

    abstract type Auditable {
        required created_at -> cal::local_datetime {
            readonly := true;
            default := cal::to_local_datetime(datetime_current(), 'Asia/Seoul');
        }
    }
    
    type Meeting extending Auditable {
        required url_code: str{
            constraint exclusive;
            readonly := true;
		    };
    }
    
}