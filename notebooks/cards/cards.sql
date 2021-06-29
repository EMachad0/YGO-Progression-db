
-- drop table card
create table card(
    card_cod int,
    name varchar(100),
    type varchar(100),
    flavour_text text,
    atk int,
    def int,
    level int,
    scale int,
    race varchar(100),
    attribute varchar(100),
    archetype varchar(100),
    cod_img int,
    link_val int,
    link_markers int,
    primary key (card_cod)
);


