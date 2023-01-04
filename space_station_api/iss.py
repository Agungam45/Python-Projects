import requests, json, turtle

iss = turtle.Turtle() #initiate pointer

def setup(window): #Window and Turtle setup
    global iss

    window.setup(1000, 500) #increase the screen size to 1000x500 pixels
    window.bgpic('earth.gif') #Background image
    window.setworldcoordinates(-180, -90, 180, 90) #Reset coordinates of the turtle 
    turtle.register_shape("iss.gif") #let module know where want to use an image as a shape
    iss.shape("iss.gif") #Set shape to the gif
    

def move_iss(lat, long):
    global iss

    iss.penup() # lift pen
    iss.goto(long, lat) #move pen to the correct coordinate 
    iss.pendown() #drop pen

def track_iss():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    if (response.status_code == 200) :
        response_dictionary = json.loads(response.text)
        position = response_dictionary['iss_position']
        print('International Space Station at ' +
            position['latitude'] + ', ' + position['longitude'])
        lat = float(position['latitude']) #convert strings into floats 
        long = float(position['longitude']) #convert into float
        move_iss(lat, long)
    else:
        print("Houston, we have a problem:" , response.status_code)
    widget = turtle.getcanvas()
    widget.after(5000, track_iss)
    
    

def main():
    global iss
    screen = turtle.Screen() # Reference to the turtle's screen object
    setup(screen)
    track_iss()

if __name__ == "__main__":
    main()
    turtle.mainloop()






    

turtle.mainloop() #displays the turtle window
