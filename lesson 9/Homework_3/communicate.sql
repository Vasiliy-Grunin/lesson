select first_name, last_name, position_in_company from worker where chef in (select worker from chef where worker=2);
