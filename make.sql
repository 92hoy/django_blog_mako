use main;

alter table Board modify column modify_date  datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
alter table Board modify column create_date  datetime DEFAULT CURRENT_TIMESTAMP;
alter table User modify column create_date  datetime DEFAULT CURRENT_TIMESTAMP;
alter table User modify column modify_date  datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
alter table User ALTER user_role set default 'U';
alter table User ALTER delete_yn set default 'N';