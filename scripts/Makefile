include /usr/local/share/luggage/luggage.make

TITLE=MacNamer
PACKAGE_NAME=Macnamer
REVERSE_DOMAIN=com.grahamgilbert
PAYLOAD=\
			pack-script\
			pack-Library-LaunchDaemons-com.pebbleit.namer.plist\
            pack-script-postflight

pack-script: l_usr_local
		@sudo mkdir -p ${WORK_D}/usr/local/macnamer/
		@sudo ${CP} namer ${WORK_D}/usr/local/macnamer/namer