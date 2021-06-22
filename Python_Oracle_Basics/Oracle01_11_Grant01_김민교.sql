SQL> show user
USER is "SYS"
SQL> create user angel identified by angel;

User created.

SQL> conn angel/angel;
ERROR:
ORA-01045: user ANGEL lacks CREATE SESSION privilege; logon denied


Warning: You are no longer connected to ORACLE.
SQL> conn /as sysdba;
Connected.
SQL> grant dba to angel;

Grant succeeded.

SQL> conn angel/angel;
Connected.
SQL>