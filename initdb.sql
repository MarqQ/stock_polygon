CREATE DATABASE stockdb
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Table: public.stock_model

-- DROP TABLE IF EXISTS public.stock_model;

CREATE TABLE IF NOT EXISTS public.stock_model
(
    id integer NOT NULL DEFAULT nextval('stock_model_id_seq'::regclass),
    after_hours double precision,
    close double precision,
    from_date character varying COLLATE pg_catalog."default",
    high double precision,
    low double precision,
    open double precision,
    pre_market double precision,
    status character varying COLLATE pg_catalog."default",
    symbol character varying COLLATE pg_catalog."default",
    volume integer,
    CONSTRAINT stock_model_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stock_model
    OWNER to postgres;
-- Index: ix_stock_model_id

-- DROP INDEX IF EXISTS public.ix_stock_model_id;

CREATE INDEX IF NOT EXISTS ix_stock_model_id
    ON public.stock_model USING btree
    (id ASC NULLS LAST)
    TABLESPACE pg_default;