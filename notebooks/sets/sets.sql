-- "set_name":"Legend of Blue Eyes White Dragon","set_code":"LOB","num_of_cards":355,"tcg_date":"2002-03-08"

-- drop table set
create table set(
    set_cod varchar(3),
    set_name varchar(100),
    num_of_cards int,
    release_date date,
    banlist_release int,
    banlist_end int,
    foreign key (banlist_release) references banlist on update cascade on delete set null,
    foreign key (banlist_end) references banlist on update cascade on delete set null,
    primary key (set_cod)
);
