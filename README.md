<p align="center">
	<b>postloris</b>
	<br>
	<i>An HTTP POST spam tool. Random values, random User-Agent.</i>
	<br><br><br>
	<img alt="Sreenshot_1" src="https://user-images.githubusercontent.com/48186982/63628062-c9da2480-c60a-11e9-9d71-e6764d500a15.png">
</p>

# Syntax
```
$ python3 postloris.py
                 _   _            _
                | | | |          (_)
 _ __   ___  ___| |_| | ___  _ __ _ ___
| '_ \ / _ \/ __| __| |/ _ \| '__| / __|
| |_) | (_) \\__ \ |_| | (_) | |  | \__ \
| .__/ \___/|___\\__|_|\___/|_|  |_|___/
| |
|_|

Usage: postloris.py <url> <threads> [fields]
Examples: python3 postloris.py http://localhost/login.php 25 email password
          python3 postloris.py http://localhost/login.php 16 login pass key
          python3 postloris.py http://localhost/login.php 4 username
```

* In **url**, you need to specify address where POST requests are parsed.
* In **threads**, you need to specify an amount of threads used by script.
* In **fields**, you need to specify name of field (email/password/username/login etc.).

![Screenshot_2](https://user-images.githubusercontent.com/48186982/63627895-fccfe880-c609-11e9-8feb-3059983b9e56.png)
