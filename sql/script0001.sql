create database dev_share;
use dev_share;
create user 'springuser'@'%' identified by 'sinistro';
grant all on dev_share.* to 'springuser'@’%’ ;

create table usuario
(
   id             int auto_increment primary key,
   data_alteracao datetime(6)   not null,
   email          varchar(255)  null,
   nome           varchar(255)  not null,
   senha          varchar(255)  not null,
   data_insercao  datetime(6)   not null,
   pontos         int default 0 not null,
   constraint usuario_id_uindex
       unique (id),
   constraint usuario_pk
       unique (nome, senha)
);





create table postagem
(
   id                     int auto_increment primary key,
   data_alteracao         datetime(6)                          not null,
   conteudo               longtext                             null,
   tipo                   varchar(20)                          not null,
   titulo                 varchar(255)                         not null,
   postagem_respondida_id int                                  null,
   usuario_id             int                                  not null,
   data_insercao          datetime(6)                          not null,
   relevancia             int         default 0                not null,
   situacao               varchar(20) default 'NAO_RESPONDIDA' not null,
   curtidas               int         default 0                not null,
   constraint postagem_id_uindex
       unique (id),
   constraint FK34st6ne0plpc5gm60od333y8q
       foreign key (postagem_respondida_id) references postagem (id),
   constraint FKpja26t3vck8aga5ckfeea4cuw
       foreign key (usuario_id) references usuario (id)
);



create table ecos_postagem
(
  id int auto_increment primary key ,
  data_insercao datetime(6) not null,
  data_alteracao datetime(6) not null,
  postagem_id int not null,
  usuario_id int not null,
  constraint ecos_postagem_pk_2
     unique (postagem_id, usuario_id),
  constraint ecos_pergunta_postagem_id_fk
     foreign key (postagem_id) references postagem (id),
  constraint ecos_pergunta_usuario_id_fk
     foreign key (usuario_id) references usuario (id)
);

create unique index ecos_postagem_id_uindex
  on ecos_postagem (id);


create table historico_notificacoes
(
   id                    int auto_increment primary key,
   data_insercao         datetime(6) not null,
   data_alteracao        datetime(6) not null,
   tipo                  varchar(20) not null,
   postagem_id           int         not null,
   usuario_notificado_id int         not null,
   mensagem_enviada      longtext    not null,
   constraint historico_notificacoes_id_uindex
       unique (id),
   constraint historico_notificacoes_postagem_id_fk
       foreign key (postagem_id) references postagem (id),
   constraint historico_notificacoes_usuario_id_fk
       foreign key (usuario_notificado_id) references usuario (id)
);



