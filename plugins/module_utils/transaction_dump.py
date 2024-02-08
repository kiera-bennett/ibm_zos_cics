# -*- coding: utf-8 -*-

# (c) Copyright IBM Corp. 2024
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)

from ansible_collections.ibm.ibm_zos_core.plugins.module_utils.dd_statement import DatasetDefinition
__metaclass__ = type


def _build_seq_data_set_definition_transaction_dump(data_set):   # type: (dict) -> DatasetDefinition
    definition = DatasetDefinition(
        dataset_name=data_set["name"],
        primary=data_set["primary"],
        primary_unit=data_set["unit"],
        block_size=BLOCK_SIZE_DEFAULT,
        record_length=RECORD_LENGTH_DEFAULT,
        record_format=RECORD_FORMAT,
        disposition=DISPOSITION,
        normal_disposition=NORMAL_DISP,
        conditional_disposition=CONDITION_DISP,
        type=TYPE
    )
    return definition


STATE_OPTIONS = ["absent", "initial", "warm"]
SPACE_PRIMARY_DEFAULT = 20
SPACE_TYPE_DEFAULT = "M"
SPACE_SECONDARY_DEFAULT = 4
BLOCK_SIZE_DEFAULT = 4096
RECORD_LENGTH_DEFAULT = 4092
RECORD_FORMAT = "VB"
TYPE = "SEQ"
DISPOSITION = "NEW"
NORMAL_DISP = "CATALOG"
CONDITION_DISP = "DELETE"
DESTINATION_OPTIONS = ["A", "B"]
DESTINATION_DEFAULT_VALUE = "A"
