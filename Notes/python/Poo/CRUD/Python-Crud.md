Flask | python | mariadb

```python 
from flask import Flask

carsales = Flask(__name__)

carsales.route("/")

if(__name__ == "__main__"):
	carsales.run()
```

The ``carsales.route("/")`` sets route of the site. 


This if is verifying the __name__  
``` python
if(__name__ == "__main__"):
	carsales.run()
```


