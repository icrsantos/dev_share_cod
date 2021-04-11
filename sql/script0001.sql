create database dev_share;

use dev_share;

create user 'springuser'@'%' identified by 'sinistro';

grant all on dev_share.* to 'springuser'@’%’ ;

create table usuario (
    id             int auto_increment primary key,
    data_alteracao datetime(6)  not null,
    email          varchar(255) null,
    nome           varchar(255) not null,
    senha          varchar(255) not null,
    data_insercao  datetime(6)  not null,
    constraint usuario_pk unique (nome, senha)
);


create table postagem (
    id                     int auto_increment primary key,
    data_alteracao         datetime(6)                          not null,
    conteudo               longtext                             null,
    tipo                   varchar(20)                          not null,
    titulo                 varchar(255)                         not null,
    postagem_respondida_id int                                  null,
    usuario_id             int                                  not null,
    data_insercao          datetime(6)                          not null,
    relevacia              int         default 0                not null,
    situacao               varchar(20) default 'NAO_RESPONDIDA' not null,
    constraint FK34st6ne0plpc5gm60od333y8q foreign key (postagem_respondida_id) references postagem (id),
    constraint FKpja26t3vck8aga5ckfeea4cuw foreign key (usuario_id) references usuario (id)
);



