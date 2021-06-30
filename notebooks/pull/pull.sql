-- drop table pull
create table pull(
    pull_cod serial unique,
    card_cod int,
    set_cod varchar(3),
    rarity varchar(100),
    rarity_code varchar(100),
    price varchar(30),
    primary key (pull_cod),
    unique (card_cod, set_cod, rarity),
    foreign key (card_cod) references card on delete cascade,
    foreign key (set_cod) references set on delete cascade
);