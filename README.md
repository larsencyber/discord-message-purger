# discord-message-purger
A Discord message purging tool, which can be used to delete all messages (including message replies) with a specific user, or in a specific channel.

# Installation 

* Get the latest version of python installed
* Run this command in a command prompt `"pip install discord discord.py-self"`
* Download main.py
* Run main.py
* Enter your discord token, scroll down to see how to get it
* Enter the persons dms you want to purge, and copy their userid into the program
* Enjoy

# Discord Token Retrieval

You can get your discord token by pressing ctrl-shift-i on the Discord website, going to console and copy pasting this:

(
    webpackChunkdiscord_app.push(
        [
            [''],
            {},
            e => {
                m=[];
                for(let c in e.c)
                    m.push(e.c[c])
            }
        ]
    ),
    m
).find(
    m => m?.exports?.default?.getToken !== void 0
).exports.default.getToken()
