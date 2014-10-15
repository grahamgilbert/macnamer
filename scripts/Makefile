USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make
TITLE=MacNamer
PACKAGE_NAME=MacNamer
REVERSE_DOMAIN=com.grahamgilbert

PAYLOAD=\
			pack-script\
			pack-Library-LaunchDaemons-com.grahamgilbert.macnamer.plist\
            pack-script-postinstall

pack-script: l_usr_local
		@sudo mkdir -p ${WORK_D}/usr/local/macnamer/
		@sudo ${CP} namer ${WORK_D}/usr/local/macnamer/namer
		@sudo chown -R root:wheel ${WORK_D}/usr/local/macnamer/