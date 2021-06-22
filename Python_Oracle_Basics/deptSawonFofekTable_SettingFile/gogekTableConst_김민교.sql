drop table gogek;

create table gogek (
gobun number(3),
goname varchar2(10),
gotel varchar2(20),
gojumin varchar2(14),
godam number(3),
constraint gogek_gobun_pk primary key (gobun),
constraint gogek_godam_fk foreign key (godam) references sawon(sabun)
);

select * from tab;