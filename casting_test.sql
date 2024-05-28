--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Actors" (
    id integer NOT NULL,
    name character varying,
    age character varying,
    gender character varying,
    movie_id integer NOT NULL
);


ALTER TABLE public."Actors" OWNER TO postgres;

--
-- Name: Actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Actors_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Actors_id_seq" OWNER TO postgres;

--
-- Name: Actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Actors_id_seq" OWNED BY public."Actors".id;


--
-- Name: Movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Movies" (
    id integer NOT NULL,
    title character varying,
    release_date character varying
);


ALTER TABLE public."Movies" OWNER TO postgres;

--
-- Name: Movies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Movies_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Movies_id_seq" OWNER TO postgres;

--
-- Name: Movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Movies_id_seq" OWNED BY public."Movies".id;


--
-- Name: Actors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actors" ALTER COLUMN id SET DEFAULT nextval('public."Actors_id_seq"'::regclass);


--
-- Name: Movies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movies" ALTER COLUMN id SET DEFAULT nextval('public."Movies_id_seq"'::regclass);


--
-- Data for Name: Actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Actors" (id, name, age, gender, movie_id) FROM stdin;
1	Actor 1	18	Male	1
2	Actor 2	20	Male	1
3	Actor 3	21	Male	2
\.


--
-- Data for Name: Movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Movies" (id, title, release_date) FROM stdin;
1	Movies 1 Update	2024-05-27
2	Movies 2	2024-05-27
3	Movies 3	2024-05-27
4	Movies 4	2024-05-27
5	Movies 5	2024-05-27
\.


--
-- Name: Actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Actors_id_seq"', 3, true);


--
-- Name: Movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Movies_id_seq"', 5, true);


--
-- Name: Actors Actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actors"
    ADD CONSTRAINT "Actors_pkey" PRIMARY KEY (id);


--
-- Name: Movies Movies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movies"
    ADD CONSTRAINT "Movies_pkey" PRIMARY KEY (id);


--
-- Name: Actors Actors_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actors"
    ADD CONSTRAINT "Actors_movie_id_fkey" FOREIGN KEY (movie_id) REFERENCES public."Movies"(id);


--
-- PostgreSQL database dump complete
--

