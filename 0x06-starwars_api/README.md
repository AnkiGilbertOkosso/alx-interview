# Star Wars Characters Printer

This script fetches and prints all characters of a specified Star Wars movie using the Star Wars API.

## Usage

To use the script, run it from the command line with the ID of the desired Star Wars movie as the first argument:

```
./0-starwars_characters.js <movie_id>
```

Where `<movie_id>` is an integer representing the ID of the Star Wars movie.

The script will then fetch the characters of the specified movie from the Star Wars API and print each character's name on a separate line.

## Example

```
./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Implementation Details

The script uses the `request` module to make HTTP requests to the Star Wars API. It fetches the characters of the specified movie, extracts their names, and prints them one per line.

## Error Handling

- If the user provides the wrong number of arguments or the argument is not a valid movie ID, the script will display a usage message and exit with status 1.
- If there is an error fetching the movie characters or their details from the API, the script will display the error message and exit with status 1.
