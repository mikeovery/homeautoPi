# homeautoPi

[TingBot](http://tingbot.com) Application Developed on Tide

Displays interactive panels of information, each Panel displays a 4x4 grid of tiles with activity and data defined in the pagedata.json file

Each Tile can be one of:
```
label - Simple Text
datalabel - Text from a url source (text or JSON)
button - on / off functionality
image - small icon e.g. for weather
```

## Tile Button
The tile supports interaction 

**act**: tile image to display for active  
**inact**: tile image to diaplay for inactive  
**on_action**: HTTP method and URL for the action to perform to enable   
**off_action**: HTTP method and URL for the action to perform to disable   
**data**: HTTP method and URL to get the current state data  
**actvalue**: type and value for the active state  

e.g.
> "A2": {  
>  "act": "on.png",  
>  "inact": "off.png",  
>  "on_action": "GET,http://192.168.0.2:8080/api/sensor/hall/on,",  
>  "off_action": "GET,http://192.168.0.2:8080/api/sensor/hall/off,",  
>  "data": "GET,http://192.168.0.2:8080/api/sensor/hall/state,",  
>  "actvalue": "int,1"  
> }

## Data Tile
The tile supports data displays

**dispdata**: HTTP method and URL to get the current state data  
**headers**: HTTP headers to pass if the url requires them  
**jsonValue**: json location for data retreival  
**syntax**: display string to use where {0} is the value to display  

e.g.
> "B2": {  
>  "dispdata": "GET,http://192.168.0.3:5182/characteristics?id=17.13,",   
>  "headers": {"Authorization":"passstring"},   
>  "jsonValue": "['characteristics'][0].get('value')",  
>  "syntax": "{0} ºC"  
> }

