# alfred-random-password

An [alfred](https://alfredapp.com) workflow that generates and copy into your
clipboard a random password by typing the keyword `passwd`.

## Variables

You can configure your password specification by changing the workflow variables.

| Variable    | Description                                                    |
|-------------|----------------------------------------------------------------|
| max_repeats | Number of max repeating character, number or symbol            |
| separator   | Word separator to be used. Set to empty to not use a separator |
| word_length | When using a separator, the length of a single "word"          |
| words       | Number of "words" to be used.                                  |