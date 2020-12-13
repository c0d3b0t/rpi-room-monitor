# RPi Space Monitor

## Dependencies

### Install pipenv

Run `pip3 install pipenv` to install the pipenv package.

After the pipenv installation, you may see warning:
```
The script virtualenv is installed in '/home/pi/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

To add that directory to the PATH, we need to edit the `~/.bash_profile`.

Open the terminal and run `echo 'export PATH=$PATH:/home/pi/.local/bin' >> ~/.bash_profile && source ~/.bash_profile`.
Now if you look into `~/.bash_profile` you should see the `export PATH=$PATH:/home/pi/.local/bin` string added to the end of that file. 

### Install dependencies

In the root of the project, in the terminal, run `pipenv install` to install dependencies from `Pipfile`.

### Libgpiod

In case if you're getting 500 internal server error, and you see a log message related to missing `libgpiod`, run `sudo apt-get install libgpiod2 python3-libgpiod gpiod` to install missing dependencies.