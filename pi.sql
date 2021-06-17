-- Table: public.reservas

-- DROP TABLE public.reservas;

CREATE TABLE public.reservas
(
    id bigint NOT NULL DEFAULT nextval('reservas_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default",
    phone character varying(100) COLLATE pg_catalog."default",
    date character varying(100) COLLATE pg_catalog."default",
    "time" character varying(100) COLLATE pg_catalog."default",
    num_people character varying(100) COLLATE pg_catalog."default",
    num_table character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT reservas_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.reservas
    OWNER to postgres;