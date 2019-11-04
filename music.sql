#!/usr/bin/python
# -*- coding: utf-8 -*-

CREATE TABLE artist (
    id int PRIMARY KEY,
    artist_name varchar(25) NOT NULL
);

CREATE TABLE album (
    id int PRIMARY KEY,
    album_name varchar(25) NOT NULL,
    artist_id int
 );

CREATE TABLE songs (
    id int PRIMARY KEY,
    song_name varchar(25) NOT NULL, 
    album_id int, 
    artist_id int,
    track_number int,
    track_length int
);