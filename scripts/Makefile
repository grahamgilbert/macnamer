include /usr/local/share/luggage/luggage.make

TITLE=MacNamer
PACKAGE_NAME=MacNamer
REVERSE_DOMAIN=com.grahamgilbert
PACKAGE_TARGET_OS=10.5
PLIST_FLAVOR=pkg-info
PAYLOAD=\
			pack-script\
			pack-Library-LaunchDaemons-com.grahamgilbert.macnamer.plist\
            pack-script-postflight

pack-script: l_usr_local
		@sudo mkdir -p ${WORK_D}/usr/local/macnamer/
		@sudo ${CP} namer ${WORK_D}/usr/local/macnamer/namer
		@sudo chown -R root:wheel ${WORK_D}/usr/local/macnamer/