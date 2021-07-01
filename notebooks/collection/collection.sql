-- drop table collection
create table collection(
    collection_cod serial unique,
    player_cod int,
    pull_cod int,
    quantity int default 1,
    primary key (collection_cod),
    unique (player_cod, pull_cod),
    foreign key (player_cod) references player on delete cascade,
    foreign key (pull_cod) references pull on delete cascade
);

create or replace function fun_collection_acc() returns trigger as
    $$
    declare
        var int;
    begin
        var := (select quantity from collection where player_cod=new.player_cod and pull_cod=new.pull_cod);
        if (var is not null) then
            update collection set quantity=var+1 where player_cod=new.player_cod and pull_cod=new.pull_cod;
            return null;
        else
            return new;
        end if;
    end;
    $$ language plpgsql;

create trigger tri_collection_acc before insert on collection for each row execute function fun_collection_acc();
