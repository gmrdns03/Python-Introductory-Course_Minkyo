drop table dept;
drop table sawon;
drop table gogek;

create table dept (
deptno number(3),
dname varchar2(10),
loc varchar2(20)
);

create table gogek (
gobun number(3),
goname varchar2(10),
gotel varchar2(20),
gojumin varchar2(14),
godam number(3)
);

create table sawon (
sabun number(3),
saname varchar2(10),
deptno number(3),
sajob varchar2(10),
sapay number(10),
sahire date,
sasex varchar2(4),
samgr number(3)
);

select * from tab;