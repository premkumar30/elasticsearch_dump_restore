
INDICES = [
        "documents_index",
        "england_geographies"
]

SRC_HOST = 'src_host'
SRC_PORT = 9200

DEST_HOST = 'dest_host'
DEST_PORT = 9200

MAPPING_CMD = 'elasticdump --input=http://%(SRC_HOST)s:%(SRC_PORT)s/%(INDEX)s --output=http://%(DEST_HOST)s:%(DEST_PORT)s/%(INDEX)s --type=mapping'
DATA_CMD = 'elasticdump --input=http://%(SRC_HOST)s:%(SRC_PORT)s/%(INDEX)s --output=http://%(DEST_HOST)s:%(DEST_PORT)s/%(INDEX)s --type=data'


for index in INDICES:
    print("Migrating %s Index..." % index)
    os.system(
        MAPPING_CMD.format({
            'SRC_HOST': SRC_HOST,
            'SRC_PORT': SRC_PORT,
            'DEST_HOST': DEST_HOST,
            'DEST_PORT': DEST_PORT,
            'INDEX': index
        })
    )
    print("%s Index Migrated" % index)

