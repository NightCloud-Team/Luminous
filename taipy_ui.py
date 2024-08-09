from taipy import Gui
from jinja2 import Template
from function.handle import *
pages = {
    "/" : 
    """
<!DOCTYPE html>
<html lang="en">

<head>
    

</head>

<body>


</body>

</html>

    """
}
Gui(pages=pages).run()
