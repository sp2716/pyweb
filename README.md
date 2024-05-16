Making a RESTful web service using Python Flask Package
    This Repository goal is to test and develop a web service capable of filling out a form and creating a JSON configuration.
    
currently this repo starts a webserver.

in the /config page - the user can set the IP of an Allen Bradley controller (slot 0 only) and a tag to poll.
on the main page the tag will be polled and updated once per second using AJAX

    This configuration resides on the same docker container as an Ethernet/IP server


