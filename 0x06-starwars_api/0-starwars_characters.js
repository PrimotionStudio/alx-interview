#!/usr/bin/node
const { rejects } = require("assert");
const { error, log } = require("console");
const { resolve } = require("path");
const req = require("request");

const FILM_ID = process.argv[2];
const FILM_URL = 'https://swapi-api.alx-tools.com/api/films';

const requestPromise = (url) => {
    return new Promise((resolve, reject) => {
        req(url, (error, response, body) => {
            if (!error && response.statusCode == 200)
                resolve(JSON.parse(body))
            reject("An error occured");
        });
    });
};

const get_all_films = async () => {
    const films = await requestPromise(`${FILM_URL}/${FILM_ID}/`);
    const characters = films.characters;

    for (let index = 0; index < characters.length; index++) {
        const character_url = characters[index];
        const character = await requestPromise(character_url);
        console.log(character['name']);
    }
};
get_all_films();