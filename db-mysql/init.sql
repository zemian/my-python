create database testdb;

create table test(
    id int primary key auto_increment,
    dt datetime,
    amount decimal(12, 2),
    measurement float,
    name varchar(1000),
    code char(3),
    flag boolean,
    content text);

insert into test values(1, '2022-03-29 15:00:00', 300000.10, 0.1, 'test', 'ABC', true, 'Hello World.');
insert into test values(2, '2022-03-29 19:00:00', 300000.20, 0.2, 'test2', 'DEF', true, 'Hello World again.');

select sum(measurement), sum(amount) from test;

select now(), dt, now() - dt from test;
select date_format(dt, '%Y-%m-%dT%TZ') from test;