-- drop table collection
create table collection(
    collection_cod serial unique,
    player_cod int,
    pull_cod int,
    primary key (collection_cod),
    unique (player_cod, pull_cod),
    foreign key (player_cod) references player on delete cascade,
    foreign key (pull_cod) references pull on delete cascade
);