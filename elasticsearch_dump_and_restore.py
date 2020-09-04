
INDICES = [
    "discovery_org_entities_v1",
    "discovery_log_v3",
    "discovery_log_admin",
    "discovery_chat",
    "revised_email_stats",
    "all_individual_v7",
    "all_practices_v1",
    "all_individual",
    "all_formulary_document_v10",
    'daily_stats_rollup',
    'discovery_email_events_v1',
    'local_notifications',
    "discovery_impersonate_index"
]


MAPPING_CMD = 'elasticdump --input=http://%(SRC_HOST)s:%(SRC_PORT)s/%(INDEX)s --output=http://%(DEST_HOST)s:%(DEST_PORT)s/%(INDEX)s --type=mapping'
DATA_CMD = 'elasticdump --input=http://%(SRC_HOST)s:%(SRC_PORT)s/%(INDEX)s --output=http://%(DEST_HOST)s:%(DEST_PORT)s/%(INDEX)s --type=data'


for index in INDICES:
    os.system(
        MAPPING_CMD.format({
            'SRC_HOST': 'localhost',
            'SRC_PORT': 9200,
            'DEST_HOST': '192.168.11.22',
            'DEST_PORT': 9200,
            'INDEX': index
        })
    )

