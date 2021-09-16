# Teams Bot - A lazy student's guardian angel

### Purpose of this bot

- Log in to teams web app
- Join classes based off a predefined schedule

### Requirements

- all requirements will be in requirements.txt
- to install all requirements

```bash
pip3 install -r requirements.txt
```

### Configure

- The creds for the teams account will be stored in _.creds.json_ file
- Create a _.creds.json_ file in project's root dir
- Store your creds in the following format:

```json
{
    "email": "test@mail.com",
    "password": "mypasswordsucks!"
}
```

- If you were to modify it in your own repo don't worry cos the _.creds.json_ file is in the _.gitignore_ so it won't get pushed to the repo

---