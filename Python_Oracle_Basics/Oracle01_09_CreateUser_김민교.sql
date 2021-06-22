SQL> show user
USER is "HR"
SQL> conn /as sysdba
Connected.
SQL> create user angel identified by angel;

User created.

SQL> desc all_users;
 Name
           Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 USERNAME
           NOT NULL VARCHAR2(30)
 USER_ID
           NOT NULL NUMBER
 CREATED
           NOT NULL DATE

SQL> select username from all_users;

USERNAME
------------------------------------------------------------
XS$NULL
ANGEL
APEX_040000
APEX_PUBLIC_USER
FLOWS_FILES
HR
MDSYS
ANONYMOUS
XDB
CTXSYS
APPQOSSYS
DBSNMP
ORACLE_OCM
DIP
OUTLN
SYSTEM
SYS

17 rows selected.