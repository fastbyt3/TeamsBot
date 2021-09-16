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

### Configure credentials

- The creds for the teams account will be stored in _.config.json_ file
- Create a _.config.json_ file in project's root dir
- Store your creds in the following format:

```json
{
    "email": "test@mail.com",
    "password": "mypasswordsucks!"
}
```

- If you were to modify it in your own repo don't worry cos the _.creds.json_ file is in the _.gitignore_ so it won't get pushed to the repo

### Setting up the WebDriver

#### For Windows

- this was tested on **Chrome v93**
- Included `chromedriver.exe` in `./src` folder which is for _chrome v93_
- All you have to do is:
  - Check if your chrome version is 93 else download a [new driver](https://chromedriver.chromium.org/downloads) for your version of Chrome(ium)
  - update the chromedriver path in `.config.json` (refer the sample file)

    ```json
    "chromedriver": "your path"
    ```

> Note: your path should be like: C:\\SomeDir\\chromedriver.exe

- In case of using **Firefox** you can try using _GeckoDriver_ (not tested)

#### For Linux

- download the appropirate [chromedriver](https://chromedriver.chromium.org/downloads) based off our chrome version
- now export the path to where your driver is:

```bash
export PATH="$PATH:/path/to/chromedriver"
```

- and update the path in the _.config.json_ (refer the sample file)


---