
-- drop table discord_user
create table discord_user(
    user_cod bigint,
    name varchar(100),
    discriminator int,
    img_url varchar(500),
    primary key (user_cod) 
);