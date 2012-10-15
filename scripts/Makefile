include /usr/local/share/luggage/luggage.make

TITLE=MacNamer
PACKAGE_NAME=Macnamer
REVERSE_DOMAIN=com.grahamgilbert
#PACKAGE_TARGET_OS=10.5
PAYLOAD=\
			pack-script\
			pack-Library-LaunchDaemons-com.pebbleit.namer.plist \
			pack-script-postinstall

pack-script: l_usr_local
		@sudo mkdir -p ${WORK_D}/usr/local/macnamer/
		@sudo ${CP} namer ${WORK_D}/usr/local/macnamer/namer