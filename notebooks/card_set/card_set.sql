
-- drop table card_set
create table card_set(
    card_cod int,
    set_cod varchar(3),
    rarity varchar(100),
    rarity_code varchar(100),
    price varchar(30),
    primary key (card_cod, set_cod, rarity),
    foreign key (card_cod) references card,
    foreign key (set_cod) references set
);