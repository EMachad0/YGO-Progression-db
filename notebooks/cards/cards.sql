
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

create or replace function fun_cards_ins() returns trigger as
    $$
    declare
        var int;
    begin
        var := (select count(*) from card where card_cod=new.card_cod);
        if (var = 0) then
            return new;
        else
            update card set name=new.name, type=new.type, flavour_text=new.flavour_text, atk = new.atk, def=new.def,
                            level=new.level, scale=new.scale, race=new.race, attribute=new.attribute, archetype=new.archetype,
                            cod_img=new.cod_img, link_val=new.link_val, link_markers=new.link_markers
                            where card_cod=new.card_cod;
            return null;
        end if;
    end;
    $$ language plpgsql;

create trigger tri_cards_inc before insert on card for each row execute function fun_cards_ins();