-- drop table player
create table player(
    player_cod serial,
    user_cod bigint,
    server_cod bigint,
    primary key (player_cod),
    unique (user_cod, server_cod),
    foreign key (user_cod) references discord_user on delete cascade,
    foreign key (server_cod) references discord_server on delete cascade
);
