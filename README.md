#MacNamer
MacNamer is a combination of a Django web app and a companion script to run on your client Macs with the goal of setting the name of your Macs.

##Why?
I'm rather OCD about the names of the Macs I look after. I like them to follow the convention of ABC 123 where ABC is a unique identifier for that set of macs and the number increments from 1. MacNamer will also pad the front of the name with the appropriate number of leading zeroes so your ARD lists line up nicely.

##Server installation
* [Ubuntu](https://github.com/grahamgilbert/macnamer/wiki/Installation-on-Ubuntu)
* [Docker](https://github.com/macadmins/macnamer)
* OS X

##Deploying to clients
Installation is simple - [install the package](https://github.com/grahamgilbert/macnamer/releases) using your favourite method, and then set the preference to point to the ServerURL. You can use MCX, Profiles, or plain old defaults write:

	defaults write /Library/Preferences/com.grahamgilbert.macnamer ServerURL "http://macnamer.yourserver.com"

##Usage
MacNamer is divided into groups, and within each group are computers and networks. 

###Computer Numbers
If you set a prefix for the group, MacNamer will auto increment the number - it for example, set ABC as the prefix and your first machine will be ABC 1.

###Networks
If you assign a network to a group, any new request that comes from that network will be assigned the next available number (if you're using the auto naming functionality). If you don't wish Macs to be automatically added to MacNamer, don't assign any networks to a group.

You should enter the network as the LAN subnet xxx.xxx.xxx.0 (e.g. 192.168.10.0) - there isn't currently any support for subnets other than /24, although you can enter multiple subnets, nor is there any validation currently of the field, so make sure you're entering your desired subnets correctly.

###Permissions
You can assign permissions for creating, modifying and deleting to users for groups, computers and networks from within the administration pages. For more information on permissions, please check the [Django documentation](https://docs.djangoproject.com/en/dev/topics/auth/).

##Acknowledgements
Many thanks to my lovely employers at [pebble.it](http://pebbleit.com) for letting me release this.
