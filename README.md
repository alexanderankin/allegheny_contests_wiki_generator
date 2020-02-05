# Automated Installer for Mediawiki

## Features

What currently works:

* database check table names
* database create db and reconnect
* database parse name from error and connection string url
* virtual environment creation
* virtual environment selecting
* virtual environment installing packages into

## Usage

This repository is supposed to push to Heroku. It has a tarball of the latest
Mediawiki, which it undoes, simulates some requests to itself to finish the
install and then adds a bunch of pages with python wiki bot.

To customize this, eventually should be ENV var hooks, and they should be
documented here, but for now, they should be accomplished by editing the
`script.py` file. 
