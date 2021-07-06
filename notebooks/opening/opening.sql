-- drop table collection
create table opening(
    open_cod serial,
    set_cod varchar(3),
    player_cod int,
    quantity int default 0,
    primary key (open_cod),
    unique (set_cod, player_cod),
    foreign key (player_cod) references player on delete cascade,
    foreign key (set_cod) references set on delete cascade
);
